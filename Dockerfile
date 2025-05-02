FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY pyproject.toml .

# Install build dependencies and project
RUN pip install --no-cache-dir build && \
    pip install --no-cache-dir .

# Copy application code
COPY phoenix/ ./phoenix/

# Set environment variables
ENV ENVIRONMENT="production"
ENV GCP_PROJECT_ID="pheonix-project-20250502"
ENV BQ_DATASET_ID="budget_data"

# Run the application
CMD ["python", "-m", "phoenix.main"]