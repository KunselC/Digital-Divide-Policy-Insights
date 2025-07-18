#!/bin/bash

# Setup script for Digital Divide Policy Insights platform

echo "🚀 Setting up Digital Divide Policy Insights platform..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8 or later."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing Python packages..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file..."
    cp .env.example .env
    echo "✏️ Please edit .env file with your configuration (especially API keys)"
fi

# Create data directory if it doesn't exist
mkdir -p data/processed
mkdir -p data/raw

# Create logs directory
mkdir -p logs

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit the .env file with your configuration"
echo "2. Start the Flask API: python api/app.py"
echo "3. In a new terminal, start Streamlit: streamlit run frontend/Home.py"
echo ""
echo "🌐 Your application will be available at:"
echo "   - API: http://localhost:5000"
echo "   - Frontend: http://localhost:8501"
echo ""
