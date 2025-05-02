from fastapi import FastAPI

app = FastAPI(
    title="Phoenix Financial Analysis API",
    description="LangGraph AI application for financial data analysis",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}