"""Anthropic Claude 프로바이더 모듈.

이 모듈은 Anthropic Claude API를 사용하여 프롬프트를 확장하는 LLM 프로바이더를 제공합니다.
"""

import os
from typing import Optional
from ..logger import get_logger
from ..exceptions import LLMProviderError, APIKeyError
from .base import BaseLLMProvider

class ClaudeProvider(BaseLLMProvider):
    """Anthropic Claude 프로바이더.
    
    이 클래스는 Anthropic의 Claude 모델을 사용하여 프롬프트를 확장합니다.
    BaseLLMProvider를 상속받아 필요한 메서드를 구현합니다.
    
    클래스 속성:
        client: Anthropic 클라이언트 인스턴스
        model: 사용할 모델 이름 (기본값: claude-3-5-sonnet-20241022)
        logger: 로거 인스턴스
        
    사용 예시:
        provider = ClaudeProvider(api_key="your-api-key")
        response = asyncio.run(provider.call("프롬프트", 0.7, 1000))
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """ClaudeProvider 초기화.
        
        인자:
            api_key: Anthropic API 키 (기본값: None)
            model_name: 사용할 Anthropic 모델 이름 (기본값: claude-3-5-sonnet-20241022)
        """
        super().__init__(api_key)
        from anthropic import Anthropic
        self.client = Anthropic(api_key=self.api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model_name or os.getenv("ANTHROPIC_MODEL_NAME", "claude-3-5-sonnet-20241022")
        self.validate_api_key()
    
    async def call(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """Claude API 호출.
        
        이 메서드는 Anthropic Claude API를 호출하여 프롬프트를 확장합니다.
        
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
            self.logger.debug(f"Calling Claude with temp={temperature}")
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            self.logger.info(f"Claude response received")
            return response.content[0].text
            
        except Exception as e:
            self.logger.error(f"Claude call failed: {str(e)}")
            raise LLMProviderError(f"Claude failed: {str(e)}")
    
    def count_tokens(self, text: str) -> int:
        """토큰 수 계산.
        
        이 메서드는 입력 텍스트의 토큰 수를 계산합니다.
        Claude 모델용 추정 값을 사용합니다.
        
        인자:
            text: 토큰 수를 계산할 텍스트
            
        반환값:
            텍스트의 토큰 수
            
        발생 예외:
            LLMProviderError: 토큰 계산 실패 시
        """
        # Claude: 약 3.7자 = 1토큰 (실제 구현에서는 Anthropic의 토크나이저 사용 권장)
        return int(len(text) * 0.27)
