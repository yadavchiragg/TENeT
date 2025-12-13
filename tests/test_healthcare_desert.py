"""Tests for healthcare desert analysis."""
import pytest
from backend.analysis.healthcare_desert import HealthcareDesertAnalyzer


class TestHealthcareDesertAnalyzer:
    """Test healthcare desert analysis."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.analyzer = HealthcareDesertAnalyzer()
    
    def test_severe_desert(self):
        """Test identification of severe healthcare desert."""
        region_data = {
            'facility_count': 0,
            'population': 5000,
            'avg_distance': 75,
            'specialists': 0,
            'has_transportation': False
        }
        
        score = self.analyzer.calculate_desert_score(region_data)
        assert score > 0.7
        assert self.analyzer.classify_region(score) == "Severe Healthcare Desert"
    
    def test_adequate_access(self):
        """Test identification of adequate healthcare access."""
        region_data = {
            'facility_count': 5,
            'population': 5000,
            'avg_distance': 5,
            'specialists': 3,
            'has_transportation': True
        }
        
        score = self.analyzer.calculate_desert_score(region_data)
        assert score < 0.3
        assert self.analyzer.classify_region(score) == "Adequate Healthcare Access"
    
    def test_facility_score_calculation(self):
        """Test facility density score calculation."""
        # 0 facilities = high score (bad)
        score_zero = self.analyzer._calculate_facility_score(0, 1000)
        assert score_zero == 1.0
        
        # 1 facility per 1000 people = good score
        score_good = self.analyzer._calculate_facility_score(1, 1000)
        assert score_good == 0.0
    
    def test_distance_score_calculation(self):
        """Test distance score calculation."""
        # 0 miles = score 0 (good)
        assert self.analyzer._calculate_distance_score(0) == 0.0
        
        # 50 miles = score 1 (bad)
        assert self.analyzer._calculate_distance_score(50) >= 0.9
        
        # 25 miles = score 0.5
        assert 0.4 <= self.analyzer._calculate_distance_score(25) <= 0.6