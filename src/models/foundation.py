from pydantic import BaseModel

class ExampleModel(BaseModel):
    id: int
    name: str
    description: str = None

# This file is currently a placeholder for future business logic and SQL generation.