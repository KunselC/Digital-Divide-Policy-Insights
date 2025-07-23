"""
NetEquity - ML Prediction Module
Advanced machine learning analysis for digital divide prediction
"""

import streamlit as st
import sys
import os
import subprocess


# Add the parent directory to the path to import components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.ui_components import (
    display_page_header, 
    render_metric_card, 
    render_section_header,
    load_custom_css,
    display_interactive_background,
    get_icon
)
from utils.ml_predictor import DigitalDividePredictor
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure page
st.set_page_config(
    page_title="ML Prediction - NetEquity",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

def render_ml_page():
    """Render the ML prediction page with enhanced UI."""
    
    # Configure page styling
    load_custom_css()
    display_interactive_background()
    
    # Page header
    display_page_header(
        title="Machine Learning Predictions",
        subtitle="Advanced AI-driven analysis for digital divide insights",
        icon_name="ml-prediction.svg"
    )
    
    # Initialize predictor
    try:
        predictor = DigitalDividePredictor()
        
        # Create tabs for different sections
        tab1, tab2, tab3 = st.tabs(["Dataset Overview", "Model Training", "Make Predictions"])
        
        with tab1:
            render_dataset_overview(predictor)
        
        with tab2:
            render_model_training(predictor)
            
        with tab3:
            render_predictions_interface(predictor)
            
    except Exception as e:
        st.error(f"Error initializing ML module: {str(e)}")
        st.info("Please check that all required dependencies are installed and data files are available.")
def render_notebook_prediction_gui():
    """GUI for notebook-style prediction function."""
    st.subheader("Notebook-Style ML Prediction")
    st.caption("Enter feature values to predict using the notebook's ML logic.")

    # Feature inputs (matching notebook logic)
    with st.form("notebook_prediction_form"):
        st.write("**Enter values for prediction:**")
        internet_pen = st.number_input("Internet Penetration (%)", min_value=0.0, max_value=100.0, value=75.0)
        broadband_speed = st.number_input("Broadband Speed (Mbps)", min_value=0.0, max_value=100.0, value=40.0)
        gdp_per_capita = st.number_input("GDP per Capita ($)", min_value=0.0, max_value=100000.0, value=35000.0)
        electricity_access = st.number_input("Electricity Access (%)", min_value=0.0, max_value=100.0, value=95.0)
        urban_pop = st.number_input("Urban Population (%)", min_value=0.0, max_value=100.0, value=70.0)
        mobile_subs = st.number_input("Mobile Subscriptions (per 100)", min_value=0.0, max_value=200.0, value=120.0)
        edu_index = st.number_input("Education Index", min_value=0.0, max_value=1.0, value=0.85)
        cs_graduates = st.number_input("CS Graduates per Capita", min_value=0.0, max_value=50.0, value=15.0)
        submit_btn = st.form_submit_button("Predict")

    if submit_btn:
        # Use the same model logic as the notebook (RandomForestRegressor, etc.)
        import pandas as pd
        import numpy as np
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.impute import SimpleImputer
        from sklearn.preprocessing import StandardScaler
        from sklearn.pipeline import Pipeline

        # Load data (use local CSV for consistency)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        data_path = os.path.join(project_root, "data", "country_digital_features.csv")
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
        else:
            st.error(f"Dataset not found at {data_path}")
            return

        features = [
            'InternetPenetration', 'BroadbandSpeed', 'GDPperCapita',
            'ElectricityAccess', 'UrbanPopulation', 'MobileSubscriptions',
            'EduIndex', 'CSGraduatesPerCapita'
        ]
        target = 'WebPagesPerMillion'
        X = df[features]
        y = df[target]

        pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
            ("model", RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10, min_samples_split=5))
        ])
        pipeline.fit(X, y)

        input_data = np.array([[
            internet_pen, broadband_speed, gdp_per_capita, electricity_access,
            urban_pop, mobile_subs, edu_index, cs_graduates
        ]])
        prediction = pipeline.predict(input_data)

        st.success(f"Predicted Web Pages per Million: {prediction[0]:,.0f}")
def render_notebook_export(predictor):
    """Render the notebook export section as JSON."""
    st.subheader("Export ML Workflow as Notebook (JSON)")
    st.caption("Download or copy the ML workflow in a notebook-compatible JSON format.")

    # Prepare notebook cells
    cells = []

    # Cell 1: Markdown - Title
    cells.append({
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "# Digital Divide ML Prediction Workflow",
            "This notebook contains the steps for data loading, model training, feature analysis, and prediction."
        ]
    })

    # Cell 2: Code - Imports
    cells.append({
        "cell_type": "code",
        "metadata": {"language": "python"},
        "source": [
            "import pandas as pd",
            "import numpy as np",
            "from sklearn.ensemble import RandomForestRegressor",
            "from sklearn.model_selection import train_test_split",
            "from sklearn.metrics import r2_score, mean_squared_error",
            "from sklearn.preprocessing import StandardScaler",
            "from sklearn.pipeline import Pipeline"
        ]
    })

    # Cell 3: Markdown - Data Loading
    cells.append({
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## Load Dataset",
            "Load the country digital features dataset."
        ]
    })

    # Cell 4: Code - Data Loading
    cells.append({
        "cell_type": "code",
        "metadata": {"language": "python"},
        "source": [
            "df = pd.read_csv('../data/country_digital_features.csv')",
            "df.head()"
        ]
    })

    # Cell 5: Markdown - Model Training
    cells.append({
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## Train Random Forest Model",
            "Train a Random Forest regressor to predict web pages per million."
        ]
    })

    # Cell 6: Code - Model Training
    cells.append({
        "cell_type": "code",
        "metadata": {"language": "python"},
        "source": [
            "features = [",
            "    'InternetPenetration', 'BroadbandSpeed', 'GDPperCapita',",
            "    'ElectricityAccess', 'UrbanPopulation', 'MobileSubscriptions',",
            "    'EduIndex', 'CSGraduatesPerCapita'",
            "]",
            "target = 'WebPagesPerMillion'",
            "X = df[features]",
            "y = df[target]",
            "pipeline = Pipeline([",
            "    ('imputer', SimpleImputer(strategy='mean')),",
            "    ('scaler', StandardScaler()),",
            "    ('model', RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10, min_samples_split=5))",
            "])",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
            "pipeline.fit(X_train, y_train)",
            "predictions = pipeline.predict(X_test)",
            "r2 = r2_score(y_test, predictions)",
            "mse = mean_squared_error(y_test, predictions)",
            "print('R2 Score:', r2)",
            "print('MSE:', mse)"
        ]
    })

    # Cell 7: Markdown - Feature Importance
    cells.append({
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## Feature Importance",
            "Analyze which features most influence digital presence."
        ]
    })

    # Cell 8: Code - Feature Importance
    cells.append({
        "cell_type": "code",
        "metadata": {"language": "python"},
        "source": [
            "importances = pipeline.named_steps['model'].feature_importances_",
            "for feature, importance in zip(features, importances):",
            "    print(f'{feature}: {importance:.3f}')"
        ]
    })

    # Cell 9: Markdown - Prediction
    cells.append({
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": [
            "## Make Predictions",
            "Use the trained model to predict web presence for new scenarios."
        ]
    })

    # Cell 10: Code - Prediction Example
    cells.append({
        "cell_type": "code",
        "metadata": {"language": "python"},
        "source": [
            "sample_input = np.array([[90, 80, 60000, 100, 80, 120, 0.9, 25]])",
            "pred = pipeline.predict(sample_input)",
            "print('Predicted Web Pages per Million:', pred[0])"
        ]
    })

    # Output JSON
    notebook_json = {
        "cells": cells
    }

    st.code(
        notebook_json,
        language="json",
        line_numbers=True
    )

    # Add a section to run the original regression script
    st.subheader("🔬 Advanced Analysis")
    st.caption("Run the comprehensive regression analysis with detailed output")
    
    if st.button("Run Complete Regression Analysis", type="secondary"):
        with st.spinner("Running comprehensive regression analysis..."):
            # Run the standalone script
            import subprocess
            import sys
            
            try:
                result = subprocess.run([
                    sys.executable, "standalone_regression.py"
                ], capture_output=True, text=True, cwd=os.getcwd())
                
                if result.returncode == 0:
                    st.success("Analysis completed successfully!")
                    
                    # Show the output
                    with st.expander("Analysis Output"):
                        st.code(result.stdout, language="text")
                    
                    # Show the plot if it was generated
                    plot_path = "plots/feature_importance.png"
                    if os.path.exists(plot_path):
                        st.image(plot_path, caption="Generated Feature Importance Plot")
                else:
                    st.error(f"Analysis failed: {result.stderr}")
                    
            except Exception as e:
                st.error(f"Error running analysis: {str(e)}")

def render_dataset_overview(predictor):
    """Render the dataset overview section."""
    st.markdown("### Dataset Overview")
    
    try:
        # Load data
        df = predictor.load_data()
        
        if df is not None and not df.empty:
            st.success(f"Dataset loaded successfully with {len(df)} countries")
            
            # Display basic statistics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                render_metric_card(
                    "Countries", 
                    str(len(df)), 
                    "Total countries in dataset"
                )
            
            with col2:
                render_metric_card(
                    "Features", 
                    str(len(predictor.features)), 
                    "Input features for prediction"
                )
            
            with col3:
                render_metric_card(
                    "Target Variable", 
                    "Web Pages/Million", 
                    "What we're predicting"
                )
            
            # Show data preview
            st.markdown("#### Data Preview")
            st.dataframe(df.head(10), use_container_width=True)
            
            # Show feature statistics
            st.markdown("#### Feature Statistics")
            feature_stats = df[predictor.features].describe()
            st.dataframe(feature_stats, use_container_width=True)
            
        else:
            st.error("Failed to load dataset")
            
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")

def render_model_training(predictor):
    """Render the model training section."""
    st.markdown("### Model Training & Evaluation")
    
    try:
        # Load and train model
        df = predictor.load_data()
        
        if df is not None and not df.empty:
            if st.button("Train Model", type="primary"):
                with st.spinner("Training machine learning model..."):
                    results = predictor.train_model(df)
                
                if results:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        render_metric_card(
                            "R² Score", 
                            f"{results['r2_score']:.3f}", 
                            "Model accuracy (higher is better)"
                        )
                    
                    with col2:
                        render_metric_card(
                            "MSE", 
                            f"{results['mse']:,.0f}", 
                            "Mean Squared Error (lower is better)"
                        )
                    
                    # Show feature importance if available
                    try:
                        importance = predictor.get_feature_importance()
                        if importance is not None:
                            st.markdown("#### Feature Importance")
                            importance_df = pd.DataFrame({
                                'Feature': predictor.features,
                                'Importance': importance
                            }).sort_values('Importance', ascending=False)
                            
                            st.bar_chart(importance_df.set_index('Feature'))
                    except:
                        pass
                        
        else:
            st.error("Cannot train model: Dataset not available")
            
    except Exception as e:
        st.error(f"Error training model: {str(e)}")

def render_predictions_interface(predictor):
    """Render the predictions interface."""
    st.markdown("### Make Predictions")
    
    # Load and train model first
    try:
        df = predictor.load_data()
        if df is not None and not df.empty:
            # Train the model
            results = predictor.train_model(df)
            
            st.markdown("#### Input Feature Values")
            st.caption("Adjust the values below to see how they affect digital divide predictions")
            
            # Create input fields for each feature
            col1, col2 = st.columns(2)
            
            with col1:
                internet_pen = st.slider("Internet Penetration (%)", 0.0, 100.0, 75.0)
                broadband_speed = st.slider("Broadband Speed (Mbps)", 0.0, 100.0, 40.0)
                gdp_per_capita = st.slider("GDP per Capita ($)", 0, 100000, 35000)
                electricity_access = st.slider("Electricity Access (%)", 0.0, 100.0, 95.0)
            
            with col2:
                urban_pop = st.slider("Urban Population (%)", 0.0, 100.0, 70.0)
                mobile_subs = st.slider("Mobile Subscriptions (per 100)", 0.0, 200.0, 120.0)
                edu_index = st.slider("Education Index", 0.0, 1.0, 0.85)
                cs_graduates = st.slider("CS Graduates per Capita", 0.0, 50.0, 15.0)
            
            # Make prediction
            if st.button("Make Prediction", type="primary"):
                try:
                    input_data = np.array([[
                        internet_pen, broadband_speed, gdp_per_capita, electricity_access,
                        urban_pop, mobile_subs, edu_index, cs_graduates
                    ]])
                    
                    prediction = predictor.predict(input_data)
                    
                    if prediction is not None:
                        st.success("Prediction completed successfully!")
                        
                        # Display prediction
                        col1, col2, col3 = st.columns(3)
                        
                        with col2:  # Center the result
                            render_metric_card(
                                "Predicted Web Pages per Million", 
                                f"{prediction[0]:,.0f}", 
                                "Expected digital content creation"
                            )
                        
                        # Show prediction context
                        st.markdown("#### Prediction Context")
                        avg_target = df[predictor.target].mean()
                        
                        if prediction[0] > avg_target:
                            st.success(f"This prediction ({prediction[0]:,.0f}) is above the global average ({avg_target:,.0f}), indicating strong digital presence.")
                        else:
                            st.warning(f"This prediction ({prediction[0]:,.0f}) is below the global average ({avg_target:,.0f}), suggesting potential for digital growth.")
                            
                    else:
                        st.error("Failed to make prediction")
                        
                except Exception as e:
                    st.error(f"Error making prediction: {str(e)}")
            
            # Preset scenarios
            st.markdown("#### Quick Scenarios")
            st.caption("Try these preset scenarios to see different prediction outcomes")
            
            col1, col2, col3 = st.columns(3)
            
            scenarios = {
                "Developed Country": {
                    "internet": 90.0, "broadband": 80.0, "gdp": 50000, "electricity": 100.0,
                    "urban": 85.0, "mobile": 150.0, "education": 0.95, "cs_grads": 25.0
                },
                "Developing Country": {
                    "internet": 45.0, "broadband": 15.0, "gdp": 8000, "electricity": 75.0,
                    "urban": 55.0, "mobile": 80.0, "education": 0.65, "cs_grads": 5.0
                },
                "Emerging Economy": {
                    "internet": 70.0, "broadband": 35.0, "gdp": 25000, "electricity": 90.0,
                    "urban": 70.0, "mobile": 110.0, "education": 0.80, "cs_grads": 12.0
                }
            }
            
            for i, (scenario_name, values) in enumerate(scenarios.items()):
                col = [col1, col2, col3][i]
                
                with col:
                    if st.button(scenario_name, use_container_width=True):
                        input_data = np.array([[
                            values["internet"], values["broadband"], values["gdp"], values["electricity"],
                            values["urban"], values["mobile"], values["education"], values["cs_grads"]
                        ]])
                        
                        prediction = predictor.predict(input_data)
                        if prediction is not None:
                            st.metric(
                                "Predicted Web Pages",
                                f"{prediction[0]:,.0f}",
                                help="Web pages per million population"
                            )
        
            # Add feature simulation section
            st.markdown("---")
            render_feature_simulation()
            
        else:
            st.error("Cannot make predictions: Dataset not available")
            
    except Exception as e:
        st.error(f"Error in predictions interface: {str(e)}")

def render_feature_simulation():
    """Render feature simulation section."""
    st.subheader("Feature Impact Simulation")
    st.caption("Simulate the effect of changing a feature on digital divide predictions")
    
    # Feature selection - using actual feature names from the ML data
    available_features = [
        'GDP per capita (current US$)',
        'Urban population (% of total population)',
        'Mobile-cellular subscriptions (per 100 inhabitants)',
        'Individuals using the Internet (per 100 inhabitants)',
        'Education: Government expenditure (% of GDP)',
        'Education: Tertiary gross enrol. ratio (f/m per 100 pop.)',
        'Health: Total expenditure (% of GDP)',
        'Employment: Services (% of employed)',
        'Economy: Services and other activity (% of GVA)',
        'Population density (per km2, 2017)',
        'Life expectancy at birth (females/males, years)',
        'Seats held by women in national parliaments %'
    ]
    
    selected_feature = st.selectbox(
        "Select Feature to Modify", 
        available_features,
        help="Choose which feature to simulate changes for"
    )
    
    pct_increase = st.number_input("Percentage Change (+/-)", min_value=-100.0, max_value=100.0, value=10.0, step=1.0)
    top_n = st.number_input("Show Top N Countries", min_value=1, max_value=20, value=10, step=1)

    # --- Prediction Trigger ---
    if st.button("Run Simulation"):
        try:
            # Add the project root to sys.path to import ml_data module
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            sys.path.append(project_root)
            
            # Change working directory to project root temporarily
            original_cwd = os.getcwd()
            os.chdir(project_root)
            
            from ml_data.ml_predict import simulate_feature_change, stacking_pipeline, df
            results_df = simulate_feature_change(
                stacking_pipeline,
                df,
                selected_feature,
                pct_increase,
                top_n=top_n
            )
            
            # Restore original working directory
            os.chdir(original_cwd)
            
            st.success(f"Simulation complete for {selected_feature} +{pct_increase}%")
            st.dataframe(results_df)
        except Exception as e:
            # Restore original working directory in case of error
            try:
                os.chdir(original_cwd)
            except:
                pass
            st.error(f"Error running simulation: {e}")
            import traceback
            st.error(traceback.format_exc())

    # --- Existing Dataset Preview ---
    st.subheader("Dataset Overview")
    ml_data_path = "ml_data/internet_usage.csv"
    if os.path.exists(ml_data_path):
        ml_df = pd.read_csv(ml_data_path)
        st.write("**internet_usage.csv**")
        st.dataframe(
            ml_df.head(10),
            use_container_width=True,
            hide_index=True
        )
        col1, col2 = st.columns(2)
        if 'InternetPenetration' in ml_df.columns:
            with col1:
                st.info(
                    f"**Internet Penetration Range**: {ml_df['InternetPenetration'].min():.1f}% - "
                    f"{ml_df['InternetPenetration'].max():.1f}%"
                )
        if 'WebPagesPerMillion' in ml_df.columns:
            with col2:
                st.info(
                    f"**Web Pages Range**: {ml_df['WebPagesPerMillion'].min():.0f} - "
                    f"{ml_df['WebPagesPerMillion'].max():.0f} per million"
                )

    profile_data_path = "ml_data/country_profile_variables.csv"
    if os.path.exists(profile_data_path):
        profile_df = pd.read_csv(profile_data_path)
        st.write("**country_profile_variables.csv**")
        st.dataframe(
            profile_df.head(10),
            use_container_width=True,
            hide_index=True
        )

def render_model_training(predictor):
    """Render the model training section."""
    st.subheader("Train Prediction Model")
    st.caption("Build a Random Forest model to predict digital presence")
    
    # Load data
    df = predictor.load_data()
    
    # Training configuration
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("**Model Configuration**")
        st.write("- **Algorithm**: Random Forest Regression")
        st.write("- **Features**: 8 digital and economic indicators")
        st.write("- **Target**: Web pages per million population")
        st.write("- **Validation**: 80/20 train-test split")
    
    with col2:
        train_button = st.button(
            "Train Model",
            type="primary",
            use_container_width=True,
            help="Train the machine learning model"
        )
    
    # Training results
    if train_button or 'model_results' in st.session_state:
        if train_button:
            with st.spinner("Training model... This may take a moment."):
                results = predictor.train_model(df)
                st.session_state.model_results = results
                st.session_state.trained_predictor = predictor
        
        results = st.session_state.model_results
        
        # Success message
        st.success("Model training completed successfully!")
        
        # Performance metrics
        st.subheader("Model Performance")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            render_metric_card("R² Score", f"{results['r2_score']:.3f}")
        
        with col2:
            render_metric_card("MSE", f"{results['mse']:.0f}")
        
        with col3:
            render_metric_card("Training Size", str(results['training_samples']))
        
        with col4:
            render_metric_card("Test Size", str(results['test_samples']))
        
        # Performance visualization
        st.subheader("Prediction Accuracy")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(results['y_test'], results['predictions'], alpha=0.7, color='#00d4ff', s=60)
        ax.plot([results['y_test'].min(), results['y_test'].max()], 
                [results['y_test'].min(), results['y_test'].max()], 
                color='#ff6b6b', linestyle='--', linewidth=2, label='Perfect Prediction')
        
        ax.set_xlabel('Actual Web Pages per Million')
        ax.set_ylabel('Predicted Web Pages per Million')
        ax.set_title('Model Prediction Accuracy')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Set dark theme
        fig.patch.set_facecolor('#0e1117')
        ax.set_facecolor('#0e1117')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        
        st.pyplot(fig)
        plt.close()

def render_feature_analysis(predictor):
    """Render the feature importance analysis."""
    st.subheader("Feature Importance Analysis")
    st.caption("Understand which factors most influence digital presence")
    
    if 'trained_predictor' not in st.session_state:
        st.warning("Please train the model first in the 'Model Training' tab.")
        return
    
    trained_predictor = st.session_state.trained_predictor
    importance_df = trained_predictor.get_feature_importance()
    
    if importance_df is None:
        st.error("Unable to get feature importance. Please retrain the model.")
        return
    
    # Feature importance visualization
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.barplot(
            data=importance_df, 
            x='importance', 
            y='feature', 
            ax=ax, 
            palette='viridis'
        )
        ax.set_title('Feature Importance: Digital Presence Drivers')
        ax.set_xlabel('Importance Score')
        ax.set_ylabel('')
        
        # Set dark theme
        fig.patch.set_facecolor('#0e1117')
        ax.set_facecolor('#0e1117')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    
    with col2:
        st.write("**Top Factors**")
        top_features = importance_df.tail(3)
        
        for i, (_, row) in enumerate(top_features.iterrows()):
            rank = len(top_features) - i
            render_metric_card(f"#{rank} {row['feature']}", f"{row['importance']:.3f}")
    
    # Feature explanations
    st.subheader("Understanding the Features")
    
    feature_explanations = {
        'InternetPenetration': "Percentage of population with internet access",
        'BroadbandSpeed': "Average broadband speed in Mbps",
        'GDPperCapita': "Gross domestic product per person",
        'ElectricityAccess': "Percentage with reliable electricity",
        'UrbanPopulation': "Percentage living in urban areas",
        'MobileSubscriptions': "Mobile subscriptions per 100 people",
        'EduIndex': "Education development index (0-1)",
        'CSGraduatesPerCapita': "Computer science graduates per capita"
    }
    
    for feature, explanation in feature_explanations.items():
        importance = importance_df[importance_df['feature'] == feature]['importance'].iloc[0]
        st.write(f"**{feature}** (Score: {importance:.3f}): {explanation}")
    
    # Show the feature importance plot if it exists
    plot_path = "plots/feature_importance.png"
    if os.path.exists(plot_path):
        st.subheader("Generated Feature Importance Plot")
        st.image(plot_path, caption="Feature importance plot from the regression model")

def render_prediction_interface(predictor):
    """Render the prediction interface."""
    st.subheader("Make Digital Presence Predictions")
    st.caption("Use the trained model to predict web presence for different scenarios")
    
    if 'trained_predictor' not in st.session_state:
        st.warning("Please train the model first in the 'Model Training' tab.")
        return
    
    trained_predictor = st.session_state.trained_predictor
    
    st.write("**Enter values for a country or scenario:**")
    
    # Input interface
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Infrastructure & Economy**")
        internet_pen = st.slider(
            "Internet Penetration (%)", 
            0.0, 100.0, 75.0, 
            help="Percentage of population with internet access"
        )
        broadband_speed = st.slider(
            "Broadband Speed (Mbps)", 
            0.0, 100.0, 40.0,
            help="Average broadband connection speed"
        )
        gdp_per_capita = st.slider(
            "GDP per Capita ($)", 
            5000, 100000, 35000,
            help="Economic prosperity indicator"
        )
        electricity_access = st.slider(
            "Electricity Access (%)", 
            0.0, 100.0, 95.0,
            help="Reliable electricity infrastructure"
        )
    
    with col2:
        st.write("**Demographics & Education**")
        urban_pop = st.slider(
            "Urban Population (%)", 
            0.0, 100.0, 70.0,
            help="Percentage living in cities"
        )
        mobile_subs = st.slider(
            "Mobile Subscriptions (per 100)", 
            0.0, 200.0, 120.0,
            help="Mobile phone penetration"
        )
        edu_index = st.slider(
            "Education Index", 
            0.0, 1.0, 0.85,
            help="Education development level"
        )
        cs_graduates = st.slider(
            "CS Graduates per Capita", 
            0.0, 50.0, 15.0,
            help="Technical education output"
        )
    
    # Prediction
    col1, col2 = st.columns([1, 2])
    
    with col1:
        predict_button = st.button(
            "Make Prediction",
            type="primary",
            use_container_width=True
        )
    
    if predict_button:
        input_data = np.array([[
            internet_pen, broadband_speed, gdp_per_capita, electricity_access,
            urban_pop, mobile_subs, edu_index, cs_graduates
        ]])
        
        prediction = trained_predictor.predict(input_data)
        
        if prediction is not None:
            with col2:
                render_metric_card("Predicted Web Presence", f"{prediction[0]:,.0f}")
            
            # Interpretation
            st.subheader("Prediction Insights")
            
            if prediction[0] > 3000:
                st.success("**High Digital Presence**: This scenario indicates strong web engagement and digital economy participation.")
            elif prediction[0] > 1500:
                st.info("**Moderate Digital Presence**: Good foundation with room for growth in digital infrastructure.")
            else:
                st.warning("**Low Digital Presence**: Significant opportunities for digital development and infrastructure investment.")
        else:
            st.error("Unable to make prediction. Please check the model training.")
    
    # Scenario presets
    st.subheader("Quick Scenarios")
    st.caption("Try these preset scenarios to see how different factors affect digital presence")
    
    scenarios = {
        "🇺🇸 Developed Country": {
            "internet": 90, "broadband": 80, "gdp": 60000, "electricity": 100,
            "urban": 80, "mobile": 120, "education": 0.9, "cs_grads": 25
        },
        "Emerging Economy": {
            "internet": 60, "broadband": 25, "gdp": 15000, "electricity": 85,
            "urban": 50, "mobile": 100, "education": 0.7, "cs_grads": 10
        },
        "Rural/Remote Area": {
            "internet": 30, "broadband": 10, "gdp": 8000, "electricity": 60,
            "urban": 20, "mobile": 80, "education": 0.5, "cs_grads": 3
        }
    }
    
    col1, col2, col3 = st.columns(3)
    
    for i, (scenario_name, values) in enumerate(scenarios.items()):
        col = [col1, col2, col3][i]
        
        with col:
            if st.button(scenario_name, use_container_width=True):
                input_data = np.array([[
                    values["internet"], values["broadband"], values["gdp"], values["electricity"],
                    values["urban"], values["mobile"], values["education"], values["cs_grads"]
                ]])
                
                prediction = trained_predictor.predict(input_data)
                if prediction is not None:
                    st.metric(
                        "Predicted Web Pages",
                        f"{prediction[0]:,.0f}",
                        help="Web pages per million population"
                    )

if __name__ == "__main__":
    render_ml_page()
