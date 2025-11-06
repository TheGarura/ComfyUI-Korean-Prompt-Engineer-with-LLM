from typing import Dict, List, Optional, Tuple
from .exceptions import ValidationError
from .logger import get_logger

logger = get_logger(__name__)

class PromptEngineer:
    def __init__(self):
        from .templates import (
            CAMERA_ANGLES_MAP, CAMERA_LENSES_MAP, LIGHTING_SETUPS_MAP, MOOD_ATMOSPHERES_MAP,
            COLOR_GRADES_MAP, COMPOSITIONS_MAP, QUALITY_SETTINGS_MAP, NEGATIVE_PROMPTS_MAP
        )
        self.camera_angles = CAMERA_ANGLES_MAP
        self.camera_lenses = CAMERA_LENSES_MAP
        self.lighting_setups = LIGHTING_SETUPS_MAP
        self.mood_atmospheres = MOOD_ATMOSPHERES_MAP
        self.color_grades = COLOR_GRADES_MAP
        self.compositions = COMPOSITIONS_MAP
        self.quality_settings = QUALITY_SETTINGS_MAP
        self.negative_prompts = NEGATIVE_PROMPTS_MAP

    def validate_options(self, **kwargs) -> Tuple[bool, Optional[str]]:
        # ... (생략: 옵션 체크)
        return True, None

    def apply_photography_techniques(self, base_prompt: str, **options) -> str:
        is_valid, error_msg = self.validate_options(**options)
        if not is_valid:
            raise ValidationError(error_msg)
        prompt_parts = [base_prompt]
        if options.get('camera_angle'): prompt_parts.append(self.camera_angles[options['camera_angle']])
        if options.get('camera_lens'): prompt_parts.append(self.camera_lenses[options['camera_lens']])
        if options.get('lighting_setup'): prompt_parts.append(self.lighting_setups[options['lighting_setup']])
        if options.get('mood_atmosphere'): prompt_parts.append(self.mood_atmospheres[options['mood_atmosphere']])
        if options.get('color_grade'): prompt_parts.append(self.color_grades[options['color_grade']])
        if options.get('composition'): prompt_parts.append(self.compositions[options['composition']])
        if options.get('quality_settings'): prompt_parts.append(self.quality_settings[options['quality_settings']])
        if options.get('custom_instructions'): prompt_parts.append(options['custom_instructions'])
        final_prompt = ", ".join(part for part in prompt_parts if part.strip())
        logger.debug(f"프롬프트 최종 확장: {final_prompt}")
        return final_prompt

    def generate_negative_prompt(self, style: str = "standard") -> str:
        if style not in self.negative_prompts:
            style = "standard"
        return self.negative_prompts[style]
