"""LLM 프로바이더 기본 클래스 모듈.

이 모듈은 모든 LLM 프로바이더의 기본 클래스를 정의합니다.
모든 구체적인 LLM 프로바이더는 BaseLLMProvider를 상속받아
필요한 메서드를 구현해야 합니다.
"""

from abc import ABC, abstractmethod
from typing import Optional
from ..logger import get_logger
from ..exceptions import LLMProviderError, APIKeyError

class BaseLLMProvider(ABC):
    """LLM 프로바이더 기본 클래스.
    
    이 클래스는 모든 LLM 프로바이더의 공통 인터페이스를 제공합니다.
    추상 메서드를 구현하여 각 프로바이더별로 맞춤형 로직을 구현할 수 있습니다.
    
    클래스 속성:
        api_key: LLM API 키
        timeout: API 호출 타임아웃 (초)
        logger: 로거 인스턴스
        
    사용 예시:
        class OpenAIProvider(BaseLLMProvider):
            def call(self, prompt: str, temperature: float, max_tokens: int) -> str:
                # OpenAI API 호출 로직 구현
                pass
                
            def count_tokens(self, text: str) -> int:
                # 토큰 수 계산 로직 구현
                pass
    """
    
    def __init__(self, api_key: Optional[str] = None, timeout: int = 30):
        """BaseLLMProvider 초기화.
        
        인자:
            api_key: LLM API 키 (기본값: None)
            timeout: API 호출 타임아웃 (초, 기본값: 30)
        """
        self.api_key = api_key
        self.timeout = timeout
        self.logger = get_logger(__name__)
    
    @abstractmethod
    async def call(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """LLM 호출 메서드 (구현 필수).
        
        이 메서드는 실제 LLM API 호출을 담당합니다.
        구체적인 프로바이더 클래스에서 구현해야 합니다.
        
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
        pass
    
    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """토큰 수 계산 메서드 (구현 필수).
        
        이 메서드는 입력 텍스트의 토큰 수를 계산합니다.
        구체적인 프로바이더 클래스에서 구현해야 합니다.
        
        인자:
            text: 토큰 수를 계산할 텍스트
            
        반환값:
            텍스트의 토큰 수
            
        발생 예외:
            LLMProviderError: 토큰 계산 실패 시
        """
        pass
    
    def validate_api_key(self) -> None:
        """API 키 유효성 검증.
        
        API 키가 설정되어 있는지 확인합니다.
        유효하지 않으면 APIKeyError를 발생시킵니다.
        
        발생 예외:
            APIKeyError: API 키가 없을 때
        """
        if not self.api_key:
            raise APIKeyError(f"{self.__class__.__name__} API 키가 설정되지 않았습니다")
