"""Telehealth feasibility analysis."""
from typing import Dict
from backend.config.settings import (
    MIN_DOWNLOAD_SPEED_MBPS,
    MIN_UPLOAD_SPEED_MBPS
)


class TelehealthFeasibilityAnalyzer:
    """Analyze regions for telehealth feasibility."""
    
    def __init__(self):
        """Initialize analyzer."""
        self.min_download = MIN_DOWNLOAD_SPEED_MBPS
        self.min_upload = MIN_UPLOAD_SPEED_MBPS
    
    def calculate_feasibility_score(self, region_data: Dict) -> float:
        """
        Calculate telehealth feasibility score.
        
        Score ranges from 0 (not feasible) to 1 (highly feasible).
        
        Args:
            region_data: Dictionary containing:
                - download_speed: Average download speed (Mbps)
                - upload_speed: Average upload speed (Mbps)
                - internet_coverage: Percentage with internet access (0-100)
                - reliability: Connection reliability score (0-1)
        
        Returns:
            Feasibility score (0-1)
        """
        # Speed score
        speed_score = self._calculate_speed_score(
            region_data.get('download_speed', 0),
            region_data.get('upload_speed', 0)
        )
        
        # Coverage score
        coverage_score = region_data.get('internet_coverage', 0) / 100.0
        
        # Reliability score
        reliability_score = region_data.get('reliability', 0)
        
        # Weighted average (speed is most important)
        total_score = (
            speed_score * 0.5 +
            coverage_score * 0.3 +
            reliability_score * 0.2
        )
        
        return min(max(total_score, 0.0), 1.0)
    
    def _calculate_speed_score(self, download: float, upload: float) -> float:
        """Calculate score based on internet speed."""
        # Check if meets minimum requirements
        if download < self.min_download or upload < self.min_upload:
            return 0.0
        
        # Normalize: 1.5-25 Mbps download range
        # Higher speeds get better scores
        download_score = min((download - self.min_download) / 23.5, 1.0)
        upload_score = min((upload - self.min_upload) / 9.5, 1.0)
        
        return (download_score + upload_score) / 2
    
    def is_telehealth_viable(self, feasibility_score: float) -> bool:
        """
        Determine if telehealth is viable.
        
        Args:
            feasibility_score: Score from 0-1
            
        Returns:
            True if viable, False otherwise
        """
        return feasibility_score >= 0.5
    
    def classify_feasibility(self, feasibility_score: float) -> str:
        """
        Classify telehealth feasibility.
        
        Args:
            feasibility_score: Score from 0-1
            
        Returns:
            Classification string
        """
        if feasibility_score >= 0.8:
            return "Highly Feasible"
        elif feasibility_score >= 0.6:
            return "Feasible"
        elif feasibility_score >= 0.4:
            return "Marginally Feasible"
        else:
            return "Not Feasible"