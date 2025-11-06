"""Google Gemini 프로바이더 모듈.

이 모듈은 Google Gemini LLM API를 위한 프로바이더 구현을 제공합니다.
"""

import os
from typing import Optional
import google.generativeai as genai  # ← 파일 상단으로 이동
from ..llm_providers.base import BaseLLMProvider
from ..exceptions import LLMProviderError, APIKeyError
from ..logger import get_logger

logger = get_logger(__name__)


class GeminiProvider(BaseLLMProvider):
    """Google Gemini 프로바이더"""

    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        super().__init__(api_key)
        self.api_key = self.api_key or os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise APIKeyError("GEMINI_API_KEY is not set")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name or os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash"))
        self.validate_api_key()
    
    async def call(
        self, 
        prompt: str, 
        temperature: float = 0.7, 
        max_tokens: int = 2000
    ) -> str:
        """Gemini API 호출"""
        try:
            self.logger.debug(f"Calling Gemini with temp={temperature}")
            
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens
                )
            )
            
            self.logger.info(f"Gemini response received")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Gemini call failed: {str(e)}")
            raise LLMProviderError(f"Gemini failed: {str(e)}")
    
    def count_tokens(self, text: str) -> int:
        """토큰 개수 추정"""
        return int(len(text) * 0.25)
    
    def validate_api_key(self) -> None:
        """API 키 검증"""
        if not self.api_key:
            raise APIKeyError("GEMINI_API_KEY is not set")
