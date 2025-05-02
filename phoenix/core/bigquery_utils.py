"""
BigQuery utility functions for the Phoenix application.
"""
from typing import Any, Dict, List, Optional, Union

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

class BigQueryClient:
    """A wrapper around the Google BigQuery client with helper methods."""
    
    def __init__(self, credentials_path: Optional[str] = None, project_id: Optional[str] = None):
        """
        Initialize the BigQuery client.
        
        Args:
            credentials_path: Path to the service account credentials JSON file.
                If None, uses application default credentials.
            project_id: Google Cloud project ID. If None, uses the project from credentials.
        """
        if credentials_path:
            credentials = service_account.Credentials.from_service_account_file(
                credentials_path
            )
            self.client = bigquery.Client(
                credentials=credentials,
                project=project_id or credentials.project_id,
            )
        else:
            self.client = bigquery.Client(project=project_id)
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """
        Execute a BigQuery SQL query and return results as a pandas DataFrame.
        
        Args:
            query: SQL query string to execute
            
        Returns:
            DataFrame containing query results
        """
        return self.client.query(query).to_dataframe()
    
    def get_budget_data(self, 
                        start_date: str, 
                        end_date: str, 
                        categories: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Fetch budget data for the specified time period and categories.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            categories: Optional list of category names to filter by
            
        Returns:
            DataFrame with budget data
        """
        query = f"""
        SELECT 
            transaction_date, 
            amount, 
            category, 
            description
        FROM 
            `your_dataset.transactions`
        WHERE 
            transaction_date BETWEEN '{start_date}' AND '{end_date}'
        """
        
        if categories:
            categories_str = "', '".join(categories)
            query += f" AND category IN ('{categories_str}')"
            
        return self.execute_query(query)
    
    def save_to_bigquery(self, 
                         df: pd.DataFrame, 
                         table_id: str, 
                         write_disposition: str = "WRITE_APPEND") -> None:
        """
        Save a DataFrame to a BigQuery table.
        
        Args:
            df: DataFrame to save
            table_id: Fully qualified table ID (project.dataset.table)
            write_disposition: How to handle existing data (WRITE_APPEND, WRITE_TRUNCATE, WRITE_EMPTY)
        """
        job_config = bigquery.LoadJobConfig(
            write_disposition=write_disposition,
        )
        
        job = self.client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )
        job.result()  # Wait for the job to complete