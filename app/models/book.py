from pydantic import BaseModel, Field
from typing import Annotated

class Book(BaseModel):
    id: int
    title: str
    author: str
    # review: int | None = None
    review: Annotated[int | None, Field(ge=1, le=5)] = None  # Assicurarsi che il valore sia compreso tra 1 e 5 e il valore di default è 1