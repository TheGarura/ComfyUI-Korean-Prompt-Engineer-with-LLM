"""OpenAI GPT-4o 프로바이더 모듈.

이 모듈은 OpenAI API를 사용하여 프롬프트를 확장하는 LLM 프로바이더를 제공합니다.
"""

import os
from typing import Optional
from ..logger import get_logger
from ..exceptions import LLMProviderError, APIKeyError
from .base import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    """OpenAI GPT-4o 프로바이더.
    
    이 클래스는 OpenAI의 GPT-4o 모델을 사용하여 프롬프트를 확장합니다.
    BaseLLMProvider를 상속받아 필요한 메서드를 구현합니다.
    
    클래스 속성:
        client: AsyncOpenAI 클라이언트 인스턴스
        model: 사용할 모델 이름 (기본값: gpt-4o)
        logger: 로거 인스턴스
        
    사용 예시:
        provider = OpenAIProvider(api_key="your-api-key")
        response = asyncio.run(provider.call("프롬프트", 0.7, 1000))
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """OpenAIProvider 초기화.
        
        인자:
            api_key: OpenAI API 키 (기본값: None)
            model_name: 사용할 OpenAI 모델 이름 (기본값: gpt-4o)
        """
        super().__init__(api_key)
        from openai import AsyncOpenAI
        self.client = AsyncOpenAI(api_key=self.api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model_name or os.getenv("OPENAI_MODEL_NAME", "gpt-4o")
        self.validate_api_key()
    
    async def call(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """OpenAI API 호출.
        
        이 메서드는 OpenAI API를 호출하여 프롬프트를 확장합니다.
        
        인자:
            prompt: LLM에 전달할 프롬프트 문자열
            temperature: 샘플링 온도 (0.0~2.0)
            max_tokens: 최대 토큰 수
            
        반환값:
            LLM의 응답 문자열
            
        발생 예외:
            LLMProviderError: LLM 호출 실패 시
            APIKeyError: API 키가 없을 때
        """
        try:
            self.logger.debug(f"Calling OpenAI with temp={temperature}")
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=self.timeout
            )
            
            self.logger.info(f"OpenAI response received")
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"OpenAI call failed: {str(e)}")
            raise LLMProviderError(f"OpenAI failed: {str(e)}")
    
    def count_tokens(self, text: str) -> int:
        """토큰 수 계산.
        
        이 메서드는 입력 텍스트의 토큰 수를 계산합니다.
        간단한 추정을 사용하여 토큰 수를 계산합니다.
        
        인자:
            text: 토큰 수를 계산할 텍스트
            
        반환값:
            텍스트의 토큰 수
            
        발생 예외:
            LLMProviderError: 토큰 계산 실패 시
        """
        # 간단한 추정: 4자 = 1토큰 (실제 구현에서는 tiktoken 사용 권장)
        return len(text) // 4
