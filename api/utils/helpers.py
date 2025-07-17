# API utility functions
import json
import pandas as pd
from datetime import datetime, timedelta
import os

def format_date(date_string):
    """Format date string for consistent display"""
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%B %d, %Y")
    except:
        return date_string

def calculate_effectiveness_score(metrics):
    """Calculate effectiveness score based on metrics"""
    # This is a simplified calculation
    # In a real application, this would use more sophisticated algorithms
    
    total_score = 0
    metric_count = 0
    
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            # Normalize different types of metrics
            if 'percentage' in key.lower() or 'rate' in key.lower():
                normalized_value = min(value / 10, 10)  # Cap at 10
            elif 'millions' in key.lower() or 'thousands' in key.lower():
                normalized_value = min(value / 1000, 10)  # Scale down large numbers
            else:
                normalized_value = min(value / 10, 10)
            
            total_score += normalized_value
            metric_count += 1
    
    return round(total_score / metric_count if metric_count > 0 else 0, 1)

def validate_policy_data(policy_data):
    """Validate policy data structure"""
    required_fields = ['id', 'name', 'description', 'implementation_date', 'status']
    
    for field in required_fields:
        if field not in policy_data:
            return False, f"Missing required field: {field}"
    
    # Validate date format
    try:
        datetime.fromisoformat(policy_data['implementation_date'])
    except:
        return False, "Invalid implementation_date format. Use YYYY-MM-DD"
    
    # Validate status
    valid_statuses = ['active', 'inactive', 'in_progress', 'planned']
    if policy_data['status'] not in valid_statuses:
        return False, f"Invalid status. Must be one of: {valid_statuses}"
    
    return True, "Valid"

def export_to_csv(data, filename):
    """Export data to CSV file"""
    try:
        df = pd.DataFrame(data)
        filepath = os.path.join('data', 'exports', filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        return True, filepath
    except Exception as e:
        return False, str(e)

def calculate_trend(data_points, metric_key):
    """Calculate trend for a specific metric over time"""
    if len(data_points) < 2:
        return None
    
    # Sort by date
    sorted_data = sorted(data_points, key=lambda x: x['date'])
    
    values = [point[metric_key] for point in sorted_data if metric_key in point]
    
    if len(values) < 2:
        return None
    
    # Simple linear trend calculation
    first_value = values[0]
    last_value = values[-1]
    
    absolute_change = last_value - first_value
    percentage_change = (absolute_change / first_value) * 100 if first_value != 0 else 0
    
    return {
        'start_value': first_value,
        'end_value': last_value,
        'absolute_change': round(absolute_change, 2),
        'percentage_change': round(percentage_change, 2),
        'trend_direction': 'increasing' if absolute_change > 0 else 'decreasing' if absolute_change < 0 else 'stable'
    }

def generate_policy_summary(policy):
    """Generate a summary description for a policy"""
    summary = f"The {policy['name']} was implemented on {format_date(policy['implementation_date'])} "
    summary += f"and is currently {policy['status']}. "
    
    if 'effectiveness_score' in policy:
        effectiveness = policy['effectiveness_score']
        if effectiveness >= 8:
            summary += "It has shown excellent effectiveness "
        elif effectiveness >= 6:
            summary += "It has shown good effectiveness "
        else:
            summary += "It has shown moderate effectiveness "
        
        summary += f"with a score of {effectiveness}/10."
    
    return summary

def search_policies(policies, query):
    """Search policies by name, description, or other fields"""
    query_lower = query.lower()
    results = []
    
    for policy in policies:
        # Search in name and description
        if (query_lower in policy.get('name', '').lower() or 
            query_lower in policy.get('description', '').lower()):
            results.append(policy)
            continue
        
        # Search in target demographics
        if 'target_demographics' in policy:
            for demographic in policy['target_demographics']:
                if query_lower in demographic.lower():
                    results.append(policy)
                    break
        
        # Search in key provisions
        if 'key_provisions' in policy:
            for provision in policy['key_provisions']:
                if query_lower in provision.lower():
                    results.append(policy)
                    break
    
    return results
