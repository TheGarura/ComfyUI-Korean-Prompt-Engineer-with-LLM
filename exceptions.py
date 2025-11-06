"""커스텀 예외 클래스 모듈.

이 모듈은 한국어 프롬프트 엔지니어링 시스템에서 사용하는
커스텀 예외 클래스들을 정의합니다. 예외 계층 구조를 통해
오류 처리를 명확하고 일관되게 관리합니다.
"""

from typing import Optional


class KoreanPromptEngineerError(Exception):
    """기본 예외 클래스.
    
    모든 커스텀 예외의 부모 클래스로, 시스템 전반의
    예외 처리를统一하게 관리하기 위해 사용됩니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)


class LLMProviderError(KoreanPromptEngineerError):
    """LLM 프로바이더 관련 오류.
    
    LLM API 호출 중 발생한 모든 오류를 처리하기 위한
    기본 예외 클래스입니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)


class APIKeyError(LLMProviderError):
    """API 키가 누락되었거나 유효하지 않을 때 발생.
    
    API 키가 설정되지 않았거나 유효하지 않은 경우 발생합니다.
    """

    def __init__(self, provider: str, message: Optional[str] = None):
        """예외 초기화.
        
        인자:
            provider: API 제공자 이름
            message: 추가 메시지 (선택)
        """
        self.provider = provider
        if message:
            full_message = f"{provider} API key error: {message}"
        else:
            full_message = f"{provider} API key not found. Please set the environment variable."
        super().__init__(full_message)


class PromptEngineeringError(KoreanPromptEngineerError):
    """프롬프트 처리 중 발생한 오류.
    
    프롬프트 엔지니어링 과정에서 발생한 모든 오류를 처리합니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)


class CLIPEncodingError(KoreanPromptEngineerError):
    """CLIP 토크나이징 중 발생한 오류.
    
    CLIP 모델을 사용한 토크나이징 작업 중 오류가 발생할 때 사용됩니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)


class ValidationError(KoreanPromptEngineerError):
    """입력 검증 중 발생한 오류.
    
    사용자 입력이나 데이터가 유효하지 않을 때 발생하는 오류입니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)


class CacheError(KoreanPromptEngineerError):
    """캐시 관련 오류.
    
    캐시 저장, 조회, 삭제 중 발생한 오류를 처리합니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)


class RateLimitError(LLMProviderError):
    """레이트 리미팅 오류.
    
    API 호출 제한으로 인해 발생한 오류로, 재시도가 가능한 오류입니다.
    """

    def __init__(self, provider: str, message: Optional[str] = None):
        """예외 초기화.
        
        인자:
            provider: API 제공자 이름
            message: 추가 메시지 (선택)
        """
        self.provider = provider
        if message:
            full_message = f"{provider} rate limit error: {message}"
        else:
            full_message = f"{provider} rate limit exceeded. Please try again later."
        super().__init__(full_message)


class SecurityError(KoreanPromptEngineerError):
    """보안 관련 오류.
    
    입력 검증, 프롬프트 인젝션 방지 등 보안 관련 작업 중 발생한 오류입니다.
    """

    def __init__(self, message: str):
        """예외 초기화.
        
        인자:
            message: 예외 메시지
        """
        self.message = message
        super().__init__(self.message)
