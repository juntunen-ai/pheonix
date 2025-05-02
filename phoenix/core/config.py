import os
from pathlib import Path
from enum import Enum
from typing import Dict, Any
from dotenv import load_dotenv

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Define environment types
class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"

# Load environment variables from .env file if it exists
env_file = BASE_DIR / ".env"
if env_file.exists():
    load_dotenv(env_file)

class Settings:
    """Application settings with environment-specific configurations."""
    
    # Determine environment
    ENVIRONMENT = Environment(os.getenv("ENVIRONMENT", "development"))
    
    # App settings
    APP_NAME = "Phoenix"
    APP_VERSION = "0.1.0"
    DEBUG = ENVIRONMENT != Environment.PRODUCTION
    
    # Google Cloud settings
    # Fix for $(pwd) in environment variables
    _credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")
    if "$(pwd)" in _credentials_path:
        # Replace $(pwd) with the actual project directory
        GOOGLE_APPLICATION_CREDENTIALS = str(BASE_DIR / "phoenix-key.json")
    else:
        GOOGLE_APPLICATION_CREDENTIALS = _credentials_path
    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    BQ_DATASET_ID = os.getenv("BQ_DATASET_ID", "budget_data")
    
    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT == Environment.DEVELOPMENT
    
    @property
    def is_testing(self) -> bool:
        return self.ENVIRONMENT == Environment.TESTING
    
    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == Environment.PRODUCTION
    
    def get_bigquery_credentials(self):
        """Get the appropriate credentials based on environment."""
        if self.is_production:
            # In production, rely on built-in service accounts
            return None
        else:
            # In development/testing, use the credentials file
            return self.GOOGLE_APPLICATION_CREDENTIALS
    
    @classmethod
    def as_dict(cls) -> Dict[str, Any]:
        """Return settings as a dictionary."""
        return {k: v for k, v in cls.__dict__.items() 
                if not k.startswith('_') and k.isupper()}

# Create a singleton instance for easy importing
settings = Settings()