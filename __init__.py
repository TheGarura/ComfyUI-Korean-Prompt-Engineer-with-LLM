"""Korean Prompt Engineer 패키지.

이 패키지는 ComfyUI와 통합된 한국어 프롬프트 엔지니어링 기능을 제공합니다.
"""

from .nodes import KoreanPromptEngineer
from .prompt_engineer import PromptEngineer
from .cache_manager import CacheManager
from .utils import (
    validate_korean_prompt,
    sanitize_text,
    truncate_prompt,
    combine_prompt_parts,
    validate_option
)
from .templates import (
    CAMERA_ANGLES_EN,
    CAMERA_LENSES_EN,
    LIGHTING_SETUPS_EN,
    MOOD_ATMOSPHERES_EN,
    COLOR_GRADES_EN,
    COMPOSITIONS_EN,
    QUALITY_SETTINGS_EN,
    NEGATIVE_PROMPTS_EN
)
from .presets import BUILTIN_PRESETS, get_preset, list_presets
from .logger import get_logger
from .exceptions import (
    KoreanPromptEngineerError,
    LLMProviderError,
    APIKeyError,
    PromptEngineeringError,
    CLIPEncodingError,
    ValidationError,
    CacheError,
    RateLimitError,
    SecurityError
)

# ==================== 필수: ComfyUI 노드 등록 ====================
# ComfyUI가 이 파일을 통해 커스텀 노드를 발견하기 위해 필수
NODE_CLASS_MAPPINGS = {
    "KoreanPromptEngineer": KoreanPromptEngineer,
}

# (선택사항) ComfyUI UI에 표시할 노드의 친화적인 이름
NODE_DISPLAY_NAME_MAPPINGS = {
    "KoreanPromptEngineer": KoreanPromptEngineer.display_name,
}

__version__ = "0.1.0"
__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "KoreanPromptEngineer",
    "PromptEngineer",
    "CacheManager",
    "validate_korean_prompt",
    "sanitize_text",
    "truncate_prompt",
    "combine_prompt_parts",
    "validate_option",
    "CAMERA_ANGLES_EN",
    "CAMERA_LENSES_EN",
    "LIGHTING_SETUPS_EN",
    "MOOD_ATMOSPHERES_EN",
    "COLOR_GRADES_EN",
    "COMPOSITIONS_EN",
    "QUALITY_SETTINGS_EN",
    "NEGATIVE_PROMPTS_EN",
    "BUILTIN_PRESETS",
    "get_preset",
    "list_presets",
    "get_logger",
    "KoreanPromptEngineerError",
    "LLMProviderError",
    "APIKeyError",
    "PromptEngineeringError",
    "CLIPEncodingError",
    "ValidationError",
    "CacheError",
    "RateLimitError",
    "SecurityError"
]
