from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    msg: str = Field(..., description="Error mesage.")
