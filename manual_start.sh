#!/bin/bash

# Manual startup script for Digital Divide Policy Insights platform
# Use this if you want to start services individually

echo "🚀 Digital Divide Policy Insights - Manual Startup"
echo ""

# Python path
PYTHON_CMD="/Users/kunselchodak/Class Project Files/Digital-Divide-Policy-Insights/.venv/bin/python"

echo "Choose an option:"
echo "1. Start API only"
echo "2. Start Frontend only"
echo "3. Start both services"
echo "4. Stop all services"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "🔧 Starting Flask API server..."
        cd api
        "$PYTHON_CMD" app.py
        ;;
    2)
        echo "🖥️ Starting Streamlit frontend..."
        "$PYTHON_CMD" -m streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
        ;;
    3)
        echo "🔧 Starting Flask API server in background..."
        cd api
        "$PYTHON_CMD" app.py &
        API_PID=$!
        cd ..
        sleep 3
        echo "🖥️ Starting Streamlit frontend..."
        "$PYTHON_CMD" -m streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
        ;;
    4)
        echo "🛑 Stopping all services..."
        pkill -f "python.*app.py"
        pkill -f streamlit
        echo "✅ All services stopped"
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac
