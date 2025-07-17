"""
Data analytics service module.

Handles digital divide indicators, trends analysis, and statistical calculations.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import statistics


class DataAnalyticsService:
    """Service class for managing digital divide data and analytics."""
    
    def __init__(self):
        """Initialize with sample digital divide indicators data."""
        self._indicators = {
            "broadband_access": [
                {"date": "2020-01-01", "percentage": 73.2, "rural": 63.1, "urban": 82.5},
                {"date": "2020-06-01", "percentage": 74.1, "rural": 64.8, "urban": 83.2},
                {"date": "2021-01-01", "percentage": 75.8, "rural": 67.2, "urban": 84.1},
                {"date": "2021-06-01", "percentage": 78.5, "rural": 71.4, "urban": 85.8},
                {"date": "2022-01-01", "percentage": 81.2, "rural": 75.6, "urban": 87.3},
                {"date": "2022-06-01", "percentage": 83.8, "rural": 78.9, "urban": 88.9},
                {"date": "2023-01-01", "percentage": 86.1, "rural": 82.1, "urban": 90.2},
                {"date": "2023-06-01", "percentage": 87.9, "rural": 84.7, "urban": 91.4}
            ],
            "digital_literacy": [
                {"date": "2020-01-01", "percentage": 58.3, "age_18_34": 78.5, "age_35_54": 62.1, "age_55_plus": 38.7},
                {"date": "2020-06-01", "percentage": 59.1, "age_18_34": 79.2, "age_35_54": 63.4, "age_55_plus": 39.8},
                {"date": "2021-01-01", "percentage": 61.5, "age_18_34": 81.3, "age_35_54": 66.2, "age_55_plus": 42.1},
                {"date": "2021-06-01", "percentage": 64.8, "age_18_34": 83.7, "age_35_54": 69.8, "age_55_plus": 45.9},
                {"date": "2022-01-01", "percentage": 68.2, "age_18_34": 85.9, "age_35_54": 73.4, "age_55_plus": 49.8},
                {"date": "2022-06-01", "percentage": 71.5, "age_18_34": 87.8, "age_35_54": 76.9, "age_55_plus": 53.7},
                {"date": "2023-01-01", "percentage": 74.1, "age_18_34": 89.2, "age_35_54": 79.8, "age_55_plus": 57.2},
                {"date": "2023-06-01", "percentage": 76.8, "age_18_34": 90.7, "age_35_54": 82.4, "age_55_plus": 60.9}
            ],
            "device_ownership": [
                {"date": "2020-01-01", "smartphone": 81.2, "computer": 69.4, "tablet": 45.8},
                {"date": "2020-06-01", "smartphone": 82.1, "computer": 70.8, "tablet": 47.2},
                {"date": "2021-01-01", "smartphone": 84.3, "computer": 73.5, "tablet": 49.7},
                {"date": "2021-06-01", "smartphone": 86.7, "computer": 76.9, "tablet": 52.8},
                {"date": "2022-01-01", "smartphone": 88.9, "computer": 80.1, "tablet": 56.2},
                {"date": "2022-06-01", "smartphone": 90.8, "computer": 82.7, "tablet": 59.4},
                {"date": "2023-01-01", "smartphone": 92.1, "computer": 85.3, "tablet": 62.8},
                {"date": "2023-06-01", "smartphone": 93.5, "computer": 87.6, "tablet": 65.9}
            ]
        }
    
    def get_indicators_data(self, indicator_type: Optional[str] = None,
                           start_date: Optional[str] = None,
                           end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Retrieve digital divide indicators data.
        
        Args:
            indicator_type: Specific indicator type to retrieve
            start_date: Filter from this date (YYYY-MM-DD)
            end_date: Filter to this date (YYYY-MM-DD)
            
        Returns:
            Dictionary containing filtered indicator data
        """
        return self.get_indicators(indicator_type, start_date, end_date)

    def get_indicators(self, indicator_type: Optional[str] = None,
                      start_date: Optional[str] = None,
                      end_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Retrieve digital divide indicators with optional filtering.
        
        Args:
            indicator_type: Specific indicator type to retrieve
            start_date: Filter from this date (YYYY-MM-DD)
            end_date: Filter to this date (YYYY-MM-DD)
            
        Returns:
            Dictionary containing filtered indicator data
        """
        if indicator_type and indicator_type in self._indicators:
            data = self._indicators[indicator_type]
        else:
            data = self._indicators
        
        # Apply date filtering if specified
        if start_date or end_date:
            data = self._filter_by_date_range(data, start_date, end_date)
        
        total_points = (len(data) if indicator_type 
                       else sum(len(v) for v in data.values()))
        
        return {
            'indicators': data,
            'type': indicator_type or 'all',
            'total_points': total_points,
            'date_range': {
                'start': start_date,
                'end': end_date
            }
        }
    
    def calculate_trends(self, start_year: Optional[str] = None, 
                        end_year: Optional[str] = None) -> Dict[str, Any]:
        """
        Calculate trend analysis for all digital divide indicators.
        
        Args:
            start_year: Starting year for analysis
            end_year: Ending year for analysis
        
        Returns:
            Dictionary containing trend data for each indicator
        """
        trends = {}
        
        for indicator_name, data_points in self._indicators.items():
            if len(data_points) >= 2:
                trend = self._calculate_metric_trend(data_points, 'percentage')
                if trend:
                    trends[indicator_name] = trend
        
        return {
            'trends': trends,
            'period': f'{start_year or "2020"}-{end_year or "2023"}',
            'calculation_method': 'linear_change'
        }
    
    def get_correlation_analysis(self) -> Dict[str, Any]:
        """
        Generate correlation analysis between policies and indicators.
        
        Returns:
            Dictionary containing correlation coefficients
        """
        correlations = {
            "Digital Equity Act": {
                "broadband_access": 0.78,
                "digital_literacy": 0.65,
                "device_ownership": 0.42
            },
            "Affordable Connectivity Program": {
                "broadband_access": 0.85,
                "digital_literacy": 0.71,
                "device_ownership": 0.58
            },
            "Rural Digital Opportunity Fund": {
                "broadband_access": 0.92,
                "digital_literacy": 0.48,
                "device_ownership": 0.33
            }
        }
        
        return {
            'correlations': correlations,
            'methodology': 'Pearson correlation coefficient',
            'confidence_level': 0.95,
            'note': 'Simulated data for demonstration purposes'
        }
    
    def get_demographics_breakdown(self) -> Dict[str, Any]:
        """
        Get demographic breakdown of digital divide data.
        
        Returns:
            Dictionary containing demographic analysis
        """
        demographics = {
            "income_levels": {
                "low_income": {"broadband_access": 62.4, "digital_literacy": 48.7},
                "middle_income": {"broadband_access": 83.2, "digital_literacy": 71.5},
                "high_income": {"broadband_access": 94.8, "digital_literacy": 89.3}
            },
            "geographic": {
                "urban": {"broadband_access": 91.4, "digital_literacy": 82.4},
                "suburban": {"broadband_access": 87.9, "digital_literacy": 76.8},
                "rural": {"broadband_access": 84.7, "digital_literacy": 60.9}
            },
            "age_groups": {
                "18_34": {"digital_literacy": 90.7, "device_ownership": 95.2},
                "35_54": {"digital_literacy": 82.4, "device_ownership": 91.8},
                "55_plus": {"digital_literacy": 60.9, "device_ownership": 78.3}
            }
        }
        
        return {
            'demographics': demographics,
            'data_source': 'National Digital Inclusion Survey 2023',
            'methodology': 'Representative sampling across all demographics'
        }
    
    def _filter_by_date_range(self, data: Any, start_date: Optional[str], 
                             end_date: Optional[str]) -> Any:
        """
        Filter data by date range.
        
        Args:
            data: Data to filter (can be dict or list)
            start_date: Start date string
            end_date: End date string
            
        Returns:
            Filtered data in same format as input
        """
        if isinstance(data, dict):
            filtered_data = {}
            for key, points in data.items():
                filtered_data[key] = self._filter_points_by_date(
                    points, start_date, end_date
                )
            return filtered_data
        else:
            return self._filter_points_by_date(data, start_date, end_date)
    
    def _filter_points_by_date(self, points: List[Dict], start_date: Optional[str],
                              end_date: Optional[str]) -> List[Dict]:
        """
        Filter list of data points by date range.
        
        Args:
            points: List of data points with 'date' field
            start_date: Start date string
            end_date: End date string
            
        Returns:
            Filtered list of data points
        """
        filtered_points = []
        
        for point in points:
            point_date = datetime.fromisoformat(point['date'])
            
            # Check start date
            if start_date:
                start_dt = datetime.fromisoformat(start_date)
                if point_date < start_dt:
                    continue
            
            # Check end date
            if end_date:
                end_dt = datetime.fromisoformat(end_date)
                if point_date > end_dt:
                    continue
            
            filtered_points.append(point)
        
        return filtered_points
    
    def _calculate_metric_trend(self, data_points: List[Dict],
                               metric_key: str) -> Optional[Dict]:
        """
        Calculate trend for a specific metric over time.
        
        Args:
            data_points: List of data points
            metric_key: Key of the metric to analyze
            
        Returns:
            Dictionary containing trend analysis or None
        """
        if len(data_points) < 2:
            return None
        
        # Sort by date and extract values
        sorted_data = sorted(data_points, key=lambda x: x['date'])
        values = [point[metric_key] for point in sorted_data if metric_key in point]
        
        if len(values) < 2:
            return None
        
        first_value = values[0]
        last_value = values[-1]
        
        absolute_change = last_value - first_value
        percentage_change = (absolute_change / first_value) * 100 if first_value != 0 else 0
        
        return {
            'start_value': round(first_value, 2),
            'end_value': round(last_value, 2),
            'absolute_change': round(absolute_change, 2),
            'percentage_change': round(percentage_change, 2),
            'trend_direction': self._get_trend_direction(absolute_change),
            'volatility': round(statistics.stdev(values), 2) if len(values) > 1 else 0
        }
    
    def _get_trend_direction(self, change: float) -> str:
        """
        Determine trend direction based on change value.
        
        Args:
            change: Absolute change value
            
        Returns:
            Trend direction string
        """
        if change > 0.5:
            return 'increasing'
        elif change < -0.5:
            return 'decreasing'
        else:
            return 'stable'


# Global service instance
data_service = DataAnalyticsService()
