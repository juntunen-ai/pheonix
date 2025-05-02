from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class FinancialQuery(BaseModel):
    """User query about financial data."""
    original_text: str
    intent: Optional[str] = None
    entities: Optional[Dict[str, Any]] = Field(default_factory=dict)

class FinancialState(BaseModel):
    """The state of the financial analysis workflow."""
    query: FinancialQuery
    # More state will be added here