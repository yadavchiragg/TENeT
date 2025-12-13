"""Configuration settings for TENeT application."""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database
DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///tenet.db')

# API Keys (to be set via environment variables)
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
HEALTHSITES_API_KEY = os.environ.get('HEALTHSITES_API_KEY')

# Data sources
HEALTHSITES_API_URL = "https://healthsites.io/api/v2/"
BROADBAND_DATA_URL = "https://broadbandmap.fcc.gov/api/"

# Alaska specific configuration
ALASKA_BOUNDS = {
    'min_lat': 51.0,
    'max_lat': 72.0,
    'min_lon': -180.0,
    'max_lon': -130.0
}

# Telehealth requirements
MIN_DOWNLOAD_SPEED_MBPS = 1.5  # Minimum for video calls
MIN_UPLOAD_SPEED_MBPS = 0.5

# Healthcare desert thresholds
MAX_DISTANCE_TO_CLINIC_MILES = 50
MIN_FACILITIES_PER_1000_PEOPLE = 0.5