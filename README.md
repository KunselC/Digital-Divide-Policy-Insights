# NetEquity

A modern analytics platform for exploring and understanding policies designed to close the digital divide.

## 🚀 Quick Start

### Option 1: Local Development

To run the NetEquity platform on your local machine, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/KunselC/Digital-Divide-Policy-Insights.git
cd Digital-Divide-Policy-Insights

# 2. Install the required Python packages
pip install -r requirements.txt

# 3. Run the Streamlit application
cd frontend
streamlit run Home.py
```

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

## 🏗️ Project Structure

```
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
└── README.md
```

## 🛠️ Technology Stack

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
