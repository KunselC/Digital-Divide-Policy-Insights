# NetEquity

A modern analytics platform to explore and understand policies designed to close the digital divide.

## 🚀 Quick Start

### Option 1: Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
cd frontend
streamlit run Home.py
```

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
- **Policy Analysis**: Deep dive into individual policy details
- **AI Chatbot**: Ask questions about policies in plain English
- **Clean Modern UI**: Professional design with interactive background

## 🏗️ Project Structure

```
├── frontend/
│   ├── Home.py              # Main dashboard
│   ├── pages/               # Additional pages
│   ├── components/          # UI components
│   ├── assets/             # Icons and images
│   └── utils/              # Utilities
├── requirements.txt         # Dependencies
└── README.md
```

## 🛠️ Technology Stack

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
