# utils.py

from typing import List, Set
from .exceptions import ValidationError
import re

def validate_korean_prompt(prompt: str, max_length: int = 10000, raise_exception: bool = True) -> bool:
    if not prompt or len(prompt.strip()) == 0:
        if raise_exception:
            raise ValidationError("프롬프트는 비어있을 수 없습니다")
        return False
    try:
        prompt.encode('utf-8')
    except UnicodeEncodeError:
        if raise_exception:
            raise ValidationError("프롬프트는 UTF-8 인코딩 가능해야 합니다")
        return False
    # 한국어 문자 포함 여부 확인 (간단한 한글 유니코드 범위 체크)
    if not re.search(r'[\u1100-\u11FF\u3130-\u318F\uAC00-\uD7AF]', prompt):
        if raise_exception:
            raise ValidationError("프롬프트에 한국어 문자가 포함되어 있지 않습니다.")
        return False
    if len(prompt) > max_length:
        if raise_exception:
            raise ValidationError(f"프롬프트 길이는 {max_length}자 이하여야 합니다")
        return False
    return True

def sanitize_text(text: str) -> str:
    if text is None:
        return ""
    sanitized = text.strip()
    sanitized = re.sub(r'\s+', ' ', sanitized)
    return sanitized

def truncate_prompt(prompt: str, max_length: int = 1000) -> str:
    if prompt is None:
        return ""
    if len(prompt) <= max_length:
        return prompt
    truncated = prompt[:max_length]
    last_space = truncated.rfind(' ')
    if last_space > 0:
        truncated = truncated[:last_space]
    return truncated.strip()

def combine_prompt_parts(*parts) -> str:
    filtered_parts = [part for part in parts if part and isinstance(part, str)]
    seen: Set[str] = set()
    unique_parts = []
    for part in filtered_parts:
        if part not in seen:
            seen.add(part)
            unique_parts.append(part)
    return ' '.join(unique_parts)

def validate_option(option_name: str, value: str, valid_values: List[str]) -> bool:
    if not value:
        raise ValidationError(f"{option_name}은(는) 비어있을 수 없습니다")
    if value not in valid_values:
        valid_values_str = ', '.join(valid_values)
        raise ValidationError(f"{option_name}은(는) {valid_values_str} 중 하나여야 합니다")
    return True
