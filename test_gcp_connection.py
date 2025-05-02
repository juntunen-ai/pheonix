import os
from google.cloud import bigquery

def test_connection():
    # Get credentials from environment variable
    project_id = os.environ.get("GCP_PROJECT_ID")
    
    # Initialize client
    client = bigquery.Client(project=project_id)
    
    # Run a simple query
    query = "SELECT 1 as test"
    query_job = client.query(query)
    results = query_job.result()
    
    # Print results
    for row in results:
        print(f"Test query result: {row.test}")
    
    print("Connection successful!")

if __name__ == "__main__":
    test_connection()