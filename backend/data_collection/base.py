"""Base class for data collectors."""
from abc import ABC, abstractmethod
from typing import Dict, List
import requests
from datetime import datetime


class DataCollector(ABC):
    """Abstract base class for all data collectors."""
    
    def __init__(self):
        """Initialize data collector."""
        self.session = requests.Session()
        self.last_updated = None
    
    @abstractmethod
    def collect(self) -> List[Dict]:
        """
        Collect data from source.
        
        Returns:
            List of dictionaries containing collected data
        """
        pass
    
    @abstractmethod
    def validate(self, data: Dict) -> bool:
        """
        Validate collected data.
        
        Args:
            data: Data dictionary to validate
            
        Returns:
            True if valid, False otherwise
        """
        pass
    
    def fetch_url(self, url: str, params: Dict = None) -> Dict:
        """
        Fetch data from URL.
        
        Args:
            url: URL to fetch
            params: Query parameters
            
        Returns:
            JSON response as dictionary
        """
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return {}
    
    def update_timestamp(self):
        """Update last updated timestamp."""
        self.last_updated = datetime.utcnow()