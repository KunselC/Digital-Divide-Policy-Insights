#!/usr/bin/env python3
"""
Test script to verify 3D globe component functionality.
"""

import sys
from pathlib import Path

# Add the frontend directory to the path
sys.path.append(str(Path(__file__).parent / "frontend"))

from components.ui_components import get_model_as_base64, ASSETS_PATH

def test_3d_component():
    """Test the 3D component loading."""
    print("Testing 3D Globe Component...")
    print("=" * 50)
    
    # Test model loading
    print("1. Testing model loading...")
    model_uri = get_model_as_base64("submarine_fiber_optic_cable_network.glb")
    
    if model_uri:
        print(f"✅ Model URI generated successfully")
        print(f"   Length: {len(model_uri):,} characters")
        print(f"   Preview: {model_uri[:100]}...")
        
        # Check size
        if len(model_uri) > 10000000:  # 10MB
            print(f"⚠️  Large model detected ({len(model_uri):,} chars)")
        else:
            print(f"✅ Model size within limits")
    else:
        print("❌ Failed to generate model URI")
        return False
    
    # Test HTML template
    print("\n2. Testing HTML template...")
    template_path = ASSETS_PATH / "modern_3d.html"
    
    if template_path.exists():
        print(f"✅ HTML template found: {template_path}")
        
        with open(template_path, 'r') as f:
            template_content = f.read()
            
        if "{{MODEL_URI}}" in template_content:
            print("✅ Template contains MODEL_URI placeholder")
            
            # Test replacement
            html_content = template_content.replace("{{MODEL_URI}}", model_uri)
            if model_uri in html_content:
                print("✅ Template replacement works correctly")
            else:
                print("❌ Template replacement failed")
                return False
        else:
            print("❌ Template missing MODEL_URI placeholder")
            return False
    else:
        print(f"❌ HTML template not found: {template_path}")
        return False
    
    print("\n3. Summary:")
    print("✅ All 3D component tests passed!")
    print("🌐 The 3D globe should load correctly in Streamlit")
    
    return True

if __name__ == "__main__":
    success = test_3d_component()
    sys.exit(0 if success else 1)
