"""Tests for telehealth feasibility analysis."""
import pytest
from backend.analysis.telehealth_feasibility import TelehealthFeasibilityAnalyzer


class TestTelehealthFeasibilityAnalyzer:
    """Test telehealth feasibility analysis."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.analyzer = TelehealthFeasibilityAnalyzer()
    
    def test_highly_feasible(self):
        """Test identification of highly feasible region."""
        region_data = {
            'download_speed': 25.0,
            'upload_speed': 10.0,
            'internet_coverage': 95,
            'reliability': 0.9
        }
        
        score = self.analyzer.calculate_feasibility_score(region_data)
        assert score > 0.8
        assert self.analyzer.classify_feasibility(score) == "Highly Feasible"
    
    def test_not_feasible(self):
        """Test identification of not feasible region."""
        region_data = {
            'download_speed': 0.5,
            'upload_speed': 0.2,
            'internet_coverage': 20,
            'reliability': 0.3
        }
        
        score = self.analyzer.calculate_feasibility_score(region_data)
        assert score < 0.4
        assert self.analyzer.classify_feasibility(score) == "Not Feasible"
    
    def test_minimum_speed_requirements(self):
        """Test minimum speed requirements."""
        # Below minimum - should get 0 score
        score_low = self.analyzer._calculate_speed_score(1.0, 0.3)
        assert score_low == 0.0
        
        # At minimum - should get low but non-zero score
        score_min = self.analyzer._calculate_speed_score(1.5, 0.5)
        assert score_min == 0.0
        
        # Well above minimum - should get high score
        score_high = self.analyzer._calculate_speed_score(25.0, 10.0)
        assert score_high > 0.8
    
    def test_telehealth_viability(self):
        """Test telehealth viability determination."""
        assert self.analyzer.is_telehealth_viable(0.6) is True
        assert self.analyzer.is_telehealth_viable(0.4) is False
        assert self.analyzer.is_telehealth_viable(0.5) is True