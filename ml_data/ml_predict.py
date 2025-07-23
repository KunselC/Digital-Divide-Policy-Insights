
# --- Imports ---
import numpy as np
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, StackingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, BayesianRidge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from fuzzywuzzy import process

warnings.filterwarnings("ignore")

# --- Load Data ---
usage = pd.read_csv("ml_data/internet_usage.csv")
usage.replace('..', np.nan, inplace=True)
usage.replace({'..': np.nan, 'N/A': np.nan, 'n/a': np.nan}, inplace=True)
usage.iloc[:, 2:] = usage.iloc[:, 2:].astype(float)

un_data = pd.read_csv("ml_data/country_profile_variables.csv")

# --- Fuzzy Match Country Names ---
usage_subset = usage[['Country Name', '2017']].copy()
usage_subset = usage_subset.rename(columns={'Country Name': 'Country_usage'})
un_data = un_data.rename(columns={'country': 'Country_un'})
matched_names = {}
for name in usage_subset['Country_usage']:
    best_match, score = process.extractOne(name, un_data['Country_un'].tolist())
    matched_names[name] = best_match if score >= 85 else None
usage_subset['Country_un'] = usage_subset['Country_usage'].map(matched_names)
combined = pd.merge(
    usage_subset,
    un_data,
    how='left',
    on='Country_un'
)
combined = combined.drop(columns=['Country_un'])
combined = combined.rename(columns={'Country_usage': 'Country'})


missing = combined.isna().mean().sort_values(ascending=False)

combined_cleaned = combined.dropna(thresh=0.4 * combined.shape[1])

# --- Clean Combined Data ---
clean_combined = combined.replace(to_replace=[-99, '...', '-~0.0', '-99.0'], value=np.nan, inplace=False)
for col in clean_combined.columns[1:]:
    clean_combined[col] = pd.to_numeric(clean_combined[col], errors='coerce')

# --- Feature Engineering ---
df = clean_combined.copy()

df.replace(['-99', '...'], np.nan, inplace=True)

slash_cols = [c for c in df.columns 
              if df[c].dtype == object and df[c].str.contains('/', na=False).any()]

for col in slash_cols:
    ucol, rcol = f"{col}_urban", f"{col}_rural"
    df[[ucol, rcol]] = (
        df[col].str.split('/', expand=True)
              .apply(pd.to_numeric, errors='coerce')
    )
    df.drop(columns=[col], inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')

df = df.dropna(subset=['2017']).reset_index(drop=True)

X = df.drop(columns=['Country', '2017'])
y = df['2017']

numeric_cols = X.select_dtypes(include=['number']).columns.tolist()
categorical_cols = ['Region']  

preprocessor = ColumnTransformer([
    ('num', Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ]), numeric_cols),

    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
])

models = {
    'Linear Regression': LinearRegression(),
    'Ridge': Ridge(alpha=1.0, random_state=42),
    'Lasso': Lasso(alpha=0.1, random_state=42),
    'Elastic Net': ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42),
    'Bayesian Ridge': BayesianRidge(),
    'KNN': KNeighborsRegressor(n_neighbors=5),
    'SVR': SVR(kernel='rbf', C=1.0, epsilon=0.1),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'AdaBoost': AdaBoostRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
}

stack = StackingRegressor(
    estimators=[
        ('enet', ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)),
        ('br', BayesianRidge()),
        ('gbr', GradientBoostingRegressor(n_estimators=100, random_state=42)),
        ('rf', RandomForestRegressor(n_estimators=100, random_state=42)),
    ],
    final_estimator=Ridge(random_state=42),
    passthrough=False
)

models['Stacking'] = stack

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
stacking_pipeline = Pipeline([
    ('pre', preprocessor),
    ('model', stack)
])
stacking_pipeline.fit(X, y)

results = []
for name, estimator in models.items():
    pipe = Pipeline([
        ('pre', preprocessor),
        ('model', estimator)
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2  = r2_score(y_test, y_pred)
    results.append((name, mse, r2))

results_df = pd.DataFrame(results, columns=['Model', 'MSE', 'R2']) \
                   .sort_values('R2', ascending=False) \
                   .reset_index(drop=True)
def simulate_feature_change(pipeline, df, feature_name, pct_increase, top_n=10):
    """
    Simulate the effect of changing a feature by a percentage and return top N countries by percent change.
    Args:
        pipeline: Trained sklearn pipeline.
        df: DataFrame with country data.
        feature_name: Feature to change (string).
        pct_increase: Percentage increase (float).
        top_n: Number of top countries to return (int).
    Returns:
        DataFrame with country, original prediction, new prediction, and percent change.
    """
    # Check if feature exists
    if feature_name not in df.columns:
        return pd.DataFrame({'Error': [f"Feature '{feature_name}' not found in dataset."]})
    # Drop rows with missing feature or target
    data = df.dropna(subset=[feature_name, '2017']).copy()
    if data.empty:
        return pd.DataFrame({'Error': ["No data available for selected feature and year."]})
    # Ensure feature is numeric
    if not pd.api.types.is_numeric_dtype(data[feature_name]):
        try:
            data[feature_name] = pd.to_numeric(data[feature_name], errors='coerce')
        except Exception:
            return pd.DataFrame({'Error': [f"Feature '{feature_name}' could not be converted to numeric."]})
    X_raw = data.drop(columns=['Country', '2017'])
    try:
        base_preds = pipeline.predict(X_raw)
        X_mod = X_raw.copy()
        X_mod[feature_name] = X_mod[feature_name] * (1 + pct_increase/100)
        mod_preds = pipeline.predict(X_mod)
        pct_change = 100 * (mod_preds - base_preds) / base_preds
        results = pd.DataFrame({
            'Country': data['Country'],
            'Original 2017_pred': base_preds,
            f'{feature_name} +{pct_increase}%': mod_preds,
            'Percent Change': pct_change
        })
        return results.sort_values('Percent Change', ascending=False).head(top_n)
    except Exception as e:
        return pd.DataFrame({'Error': [f"Simulation failed: {str(e)}"]})

