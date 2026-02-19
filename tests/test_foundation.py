from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_test_llm():
    response = client.post("/test-llm", json={"input": "Sample input for LLM"})
    assert response.status_code == 200
    assert "output" in response.json()

def test_test_embedding():
    response = client.post("/test-embedding", json={"input": "Sample input for embedding"})
    assert response.status_code == 200
    assert "embedding" in response.json()