"""
Configuration settings for the Phoenix application.
"""
import os
from typing import Dict, Any, Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings loaded from environment variables."""
    
    # App settings
    APP_NAME = "Phoenix"
    APP_VERSION = "0.1.0"
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    
    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///phoenix.db")
    
    # Google Cloud settings
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    BQ_DATASET_ID = os.getenv("BQ_DATASET_ID", "budget_data")
    
    # API settings
    API_PREFIX = "/api/v1"
    
    @classmethod
    def as_dict(cls) -> Dict[str, Any]:
        """Return settings as a dictionary."""
        return {k: v for k, v in cls.__dict__.items() 
                if not k.startswith('_') and k.isupper()}


# Instantiate settings for easy import
settings = Settings()