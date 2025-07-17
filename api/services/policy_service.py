"""
Policy data service module.

Handles all policy data operations including filtering, searching, and calculations.
In a production environment, this would interface with a database.
"""

from typing import List, Dict, Optional
from datetime import datetime


class PolicyDataService:
    """Service class for managing policy data operations."""
    
    def __init__(self):
        """Initialize with sample data."""
        self._policies = [
            {
                "id": 1,
                "name": "Digital Equity Act",
                "description": "Federal legislation aimed at ensuring equitable access to digital technologies",
                "implementation_date": "2021-11-15",
                "effectiveness_score": 7.5,
                "metrics": {
                    "broadband_access_increase": 15.2,
                    "digital_literacy_improvement": 12.8,
                    "rural_connectivity_boost": 22.1
                },
                "status": "active"
            },
            {
                "id": 2,
                "name": "Affordable Connectivity Program",
                "description": "Program providing discounted internet service to eligible households",
                "implementation_date": "2021-12-31",
                "effectiveness_score": 8.2,
                "metrics": {
                    "households_served": 14500000,
                    "cost_reduction_percentage": 45.0,
                    "rural_participation_rate": 68.3
                },
                "status": "active"
            },
            {
                "id": 3,
                "name": "Rural Digital Opportunity Fund",
                "description": "FCC program to bring broadband to underserved rural areas",
                "implementation_date": "2020-10-29",
                "effectiveness_score": 6.8,
                "metrics": {
                    "areas_covered": 5200000,
                    "speed_improvement": 85.7,
                    "completion_rate": 42.1
                },
                "status": "in_progress"
            }
        ]
    
    def get_all_policies(self, status: Optional[str] = None, 
                        year: Optional[str] = None) -> List[Dict]:
        """
        Retrieve all policies with optional filtering.
        
        Args:
            status: Filter by policy status
            year: Filter by implementation year
            
        Returns:
            List of policy dictionaries
        """
        policies = self._policies.copy()
        
        if status:
            policies = [p for p in policies if p['status'] == status]
        
        if year:
            policies = [p for p in policies 
                       if p['implementation_date'].startswith(year)]
        
        return policies
    
    def get_policy_by_id(self, policy_id: int) -> Optional[Dict]:
        """
        Retrieve a specific policy by ID.
        
        Args:
            policy_id: The policy identifier
            
        Returns:
            Policy dictionary or None if not found
        """
        return next((p for p in self._policies if p['id'] == policy_id), None)
    
    def search_policies(self, query: str) -> List[Dict]:
        """
        Search policies by name or description.
        
        Args:
            query: Search term
            
        Returns:
            List of matching policy dictionaries
        """
        query_lower = query.lower()
        results = []
        
        for policy in self._policies:
            if (query_lower in policy['name'].lower() or 
                query_lower in policy['description'].lower()):
                results.append(policy)
        
        return results
    
    def get_effectiveness_data(self) -> Dict:
        """
        Calculate effectiveness metrics for all policies.
        
        Returns:
            Dictionary containing effectiveness data and statistics
        """
        effectiveness_data = [
            {
                "id": policy["id"],
                "name": policy["name"],
                "effectiveness_score": policy["effectiveness_score"],
                "implementation_date": policy["implementation_date"],
                "metrics": policy["metrics"]
            }
            for policy in self._policies
        ]
        
        avg_effectiveness = (
            sum(p["effectiveness_score"] for p in self._policies) / 
            len(self._policies)
        )
        
        return {
            "effectiveness_data": effectiveness_data,
            "average_effectiveness": round(avg_effectiveness, 2),
            "total_policies": len(self._policies)
        }
    
    def get_timeline_data(self) -> Dict:
        """
        Get policy timeline data sorted by implementation date.
        
        Returns:
            Dictionary containing timeline data
        """
        timeline_data = [
            {
                "policy_id": policy["id"],
                "policy_name": policy["name"],
                "implementation_date": policy["implementation_date"],
                "effectiveness_score": policy["effectiveness_score"],
                "status": policy["status"]
            }
            for policy in self._policies
        ]
        
        timeline_data.sort(key=lambda x: x["implementation_date"])
        
        return {
            "timeline": timeline_data,
            "total_policies": len(timeline_data)
        }


# Global service instance
policy_service = PolicyDataService()
