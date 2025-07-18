"""
Machine Learning Module for Digital Divide Predictions
"""

import os
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


class DigitalDividePredictor:
    """Machine Learning model for predicting digital divide indicators."""
    
    def __init__(self):
        self.pipeline = None
        self.features = ['InternetPenetration', 'BroadbandSpeed', 'GDPperCapita',
                        'ElectricityAccess', 'UrbanPopulation', 'MobileSubscriptions',
                        'EduIndex', 'CSGraduatesPerCapita']
        self.target = 'WebPagesPerMillion'
        
    def load_data(self, data_path="data/country_digital_features.csv"):
        """Load and return the dataset."""
        if os.path.exists(data_path):
            df = pd.read_csv(data_path)
            return df
        else:
            # Create mock data if file doesn't exist
            return self._create_mock_data()
    
    def _create_mock_data(self):
        """Create mock data for demonstration."""
        np.random.seed(42)
        n_samples = 30
        
        data = {
            'Country': [f'Country_{i}' for i in range(n_samples)],
            'InternetPenetration': np.random.normal(75, 15, n_samples),
            'BroadbandSpeed': np.random.normal(40, 20, n_samples),
            'GDPperCapita': np.random.normal(35000, 15000, n_samples),
            'ElectricityAccess': np.random.normal(95, 10, n_samples),
            'UrbanPopulation': np.random.normal(70, 20, n_samples),
            'MobileSubscriptions': np.random.normal(120, 30, n_samples),
            'EduIndex': np.random.normal(0.85, 0.1, n_samples),
            'CSGraduatesPerCapita': np.random.normal(15, 8, n_samples),
            'WebPagesPerMillion': np.random.normal(2500, 1000, n_samples)
        }
        
        return pd.DataFrame(data)
    
    def train_model(self, df):
        """Train the machine learning model."""
        # Prepare features and target
        X = df[self.features]
        y = df[self.target]
        
        # Create pipeline
        self.pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
            ("model", RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10, min_samples_split=5))
        ])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        self.pipeline.fit(X_train, y_train)
        
        # Make predictions
        predictions = self.pipeline.predict(X_test)
        
        # Calculate metrics
        r2 = r2_score(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        
        return {
            'r2_score': r2,
            'mse': mse,
            'training_samples': len(X_train),
            'test_samples': len(X_test),
            'X_test': X_test,
            'y_test': y_test,
            'predictions': predictions
        }
    
    def get_feature_importance(self):
        """Get feature importance from the trained model."""
        if self.pipeline is None:
            return None
            
        model = self.pipeline.named_steps["model"]
        importances = model.feature_importances_
        
        return pd.DataFrame({
            'feature': self.features,
            'importance': importances
        }).sort_values('importance', ascending=True)
    
    def predict(self, input_data):
        """Make predictions on new data."""
        if self.pipeline is None:
            return None
            
        return self.pipeline.predict(input_data)
    
    def save_model(self, filepath="models/digital_divide_model.pkl"):
        """Save the trained model to disk."""
        if self.pipeline is None:
            raise ValueError("No model to save. Train the model first.")
            
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'wb') as f:
            pickle.dump(self.pipeline, f)
        
        return filepath
    
    def load_model(self, filepath="models/digital_divide_model.pkl"):
        """Load a trained model from disk."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Model file not found: {filepath}")
            
        with open(filepath, 'rb') as f:
            self.pipeline = pickle.load(f)
        
        return True


def render_ml_analysis():
    """Render the ML analysis section in Streamlit."""
    st.header("🤖 Machine Learning Analysis")
    st.subheader("Digital Divide Prediction Model")
    
    # Initialize predictor
    predictor = DigitalDividePredictor()
    
    # Load data
    with st.spinner("Loading data..."):
        df = predictor.load_data()
    
    # Display data info
    st.info(f"📊 Dataset loaded with {len(df)} countries and {len(predictor.features)} features")
    
    # Show data preview
    with st.expander("📋 View Dataset"):
        st.dataframe(df.head(10))
    
    # Train model
    if st.button("🚀 Train Model", type="primary"):
        with st.spinner("Training machine learning model..."):
            results = predictor.train_model(df)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("R² Score", f"{results['r2_score']:.4f}")
            st.metric("Training Samples", results['training_samples'])
        
        with col2:
            st.metric("Mean Squared Error", f"{results['mse']:.2f}")
            st.metric("Test Samples", results['test_samples'])
        
        # Feature importance
        importance_df = predictor.get_feature_importance()
        
        if importance_df is not None:
            st.subheader("🎯 Feature Importance")
            st.caption("What drives digital presence the most?")
            
            # Create horizontal bar chart
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=importance_df, x='importance', y='feature', ax=ax, palette='viridis')
            ax.set_title("Feature Importance: What Drives Web Presence")
            ax.set_xlabel("Importance Score")
            ax.set_ylabel("Features")
            plt.tight_layout()
            
            st.pyplot(fig)
            
            # Show top features
            st.subheader("🏆 Top Contributing Factors")
            top_features = importance_df.tail(3)
            
            for _, row in top_features.iterrows():
                st.write(f"**{row['feature']}**: {row['importance']:.3f}")
        
        # Model performance visualization
        st.subheader("📈 Model Performance")
        
        # Actual vs Predicted scatter plot
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        ax2.scatter(results['y_test'], results['predictions'], alpha=0.7, color='blue')
        ax2.plot([results['y_test'].min(), results['y_test'].max()], 
                [results['y_test'].min(), results['y_test'].max()], 'r--', lw=2)
        ax2.set_xlabel('Actual Values')
        ax2.set_ylabel('Predicted Values')
        ax2.set_title('Actual vs Predicted Web Pages per Million')
        plt.tight_layout()
        
        st.pyplot(fig2)
        
        # Save model
        model_path = predictor.save_model()
        st.success(f"✅ Model trained and saved successfully! Model file: {model_path}")
        
        # Prediction interface
        st.subheader("🔮 Make Predictions")
        st.caption("Enter values to predict web presence:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            internet_pen = st.slider("Internet Penetration (%)", 0.0, 100.0, 75.0)
            broadband_speed = st.slider("Broadband Speed (Mbps)", 0.0, 100.0, 40.0)
            gdp_per_capita = st.slider("GDP per Capita ($)", 5000, 100000, 35000)
            electricity_access = st.slider("Electricity Access (%)", 0.0, 100.0, 95.0)
        
        with col2:
            urban_pop = st.slider("Urban Population (%)", 0.0, 100.0, 70.0)
            mobile_subs = st.slider("Mobile Subscriptions (per 100)", 0.0, 200.0, 120.0)
            edu_index = st.slider("Education Index", 0.0, 1.0, 0.85)
            cs_graduates = st.slider("CS Graduates per Capita", 0.0, 50.0, 15.0)
        
        if st.button("🎯 Predict Web Presence"):
            input_data = np.array([[
                internet_pen, broadband_speed, gdp_per_capita, electricity_access,
                urban_pop, mobile_subs, edu_index, cs_graduates
            ]])
            
            prediction = predictor.predict(input_data)
            
            if prediction is not None:
                st.success(f"🌐 Predicted Web Pages per Million: **{prediction[0]:.0f}**")
            else:
                st.error("Model not trained yet. Please train the model first.")
    
    # Model loading example
    if st.button("📥 Load Pre-trained Model"):
        with st.spinner("Loading pre-trained model..."):
            try:
                predictor.load_model()
                st.success("✅ Pre-trained model loaded successfully!")
            except Exception as e:
                st.error(f"Error loading model: {e}")


if __name__ == "__main__":
    render_ml_analysis()
