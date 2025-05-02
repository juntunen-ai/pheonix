from phoenix.core.config import settings
from phoenix.core.bigquery_utils import BigQueryClient

def test_environment_setup():
    """Test that environment settings are properly loaded."""
    print(f"Environment: {settings.ENVIRONMENT}")
    print(f"Debug mode: {settings.DEBUG}")
    print(f"Using credentials from: {settings.GOOGLE_APPLICATION_CREDENTIALS}")
    print(f"Project ID: {settings.GCP_PROJECT_ID}")
    print(f"BigQuery Dataset: {settings.BQ_DATASET_ID}")
    
    # Test BigQuery connection
    try:
        client = BigQueryClient()
        result = client.execute_query("SELECT 1 as test")
        print("BigQuery connection successful!")
        print(f"Query result: {result}")
    except Exception as e:
        print(f"BigQuery connection error: {e}")

if __name__ == "__main__":
    test_environment_setup()