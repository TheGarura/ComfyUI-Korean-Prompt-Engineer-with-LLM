"""Ollama 로컬 LLM 프로바이더 모듈."""

from typing import Optional
import os
import logging
from .base import BaseLLMProvider
from ..exceptions import LLMProviderError

logger = logging.getLogger(__name__)


class OllamaProvider(BaseLLMProvider):
    """Ollama 로컬 LLM 프로바이더"""

    def __init__(self, base_url: Optional[str] = None, model_name: Optional[str] = None):
        super().__init__()
        self.base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = model_name or os.getenv("OLLAMA_MODEL_NAME", "deepseek-r1:32b")
        import ollama
        self.client = ollama.Client(host=self.base_url)
        self.check_model_available()

    def check_model_available(self):
        """모델 가용성 확인"""
        try:
            models = self.client.list(host=self.base_url)
            if self.model not in [m["name"] for m in models]:
                self.logger.warning(f"Model {self.model} not found. Pull it first.")
        except Exception as e:
            self.logger.warning(f"Could not check model availability: {e}")

    async def call(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """Ollama API 호출"""
        try:
            self.logger.debug(f"Calling Ollama model {self.model}")
            
            response = self.client.generate(
                model=self.model,
                prompt=prompt,
                stream=False,
                options={
                    "temperature": temperature,
                    "num_predict": max_tokens
                },
                host=self.base_url
            )
            
            self.logger.info(f"Ollama response received")
            return response["response"]
            
        except Exception as e:
            self.logger.error(f"Ollama call failed: {str(e)}")
            raise LLMProviderError(f"Ollama failed: {str(e)}")

    def count_tokens(self, text: str) -> int:
        return int(len(text) * 0.25)
