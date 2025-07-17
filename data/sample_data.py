"""
Sample data for Digital Divide Policy Insights.

This module contains realistic sample data representing digital divide policies
and related indicators. In a production environment, this would be replaced
with connections to real databases and APIs.
"""

from typing import List, Dict, Any
from datetime import datetime


class SampleDataProvider:
    """Provider for sample policy and indicator data."""
    
    @staticmethod
    def get_policies() -> List[Dict[str, Any]]:
        """
        Get sample policy data.
        
        Returns:
            List of policy dictionaries with comprehensive metadata
        """
        return [
            {
                "id": 1,
                "name": "Digital Equity Act",
                "description": (
                    "Federal legislation aimed at ensuring equitable access to digital "
                    "technologies and promoting digital inclusion for all Americans"
                ),
                "implementation_date": "2021-11-15",
                "effectiveness_score": 7.5,
                "metrics": {
                    "broadband_access_increase": 15.2,
                    "digital_literacy_improvement": 12.8,
                    "rural_connectivity_boost": 22.1,
                    "funding_allocated_millions": 2750
                },
                "status": "active",
                "target_demographics": [
                    "rural_communities", 
                    "low_income_households", 
                    "tribal_areas"
                ],
                "key_provisions": [
                    "Digital equity grants to states",
                    "Digital inclusion planning",
                    "Workforce development programs",
                    "Device access programs"
                ]
            },
            {
                "id": 2,
                "name": "Affordable Connectivity Program",
                "description": (
                    "Program providing discounted internet service and device subsidies "
                    "to eligible low-income households"
                ),
                "implementation_date": "2021-12-31",
                "effectiveness_score": 8.2,
                "metrics": {
                    "households_served": 14500000,
                    "cost_reduction_percentage": 45.0,
                    "rural_participation_rate": 68.3,
                    "urban_participation_rate": 72.8,
                    "monthly_savings_per_household": 38.50
                },
                "status": "active",
                "target_demographics": [
                    "low_income_households", 
                    "veterans", 
                    "students", 
                    "seniors"
                ],
                "key_provisions": [
                    "$30/month internet discount",
                    "$75/month for tribal lands",
                    "One-time device discount up to $100",
                    "Simplified enrollment process"
                ]
            },
            {
                "id": 3,
                "name": "Rural Digital Opportunity Fund",
                "description": (
                    "FCC program to bring high-speed broadband infrastructure "
                    "to underserved rural areas across the United States"
                ),
                "implementation_date": "2020-10-29",
                "effectiveness_score": 6.8,
                "metrics": {
                    "areas_covered_thousands": 5200,
                    "speed_improvement_percentage": 85.7,
                    "completion_rate": 42.1,
                    "funding_committed_billions": 20.4,
                    "projected_population_served": 10300000
                },
                "status": "in_progress",
                "target_demographics": [
                    "rural_communities", 
                    "agricultural_areas", 
                    "small_towns"
                ],
                "key_provisions": [
                    "Broadband infrastructure funding",
                    "Minimum speed requirements (25/3 Mbps)",
                    "10-year service commitments",
                    "Performance monitoring requirements"
                ]
            }
        ]
    
    @staticmethod
    def get_indicators_timeline() -> Dict[str, List[Dict[str, Any]]]:
        """
        Get time-series data for digital divide indicators.
        
        Returns:
            Dictionary containing indicator timelines
        """
        return {
            "broadband_access": [
                {
                    "date": "2020-01-01", 
                    "percentage": 73.2, 
                    "rural": 63.1, 
                    "urban": 82.5, 
                    "low_income": 58.7
                },
                {
                    "date": "2020-06-01", 
                    "percentage": 74.1, 
                    "rural": 64.8, 
                    "urban": 83.2, 
                    "low_income": 60.1
                },
                {
                    "date": "2021-01-01", 
                    "percentage": 75.8, 
                    "rural": 67.2, 
                    "urban": 84.1, 
                    "low_income": 62.8
                },
                {
                    "date": "2021-06-01", 
                    "percentage": 78.5, 
                    "rural": 71.4, 
                    "urban": 85.8, 
                    "low_income": 66.4
                },
                {
                    "date": "2022-01-01", 
                    "percentage": 81.2, 
                    "rural": 75.6, 
                    "urban": 87.3, 
                    "low_income": 70.9
                },
                {
                    "date": "2022-06-01", 
                    "percentage": 83.8, 
                    "rural": 78.9, 
                    "urban": 88.9, 
                    "low_income": 74.2
                },
                {
                    "date": "2023-01-01", 
                    "percentage": 86.1, 
                    "rural": 82.1, 
                    "urban": 90.2, 
                    "low_income": 77.8
                },
                {
                    "date": "2023-06-01", 
                    "percentage": 87.9, 
                    "rural": 84.7, 
                    "urban": 91.4, 
                    "low_income": 80.5
                }
            ],
            "digital_literacy": [
                {
                    "date": "2020-01-01", 
                    "overall": 58.3, 
                    "age_18_34": 78.5, 
                    "age_35_54": 62.1, 
                    "age_55_plus": 38.7
                },
                {
                    "date": "2020-06-01", 
                    "overall": 59.1, 
                    "age_18_34": 79.2, 
                    "age_35_54": 63.4, 
                    "age_55_plus": 39.8
                },
                {
                    "date": "2021-01-01", 
                    "overall": 61.5, 
                    "age_18_34": 81.3, 
                    "age_35_54": 66.2, 
                    "age_55_plus": 42.1
                },
                {
                    "date": "2021-06-01", 
                    "overall": 64.8, 
                    "age_18_34": 83.7, 
                    "age_35_54": 69.8, 
                    "age_55_plus": 45.9
                },
                {
                    "date": "2022-01-01", 
                    "overall": 68.2, 
                    "age_18_34": 85.9, 
                    "age_35_54": 73.4, 
                    "age_55_plus": 49.8
                },
                {
                    "date": "2022-06-01", 
                    "overall": 71.5, 
                    "age_18_34": 87.8, 
                    "age_35_54": 76.9, 
                    "age_55_plus": 53.7
                },
                {
                    "date": "2023-01-01", 
                    "overall": 74.1, 
                    "age_18_34": 89.2, 
                    "age_35_54": 79.8, 
                    "age_55_plus": 57.2
                },
                {
                    "date": "2023-06-01", 
                    "overall": 76.8, 
                    "age_18_34": 90.7, 
                    "age_35_54": 82.4, 
                    "age_55_plus": 60.9
                }
            ],
            "device_ownership": [
                {
                    "date": "2020-01-01", 
                    "smartphone": 81.2, 
                    "computer": 69.4, 
                    "tablet": 45.8
                },
                {
                    "date": "2020-06-01", 
                    "smartphone": 82.1, 
                    "computer": 70.8, 
                    "tablet": 47.2
                },
                {
                    "date": "2021-01-01", 
                    "smartphone": 84.3, 
                    "computer": 73.5, 
                    "tablet": 49.7
                },
                {
                    "date": "2021-06-01", 
                    "smartphone": 86.7, 
                    "computer": 76.9, 
                    "tablet": 52.8
                },
                {
                    "date": "2022-01-01", 
                    "smartphone": 88.9, 
                    "computer": 80.1, 
                    "tablet": 56.2
                },
                {
                    "date": "2022-06-01", 
                    "smartphone": 90.8, 
                    "computer": 82.7, 
                    "tablet": 59.4
                },
                {
                    "date": "2023-01-01", 
                    "smartphone": 92.1, 
                    "computer": 85.3, 
                    "tablet": 62.8
                },
                {
                    "date": "2023-06-01", 
                    "smartphone": 93.5, 
                    "computer": 87.6, 
                    "tablet": 65.9
                }
            ]
        }
    
    @staticmethod
    def get_demographics_data() -> Dict[str, Dict[str, Any]]:
        """
        Get demographic breakdown data.
        
        Returns:
            Dictionary containing demographic analysis data
        """
        return {
            "income_levels": {
                "under_25k": {
                    "broadband_access": 62.3,
                    "digital_literacy": 48.7
                },
                "25k_50k": {
                    "broadband_access": 74.8,
                    "digital_literacy": 61.2
                },
                "50k_75k": {
                    "broadband_access": 86.4,
                    "digital_literacy": 73.9
                },
                "75k_100k": {
                    "broadband_access": 92.7,
                    "digital_literacy": 82.1
                },
                "over_100k": {
                    "broadband_access": 96.8,
                    "digital_literacy": 89.4
                }
            },
            "geographic": {
                "northeast": {"broadband_access": 91.2},
                "southeast": {"broadband_access": 83.7},
                "midwest": {"broadband_access": 85.9},
                "southwest": {"broadband_access": 86.4},
                "west": {"broadband_access": 89.8}
            },
            "age_groups": {
                "18-34": {"digital_literacy": 90.7},
                "35-54": {"digital_literacy": 82.4},
                "55-64": {"digital_literacy": 68.9},
                "65+": {"digital_literacy": 52.8}
            }
        }


# Legacy compatibility - keeping for backward compatibility
POLICIES = SampleDataProvider.get_policies()
INDICATORS_TIMELINE = SampleDataProvider.get_indicators_timeline()
