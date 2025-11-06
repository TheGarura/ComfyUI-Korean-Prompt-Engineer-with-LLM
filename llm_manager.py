# llm_manager.py

from typing import Optional
from .logger import get_logger
from .exceptions import ValidationError
import os
from dotenv import load_dotenv

logger = get_logger(__name__)
load_dotenv()  # .env 파일 자동 로드

class LLMManager:
    def __init__(self):
        from .llm_providers.openai_provider import OpenAIProvider
        from .llm_providers.claude_provider import ClaudeProvider
        from .llm_providers.gemini_provider import GeminiProvider
        from .llm_providers.ollama_provider import OllamaProvider
        self.providers = {
            "openai": OpenAIProvider,
            "claude": ClaudeProvider,
            "gemini": GeminiProvider,
            "ollama": OllamaProvider,
        }
        self.logger = get_logger(__name__)

    def get_available_providers(self) -> list[str]:
        """사용 가능한 LLM 프로바이더 목록을 반환합니다."""
        return list(self.providers.keys())

    async def call(self, provider_name: str, prompt: str, temperature: float, max_tokens: int) -> str:
        if provider_name not in self.providers:
            raise ValidationError(f"알 수 없는 프로바이더: {provider_name}")
        
        provider_class = self.providers[provider_name]
        
        # .env에서 API 키 및 모델 이름 읽기
        api_key = None
        model_name = None
        base_url = None # Ollama 전용
        
        if provider_name == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            model_name = os.getenv("OPENAI_MODEL_NAME")
            if not api_key:
                raise ValidationError(f"{provider_name}의 API 키가 .env 또는 환경변수에 없습니다")
            provider = provider_class(api_key=api_key, model_name=model_name)
            self.logger.info(f"LLM 프로바이더 사용: {provider_name} / API 키 및 모델명 전달됨")
        elif provider_name == "claude":
            api_key = os.getenv("ANTHROPIC_API_KEY")
            model_name = os.getenv("ANTHROPIC_MODEL_NAME")
            if not api_key:
                raise ValidationError(f"{provider_name}의 API 키가 .env 또는 환경변수에 없습니다")
            provider = provider_class(api_key=api_key, model_name=model_name)
            self.logger.info(f"LLM 프로바이더 사용: {provider_name} / API 키 및 모델명 전달됨")
        elif provider_name == "gemini":
            api_key = os.getenv("GEMINI_API_KEY")
            model_name = os.getenv("GEMINI_MODEL_NAME")
            if not api_key:
                raise ValidationError(f"{provider_name}의 API 키가 .env 또는 환경변수에 없습니다")
            provider = provider_class(api_key=api_key, model_name=model_name)
            self.logger.info(f"LLM 프로바이더 사용: {provider_name} / API 키 및 모델명 전달됨")
        elif provider_name == "ollama":
            base_url = os.getenv("OLLAMA_BASE_URL")
            model_name = os.getenv("OLLAMA_MODEL_NAME")
            if not base_url:
                raise ValidationError(f"{provider_name}의 Base URL이 .env 또는 환경변수에 없습니다")
            provider = provider_class(base_url=base_url, model_name=model_name)
            self.logger.info(f"LLM 프로바이더 사용: {provider_name} / Base URL 및 모델명 전달됨")
        else:
            raise ValidationError(f"알 수 없는 프로바이더: {provider_name}")
            
        result = await provider.call(prompt, temperature, max_tokens)
        return result
