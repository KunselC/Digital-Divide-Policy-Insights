#!/usr/bin/env python3
"""Debug script to check 3D model loading."""

import sys
from pathlib import Path

# Add frontend to path
sys.path.append('frontend')
from components.ui_components import get_model_as_base64

def main():
    print("Debugging 3D model loading...")
    
    # Check if model file exists
    model_path = Path("frontend/assets/models/submarine_fiber_optic_cable_network.glb")
    print(f"Model file exists: {model_path.exists()}")
    
    if model_path.exists():
        print(f"Model file size: {model_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    # Try to load the model
    print("\nAttempting to load model as base64...")
    model_uri = get_model_as_base64("submarine_fiber_optic_cable_network.glb")
    
    if model_uri:
        print(f"✓ Model loaded successfully!")
        print(f"URI length: {len(model_uri):,} characters")
        print(f"URI preview: {model_uri[:100]}...")
        
        # Check if it's too large for browser
        if len(model_uri) > 15000000:
            print("⚠️  Model URI is very large - may cause browser issues")
        else:
            print("✓ Model URI size looks reasonable for browser")
    else:
        print("✗ Failed to load model!")

if __name__ == "__main__":
    main()
