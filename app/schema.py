from pydantic import BaseModel,Field
from typing import Optional

# =============================================================================
# ACTION: Update this schema to include the features your model needs for prediction.
# These are just some of the most important features from the Kaggle dataset.
# =============================================================================
class PredictionRequest(BaseModel):
    OverallQual: int      # Overall material and finish quality (1-10)
    GrLivArea: int        # Above grade (ground) living area square feet
    GarageCars: int       # Size of garage in car capacity
    TotalBsmtSF: int      # Total square feet of basement area
    YearBuilt: int        # Original construction date
    
    # Add any other features your model requires...
    # Example: FullBath: int, TotRmsAbvGrd: int, etc.


# FIXED: Renamed field to 'predicted_price' to match your main.py response
class PredictionResponse(BaseModel):
    predicted_price: float


# FIXED: Renamed class to 'UserCreate' (PascalCase)
class UserCreate(BaseModel):
    username: str
    password: str = Field(..., min_length=8, max_length=72)


# FIXED: Renamed class to 'Token' (PascalCase)
class Token(BaseModel):
    access_token: str
    token_type: str


# This schema is used internally for decoding the JWT
class TokenData(BaseModel):
    username: Optional[str] = None