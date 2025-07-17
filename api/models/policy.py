"""
Policy data model.

Defines the structure and validation for policy entities in the system.
"""

from typing import Dict, Any, Optional
from datetime import datetime


class Policy:
    """
    Policy entity model for digital divide policies.
    
    Represents a government policy with its metadata, metrics, and effectiveness data.
    """
    
    VALID_STATUSES = ['active', 'inactive', 'in_progress', 'planned', 'cancelled']
    
    def __init__(self, policy_id: int, name: str, description: str, 
                 implementation_date: str, effectiveness_score: float, 
                 metrics: Dict[str, Any], status: str):
        """
        Initialize a Policy instance.
        
        Args:
            policy_id: Unique identifier for the policy
            name: Policy name
            description: Detailed policy description
            implementation_date: Date when policy was implemented (YYYY-MM-DD)
            effectiveness_score: Numerical score rating policy effectiveness (0-10)
            metrics: Dictionary containing policy performance metrics
            status: Current policy status
            
        Raises:
            ValueError: If any parameters are invalid
        """
        self._validate_inputs(policy_id, name, description, implementation_date, 
                            effectiveness_score, status)
        
        self.id = policy_id
        self.name = name
        self.description = description
        self.implementation_date = implementation_date
        self.effectiveness_score = effectiveness_score
        self.metrics = metrics or {}
        self.status = status
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert policy object to dictionary representation.
        
        Returns:
            Dictionary containing all policy data
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'implementation_date': self.implementation_date,
            'effectiveness_score': self.effectiveness_score,
            'metrics': self.metrics,
            'status': self.status,
            'created_at': self.created_at
        }
    
    def to_summary(self) -> Dict[str, Any]:
        """
        Convert policy to summary representation for lists.
        
        Returns:
            Dictionary containing essential policy information
        """
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'effectiveness_score': self.effectiveness_score,
            'implementation_date': self.implementation_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Policy':
        """
        Create Policy instance from dictionary data.
        
        Args:
            data: Dictionary containing policy data
            
        Returns:
            Policy instance
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        required_fields = ['id', 'name', 'description', 'implementation_date', 'status']
        
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        return cls(
            policy_id=data['id'],
            name=data['name'],
            description=data['description'],
            implementation_date=data['implementation_date'],
            effectiveness_score=data.get('effectiveness_score', 0.0),
            metrics=data.get('metrics', {}),
            status=data['status']
        )
    
    def update_effectiveness_score(self, new_score: float) -> None:
        """
        Update the policy's effectiveness score.
        
        Args:
            new_score: New effectiveness score (0-10)
            
        Raises:
            ValueError: If score is not within valid range
        """
        if not isinstance(new_score, (int, float)) or not (0 <= new_score <= 10):
            raise ValueError("Effectiveness score must be a number between 0 and 10")
        
        self.effectiveness_score = float(new_score)
    
    def update_status(self, new_status: str) -> None:
        """
        Update the policy's status.
        
        Args:
            new_status: New policy status
            
        Raises:
            ValueError: If status is not valid
        """
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(self.VALID_STATUSES)}")
        
        self.status = new_status
    
    def add_metric(self, key: str, value: Any) -> None:
        """
        Add or update a policy metric.
        
        Args:
            key: Metric name
            value: Metric value
        """
        if not isinstance(key, str) or not key.strip():
            raise ValueError("Metric key must be a non-empty string")
        
        self.metrics[key] = value
    
    def get_metric(self, key: str, default: Any = None) -> Any:
        """
        Get a specific policy metric.
        
        Args:
            key: Metric name
            default: Default value if metric doesn't exist
            
        Returns:
            Metric value or default
        """
        return self.metrics.get(key, default)
    
    def is_active(self) -> bool:
        """
        Check if policy is currently active.
        
        Returns:
            True if policy status is 'active'
        """
        return self.status == 'active'
    
    def get_implementation_year(self) -> int:
        """
        Get the year the policy was implemented.
        
        Returns:
            Implementation year as integer
        """
        return int(self.implementation_date.split('-')[0])
    
    def calculate_age_in_years(self) -> float:
        """
        Calculate how many years since policy implementation.
        
        Returns:
            Years since implementation as float
        """
        impl_date = datetime.fromisoformat(self.implementation_date)
        current_date = datetime.now()
        age_days = (current_date - impl_date).days
        return round(age_days / 365.25, 2)
    
    @staticmethod
    def _validate_inputs(policy_id: int, name: str, description: str, 
                        implementation_date: str, effectiveness_score: float, 
                        status: str) -> None:
        """
        Validate input parameters for policy creation.
        
        Args:
            policy_id: Policy ID to validate
            name: Policy name to validate
            description: Policy description to validate
            implementation_date: Implementation date to validate
            effectiveness_score: Effectiveness score to validate
            status: Status to validate
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if not isinstance(policy_id, int) or policy_id <= 0:
            raise ValueError("Policy ID must be a positive integer")
        
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Policy name must be a non-empty string")
        
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Policy description must be a non-empty string")
        
        if not isinstance(implementation_date, str):
            raise ValueError("Implementation date must be a string")
        
        # Validate date format
        try:
            datetime.fromisoformat(implementation_date)
        except ValueError:
            raise ValueError("Implementation date must be in YYYY-MM-DD format")
        
        if not isinstance(effectiveness_score, (int, float)) or not (0 <= effectiveness_score <= 10):
            raise ValueError("Effectiveness score must be a number between 0 and 10")
        
        if status not in Policy.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(Policy.VALID_STATUSES)}")
    
    def __str__(self) -> str:
        """String representation of the policy."""
        return f"Policy(id={self.id}, name='{self.name}', status='{self.status}')"
    
    def __repr__(self) -> str:
        """Detailed string representation of the policy."""
        return (f"Policy(id={self.id}, name='{self.name}', "
                f"effectiveness_score={self.effectiveness_score}, status='{self.status}')")
