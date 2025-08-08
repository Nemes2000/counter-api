from pydantic import BaseModel, Field


class CounterBody(BaseModel):
    value: int = Field(..., description="Value for the counter")
