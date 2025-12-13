"""Healthcare desert identification and analysis."""
from typing import Dict, List


class HealthcareDesertAnalyzer:
    """Analyze regions to identify healthcare deserts."""
    
    def __init__(self):
        """Initialize analyzer with default weights."""
        self.weights = {
            'facility_density': 0.3,
            'distance_to_clinic': 0.3,
            'specialist_availability': 0.2,
            'transportation': 0.2
        }
    
    def calculate_desert_score(self, region_data: Dict) -> float:
        """
        Calculate healthcare desert score for a region.
        
        Score ranges from 0 (well-served) to 1 (severe desert).
        
        Args:
            region_data: Dictionary containing:
                - facility_count: Number of health facilities
                - population: Population count
                - avg_distance: Average distance to nearest clinic (miles)
                - specialists: Number of specialist providers
                - has_transportation: Boolean for public transport availability
        
        Returns:
            Desert score (0-1, higher = more severe desert)
        """
        # Facility density score (facilities per 1000 people)
        facility_score = self._calculate_facility_score(
            region_data.get('facility_count', 0),
            region_data.get('population', 1)
        )
        
        # Distance score
        distance_score = self._calculate_distance_score(
            region_data.get('avg_distance', 0)
        )
        
        # Specialist availability score
        specialist_score = self._calculate_specialist_score(
            region_data.get('specialists', 0),
            region_data.get('population', 1)
        )
        
        # Transportation score
        transport_score = 0.0 if region_data.get('has_transportation') else 1.0
        
        # Weighted average
        total_score = (
            facility_score * self.weights['facility_density'] +
            distance_score * self.weights['distance_to_clinic'] +
            specialist_score * self.weights['specialist_availability'] +
            transport_score * self.weights['transportation']
        )
        
        return min(max(total_score, 0.0), 1.0)
    
    def _calculate_facility_score(self, facilities: int, population: int) -> float:
        """Calculate score based on facility density."""
        if population == 0:
            return 1.0
        
        facilities_per_1000 = (facilities / population) * 1000
        
        # Normalize: 0.5+ facilities per 1000 = good (score 0)
        # 0 facilities = severe desert (score 1)
        return max(0, 1 - (facilities_per_1000 / 0.5))
    
    def _calculate_distance_score(self, avg_distance: float) -> float:
        """Calculate score based on distance to nearest clinic."""
        # Normalize: 0-50 miles range
        # 0 miles = score 0, 50+ miles = score 1
        return min(avg_distance / 50.0, 1.0)
    
    def _calculate_specialist_score(self, specialists: int, population: int) -> float:
        """Calculate score based on specialist availability."""
        if population == 0:
            return 1.0
        
        specialists_per_10000 = (specialists / population) * 10000
        
        # Normalize: 1+ specialists per 10000 = good
        return max(0, 1 - specialists_per_10000)
    
    def classify_region(self, desert_score: float) -> str:
        """
        Classify region based on desert score.
        
        Args:
            desert_score: Score from 0-1
            
        Returns:
            Classification string
        """
        if desert_score >= 0.7:
            return "Severe Healthcare Desert"
        elif desert_score >= 0.5:
            return "Moderate Healthcare Desert"
        elif desert_score >= 0.3:
            return "Limited Healthcare Access"
        else:
            return "Adequate Healthcare Access"