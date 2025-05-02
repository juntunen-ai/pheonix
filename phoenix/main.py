import os
from google.cloud import bigquery

def main():
    """Simple main function to test deployment."""
    project_id = os.environ.get("GCP_PROJECT_ID")
    dataset_id = os.environ.get("BQ_DATASET_ID")
    
    print(f"Starting Phoenix application...")
    print(f"Project ID: {project_id}")
    print(f"Dataset ID: {dataset_id}")
    
    try:
        # Initialize BigQuery client with built-in authentication
        client = bigquery.Client(project=project_id)
        
        # Run a simple query
        query = "SELECT 1 as test"
        results = client.query(query).result()
        
        for row in results:
            print(f"BigQuery test query result: {row.test}")
        
        print("BigQuery connection successful!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()