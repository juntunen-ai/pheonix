from google.cloud import bigquery
import pandas as pd
from typing import Optional

class BigQueryClient:
    """Client for interacting with BigQuery for government budget data."""
    
    def __init__(self, project_id: Optional[str] = None):
        self.project_id = project_id
        self.client = bigquery.Client(project=project_id)
        
    def execute_query(self, query: str) -> pd.DataFrame:
        """Execute a query against BigQuery and return results as DataFrame."""
        try:
            return self.client.query(query).to_dataframe()
        except Exception as e:
            print(f"Error executing query: {e}")
            raise