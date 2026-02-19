import requests
from src.core.config import settings
import logging

class LLMClient:
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.logger = logging.getLogger("llm_client")

    def generate_text(self, prompt: str, max_tokens: int = 512, temperature: float = 0.0) -> str:
        """
        Calls the Ollama LLM API to generate text.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        try:
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data.get("response") or data.get("text") or ""
        except Exception as e:
            self.logger.error(f"LLM request failed: {e}")
            raise RuntimeError(f"LLM request failed: {e}")

# Singleton instance for import
llm_client = LLMClient(
    base_url=settings.ollama_base_url,
    model=settings.llm_model,
)