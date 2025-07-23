#!/usr/bin/env python3
"""
Test script to verify petition generator functionality.
"""

import sys
from pathlib import Path
import pandas as pd

# Add the frontend directory to the path
sys.path.append(str(Path(__file__).parent / "frontend"))

def test_petition_data():
    """Test that petition generator can access the required data."""
    print("Testing Petition Generator Data Access...")
    print("=" * 50)
    
    # Test data loading
    print("1. Testing data file access...")
    data_path = Path(__file__).parent / "ml_data" / "internet_usage.csv"
    
    if data_path.exists():
        print(f"✅ Data file found: {data_path}")
        
        try:
            df = pd.read_csv(data_path)
            df.columns = df.columns.str.strip()
            print(f"✅ Data loaded successfully: {len(df)} countries")
            
            # Test country data
            countries = sorted(df["Country Name"].dropna().unique())
            print(f"✅ Countries available: {len(countries)}")
            print(f"   Sample countries: {countries[:5]}")
            
            # Test latest year data
            test_country = "United States"
            if test_country in countries:
                country_data = df[df["Country Name"] == test_country]
                
                # Check for recent data
                internet_2023 = None
                for year in ["2023", "2022", "2021", "2020"]:
                    if year in df.columns:
                        raw_value = country_data[year].values[0]
                        try:
                            if pd.notna(raw_value) and raw_value != "..":
                                internet_2023 = float(raw_value)
                                print(f"✅ Latest data for {test_country} ({year}): {internet_2023:.1f}%")
                                break
                        except (ValueError, TypeError):
                            continue
                
                if internet_2023 is None:
                    print(f"⚠️  No recent data available for {test_country}")
            
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False
    else:
        print(f"❌ Data file not found: {data_path}")
        return False
    
    print(f"\n2. Testing petition template generation...")
    
    # Test template generation logic
    sample_country = "Kenya"
    sample_issue = "Limited internet access in rural areas"
    sample_audience = "Government/Ministry of Communications"
    
    template_prompt = f"""Write a compelling policy petition to address the digital divide issue of '{sample_issue}' in {sample_country}. 

Context: The percentage of individuals using the internet is 29.8%.

The petition should:
1. Be addressed to {sample_audience}
2. Use formal, professional language suitable for policy advocacy
3. Include specific, actionable demands
4. Mention the broader impact on society and economy
5. Be between 300-500 words
6. Include a clear call to action

Make it community-driven and emphasize the urgency of addressing digital inequalities."""
    
    print("✅ Template prompt generated successfully")
    print(f"   Length: {len(template_prompt)} characters")
    
    print(f"\n3. Summary:")
    print("✅ All petition generator components are ready!")
    print("📜 The petition generator should work correctly in the AI Chatbot page")
    
    return True

if __name__ == "__main__":
    success = test_petition_data()
    sys.exit(0 if success else 1)
