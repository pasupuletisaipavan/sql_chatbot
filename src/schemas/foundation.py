from pydantic import BaseModel
from typing import List, Optional

class HealthResponse(BaseModel):
    status: str

class TestLLMResponse(BaseModel):
    result: str

class TestEmbeddingResponse(BaseModel):
    embeddings: List[float]

class QueryRequest(BaseModel):
    query: str
    parameters: Optional[dict] = None

class QueryResponse(BaseModel):
    result: str
    metadata: Optional[dict] = None