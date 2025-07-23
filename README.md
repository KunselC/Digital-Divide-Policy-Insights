# NetEquity

<<<<<<< HEAD
A modern analytics platform to explore and understand policies designed to close the digital divide.
=======
A modern analytics platform for exploring and understanding policies designed to close the digital divide.

> > > > > > > origin/main

## 🚀 Quick Start

### Option 1: Local Development

<<<<<<< HEAD

````bash
# Install dependencies
pip install -r requirements.txt

# Run the app
=======
To run the NetEquity platform on your local machine, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/KunselC/Digital-Divide-Policy-Insights.git
cd Digital-Divide-Policy-Insights

# 2. Install the required Python packages
pip install -r requirements.txt

# 3. Run the Streamlit application
>>>>>>> origin/main
cd frontend
streamlit run Home.py
````

<<<<<<< HEAD

### Option 2: Deploy to Streamlit Cloud (Recommended)

1. **GitHub Repository**: `https://github.com/KunselC/Digital-Divide-Policy-Insights`
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub and click "New app"
4. Select repository: `KunselC/Digital-Divide-Policy-Insights`
5. Set main file path: `frontend/Home.py`
6. Optional app URL: `netequity` (or your preferred name)
7. Click "Deploy!"

Your app will be live at: `https://netequity.streamlit.app` (or your chosen URL)

## ✨ Features

- **Interactive Dashboard**: Policy effectiveness scores and key metrics
- **Data Trends**: Visualize digital divide indicators over time
- **AI Chatbot**: Ask questions about policies in plain English
- **ML Prediction**: Advanced machine learning models for digital divide prediction
  - Random Forest regression for web presence prediction
  - Feature importance analysis
  - Interactive model training and evaluation
  - Scenario-based predictions
- # **Clean Modern UI**: Professional design with interactive background
  The application will be accessible at `http://localhost:8501`.

### Option 2: Deploy to Streamlit Cloud (Recommended)

Deploying on Streamlit Cloud is the easiest way to share the application.

1.  **Fork and Clone**: Fork this repository to your own GitHub account.
2.  **Sign Up**: Go to [share.streamlit.io](https://share.streamlit.io) and sign up using your GitHub account.
3.  **Deploy**:
    - Click **"New app"**.
    - Select your forked repository.
    - Set the main file path to `frontend/Home.py`.
    - Click **"Deploy!"**.

Your application will be live on its own `.streamlit.app` URL.

## ✨ Features

- **Interactive Dashboard**: At-a-glance view of policy effectiveness scores and key digital divide metrics.
- **Data Trends Analysis**: Visualize historical data and trends for various digital divide indicators.
- **In-Depth Policy Review**: Access detailed information and analysis for individual policies.
- **AI-Powered Chatbot**: Get plain-English answers to your questions about digital divide policies.
- **Predictive Modeling**: Use a Random Forest regression model to predict digital inclusion metrics and understand key drivers through feature importance analysis.
- **Modern, Clean UI**: A professional and responsive interface built for clarity and ease of use.
  > > > > > > > origin/main

## 🏗️ Project Structure

```
<<<<<<< HEAD
├── frontend/
│   ├── Home.py              # Main dashboard
│   ├── pages/               # Additional pages
│   │   ├── 5_ML_Prediction.py # Machine learning predictions
│   │   └── ...
│   ├── components/          # UI components
│   ├── assets/             # Icons and images
│   └── utils/              # Utilities
│       └── ml_predictor.py  # ML model classes
├── data/                    # Sample datasets
├── models/                  # Trained ML models
├── plots/                   # Generated plots
├── standalone_regression.py # Original regression script
├── requirements.txt         # Dependencies
=======
.
├── frontend/
│   ├── Home.py              # Main application entry point
│   ├── pages/               # App pages (Dashboard, Trends, etc.)
│   ├── components/          # Reusable UI components
│   ├── assets/              # Static assets (icons, images)
│   └── utils/               # Utility scripts (API client, ML model)
├── data/                    # Sample datasets for analysis
├── models/                  # Saved machine learning models
├── plots/                   # Directory for generated plots
├── standalone_regression.py # Script for standalone ML analysis
├── requirements.txt         # Project dependencies
>>>>>>> origin/main
└── README.md
```

## 🛠️ Technology Stack

<<<<<<< HEAD

- **Frontend**: Streamlit with custom CSS/JS
- **Charts**: Plotly for interactive visualizations
- **Styling**: Modern glassmorphism design
- **Icons**: SVG icons with parallax effects

## 📱 Demo Features

The app includes realistic mock data to demonstrate:

- Policy effectiveness tracking
- Digital divide trend analysis
- Geographic and demographic breakdowns
- AI-powered policy Q&A

## 🎨 Design

- Clean, modern interface
- Interactive parallax background
- Glassmorphism cards and components
- Responsive design
- Professional color scheme

---

Built for exploring digital equity policies and their real-world impact.

- Check that `API_BASE_URL` in `.env` matches the API server address

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

See LICENSE file for details.

## Support

For questions or issues:

1. Check the troubleshooting section
2. Review the API documentation above
3. Create an issue in the repository

## 🤖 Machine Learning Features

The ML Prediction page offers advanced analytics capabilities:

### Model Training

- **Random Forest Regression**: Predict digital presence based on 8 key indicators
- **Automated Pipeline**: Data preprocessing, scaling, and imputation
- **Performance Metrics**: R² score, MSE, and cross-validation results

### Feature Analysis

- **Importance Scoring**: Identify which factors most influence digital presence
- **Interactive Visualization**: Bar charts and importance rankings
- **Factor Explanations**: Understand what drives digital adoption

### Prediction Interface

- **Interactive Sliders**: Adjust country parameters in real-time
- **Scenario Testing**: Compare developed, emerging, and rural scenarios
- **Instant Results**: Get predictions for web pages per million population

### Standalone Analysis

Run the comprehensive regression analysis independently:

```bash
python standalone_regression.py
```

This generates:

- Feature importance plots (`plots/feature_importance.png`)
- Trained model file (`models/regression_model.pkl`)
- # Detailed console output with model performance
- **Frontend**: Streamlit
- **Data Analysis & ML**: Pandas, Scikit-learn, Matplotlib, Seaborn
- **Visualizations**: Plotly for interactive charts
- **Styling**: Custom CSS for a polished, modern design

## 📱 Demo Mode

The application runs with a mock API client by default, using realistic sample data to showcase all features without requiring a live backend. This makes it easy to explore and demonstrate the platform's capabilities.

## 🎨 Design Philosophy

- **Clarity First**: A clean, intuitive interface that makes complex data accessible.
- **Professional Aesthetic**: A modern color scheme and layout suitable for policy and data analysis.
- **Responsive**: Ensures a seamless experience across different screen sizes.

---

This project was built to provide actionable insights into digital equity and the policies that shape it.

> > > > > > > origin/main
