#!/bin/bash

# Startup script for Digital Divide Policy Insights platform

echo "🚀 Starting Digital Divide Policy Insights platform..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️ .env file not found. Using default configuration."
    cp .env.example .env
fi

# Function to start API server
start_api() {
    echo "🔧 Starting Flask API server..."
    cd api
    python app.py &
    API_PID=$!
    cd ..
    echo "✅ API server started (PID: $API_PID)"
}

# Function to start Streamlit frontend
start_frontend() {
    echo "🖥️ Starting Streamlit frontend..."
    streamlit run frontend/app.py &
    FRONTEND_PID=$!
    echo "✅ Frontend started (PID: $FRONTEND_PID)"
}

# Function to cleanup processes
cleanup() {
    echo ""
    echo "🛑 Shutting down services..."
    if [ ! -z "$API_PID" ]; then
        kill $API_PID 2>/dev/null
        echo "✅ API server stopped"
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
        echo "✅ Frontend stopped"
    fi
    echo "👋 Goodbye!"
    exit 0
}

# Trap signals to cleanup
trap cleanup SIGINT SIGTERM

# Start services
start_api
sleep 3  # Give API time to start
start_frontend

echo ""
echo "🌟 Platform is now running!"
echo "📡 API: http://localhost:5001"
echo "🖥️ Frontend: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for processes
wait
