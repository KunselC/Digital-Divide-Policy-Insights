# Digital Divide Policy Insights

A comprehensive platform for analyzing technology policies and their effectiveness in addressing the digital divide.

## Features

- **Policy Dashboard**: Interactive visualizations of policy data and effectiveness metrics
- **Timeline Analysis**: Compare policy implementation timelines with digital divide indicators
- **AI-Powered Chatbot**: Query policies and their effectiveness using natural language
- **Data Visualization**: Interactive charts and graphs showing policy impact

## Architecture

- **Backend**: Flask API for data management and processing
- **Frontend**: Streamlit for interactive dashboard and user interface
- **Data**: Policy data, effectiveness metrics, and digital divide indicators
- **AI**: Chatbot integration for policy queries and explanations

## Quick Start

1. **Clone and setup**:

```bash
git clone https://github.com/your-username/Digital-Divide-Policy-Insights.git
cd Digital-Divide-Policy-Insights
./setup.sh
```

2. **Start the platform**:

```bash
./start.sh
```

3. **Access the applications**:
   - **API**: http://localhost:5001
   - **Frontend**: http://localhost:8501

## Manual Setup

### Prerequisites

- Python 3.8 or later
- pip package manager

### Installation

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Set up environment variables**:

```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start the Flask API**:

```bash
python api/app.py
```

4. **Start the Streamlit frontend** (in a new terminal):

```bash
streamlit run frontend/Home.py
```

## Project Structure

```
.
├── .env
├── .env.example
├── .streamlit/
│   └── config.toml
├── LICENSE
├── README.md
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── models/
│   │   └── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── chatbot.py
│   │   ├── data.py
│   │   └── policies.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── data_service.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── frontend/
│   ├── Home.py
│   ├── assets/
│   │   └── icons/
│   ├── components/
│   │   ├── __init__.py
│   │   └── ui_components.py
│   ├── config.py
│   └── pages/
│       ├── 1_Policy_Analysis.py
│       ├── 2_Data_Trends.py
│       ├── 3_AI_Chatbot.py
│       └── 4_About.py
├── requirements.txt
├── setup.sh
└── start.sh
```

## API Endpoints

### Policies

- `GET /api/policies/` - Get all policies
- `GET /api/policies/{id}` - Get specific policy
- `GET /api/policies/effectiveness` - Get effectiveness metrics
- `GET /api/policies/timeline` - Get policy timeline
- `GET /api/policies/search?q={query}` - Search policies

### Data Analysis

- `GET /api/data/indicators` - Get digital divide indicators
- `GET /api/data/trends` - Get trend analysis
- `GET /api/data/correlation` - Get correlation analysis
- `GET /api/data/demographics` - Get demographic breakdown

### Chatbot

- `POST /api/chatbot/chat` - Chat with AI assistant
- `GET /api/chatbot/policies` - Get available policies
- `GET /api/chatbot/suggestions` - Get conversation starters

## Current Policies Analyzed

1. **Digital Equity Act (2021)** - Federal legislation ensuring equitable digital access

   - Effectiveness Score: 7.5/10
   - Focus: Rural connectivity, digital literacy, device access

2. **Affordable Connectivity Program (2021)** - Discounted internet for eligible households

   - Effectiveness Score: 8.2/10
   - Impact: 14.5M households served, 45% cost reduction

3. **Rural Digital Opportunity Fund (2020)** - FCC program for rural broadband infrastructure
   - Effectiveness Score: 6.8/10
   - Coverage: 5.2M areas, 85.7% speed improvement

## Features Overview

### Dashboard

- Real-time policy effectiveness metrics
- Interactive charts showing broadband access trends
- Comparison tools for policy analysis

### Policy Analysis

- Detailed policy information and metrics
- Effectiveness scoring and visualization
- Timeline correlation with digital indicators

### Data Trends

- Historical trend analysis (2020-2023)
- Demographic breakdowns by income, geography, age
- Correlation analysis between policies and outcomes

### AI Chatbot

- Natural language queries about policies
- Policy effectiveness explanations
- Comparison and recommendation features

## Data Sources

- Federal Communications Commission (FCC)
- National Telecommunications and Information Administration (NTIA)
- U.S. Census Bureau
- Pew Research Center

## Technology Stack

- **Backend**: Flask, Python 3.8+
- **Frontend**: Streamlit
- **Visualization**: Plotly, Altair
- **Data Processing**: Pandas, NumPy
- **API**: RESTful Flask API
- **Environment**: Virtual Environment (.venv)

## Development

### Testing

Run the setup verification script:

```bash
python test_setup.py
```

### Configuration

Edit `.env` file to customize:

- API port (default: 5001)
- Streamlit port (default: 8501)
- API keys for external services
- Database settings

### Adding New Policies

1. Add policy data to `data/sample_data.py`
2. Update API routes in `api/routes/policies.py`
3. Extend chatbot knowledge in `api/routes/chatbot.py`

## Troubleshooting

### Port Conflicts

If port 5000 is in use (common on macOS due to AirPlay):

- The platform is configured to use port 5001 by default
- You can change ports in the `.env` file

### Package Installation Issues

```bash
# Recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### API Connection Issues

- Ensure Flask API is running before starting Streamlit
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
2. Run `python test_setup.py` to verify setup
3. Review the API documentation above
4. Create an issue in the repository
