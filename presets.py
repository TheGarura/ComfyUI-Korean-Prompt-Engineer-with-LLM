"""
프리셋 관리 모듈.

이 모듈은 미리 정의된 프롬프트 프리셋을 관리하며,
사용자에게 일관된 프롬프트 생성 경험을 제공합니다.

프리셋은 다양한 촬영 시나리오에 맞춘 사전 설정된
카메라 앵글, 렌즈, 조명, 무드 등 프롬프트 파라미터를 포함합니다.
"""

from typing import Dict, List, Optional

# 미리 정의된 프리셋 딕셔너리
BUILTIN_PRESETS: Dict[str, Dict] = {
    "portrait_professional": {
        "camera_angle": "3/4_angle",
        "camera_lens": "85mm",
        "lighting_setup": "studio",
        "mood_atmosphere": "romantic",
        "color_grade": "warm_tones",
        "composition": "rule_of_thirds",
        "quality_settings": "professional",
        "temperature": 0.7,
        "max_tokens": 1000,
        "description": "전문가 수준의 인물 초상화 촬영"
    },
    
    "landscape_cinematic": {
        "camera_angle": "overhead",
        "camera_lens": "24mm",
        "lighting_setup": "golden_hour",
        "mood_atmosphere": "dramatic",
        "color_grade": "cinematic_color",
        "composition": "rule_of_thirds",
        "quality_settings": "cinematic_quality",
        "temperature": 0.5,
        "max_tokens": 1200,
        "description": "영화적 풍경 촬영"
    },
    
    "product_clean": {
        "camera_angle": "front",
        "camera_lens": "50mm",
        "lighting_setup": "studio",
        "mood_atmosphere": "bright_cheerful",
        "color_grade": "vibrant",
        "composition": "centered",
        "quality_settings": "high_quality",
        "temperature": 0.3,
        "max_tokens": 800,
        "description": "깨끗하고 밝은 제품 사진"
    }
}


def get_preset(name: str) -> Dict:
    """지정된 이름의 프리셋을 반환합니다.
    
    인자:
        name: 프리셋 이름
        
    반환값:
        프리셋 딕셔너리
        
    발생 예외:
        KeyError: 존재하지 않는 프리셋 이름일 경우
    """
    if name not in BUILTIN_PRESETS:
        raise KeyError(f"존재하지 않는 프리셋: {name}")
    return BUILTIN_PRESETS[name]


def list_presets() -> List[str]:
    """사용 가능한 모든 프리셋 이름 목록을 반환합니다.
    
    반환값:
        프리셋 이름 목록
    """
    return list(BUILTIN_PRESETS.keys())


# 모듈 수준에서 사용 가능한 프리셋 목록
__all__ = ["BUILTIN_PRESETS", "get_preset", "list_presets"]
