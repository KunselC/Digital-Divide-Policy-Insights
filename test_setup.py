#!/usr/bin/env python3
"""
Test script to verify the Digital Divide Policy Insights platform setup
"""

import sys
import os
import subprocess
import requests
import time

def test_python_packages():
    """Test if required Python packages are installed"""
    print("🧪 Testing Python packages...")
    
    required_packages = [
        'flask', 'flask_cors', 'streamlit', 'pandas', 
        'numpy', 'plotly', 'requests', 'dotenv'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All packages installed successfully")
    return True

def test_api_imports():
    """Test if API imports work correctly"""
    print("\n🧪 Testing API imports...")
    
    try:
        # Change to api directory
        api_dir = os.path.join(os.path.dirname(__file__), 'api')
        sys.path.insert(0, api_dir)
        
        from routes.policies import policies_bp
        from routes.data import data_bp
        from routes.chatbot import chatbot_bp
        from models.policy import Policy
        
        print("  ✅ All API imports successful")
        return True
    
    except Exception as e:
        print(f"  ❌ API import error: {e}")
        return False

def test_api_server():
    """Test if API server can start (basic test)"""
    print("\n🧪 Testing API server startup...")
    
    try:
        # Start API server in background
        api_process = subprocess.Popen([
            sys.executable, 'api/app.py'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Test if server is responding
        try:
            response = requests.get('http://localhost:5001/health', timeout=5)
            if response.status_code == 200:
                print("  ✅ API server started successfully")
                success = True
            else:
                print(f"  ❌ API server returned status {response.status_code}")
                success = False
        except requests.RequestException as e:
            print(f"  ❌ Could not connect to API server: {e}")
            success = False
        
        # Stop the test server
        api_process.terminate()
        api_process.wait(timeout=5)
        
        return success
    
    except Exception as e:
        print(f"  ❌ Error testing API server: {e}")
        return False

def test_directory_structure():
    """Test if all required directories and files exist"""
    print("\n🧪 Testing directory structure...")
    
    required_files = [
        'requirements.txt',
        '.env.example',
        'README.md',
        'api/app.py',
        'api/routes/policies.py',
        'api/routes/data.py',
        'api/routes/chatbot.py',
        'api/models/policy.py',
        'frontend/app.py',
        'data/sample_data.py',
        'setup.sh',
        'start.sh'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def main():
    """Run all tests"""
    print("🚀 Digital Divide Policy Insights - Setup Test\n")
    
    tests = [
        ("Directory Structure", test_directory_structure),
        ("Python Packages", test_python_packages),
        ("API Imports", test_api_imports),
        ("API Server", test_api_server)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20} {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your platform is ready to use.")
        print("\nTo start the platform:")
        print("  ./start.sh")
        print("\nOr manually:")
        print("  1. python api/app.py")
        print("  2. streamlit run frontend/app.py")
    else:
        print(f"\n⚠️ {total - passed} test(s) failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
