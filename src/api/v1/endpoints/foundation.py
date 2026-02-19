from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from orchestration.query_orchestrator import orchestrate_query
from response.formatter import format_response

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/test-llm")
async def test_llm():
    # Placeholder for testing LLM functionality
    return {"message": "LLM test endpoint"}

@router.get("/test-embedding")
async def test_embedding():
    # Placeholder for testing embedding functionality
    return {"message": "Embedding test endpoint"}

@router.post("/query")
async def query_endpoint(request: QueryRequest):
    try:
        result = orchestrate_query(request.question)
        return format_response(result["answer"], result["sql_used"], result["rows"])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))