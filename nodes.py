from typing import Tuple
from .logger import get_logger
from .exceptions import ValidationError, CLIPEncodingError, KoreanPromptEngineerError
from .templates import (
    CAMERA_ANGLES_KR, CAMERA_ANGLES_MAP,
    CAMERA_LENSES_KR, CAMERA_LENSES_MAP,
    LIGHTING_SETUPS_KR, LIGHTING_SETUPS_MAP,
    MOOD_ATMOSPHERES_KR, MOOD_ATMOSPHERES_MAP,
    COLOR_GRADES_KR, COLOR_GRADES_MAP,
    COMPOSITIONS_KR, COMPOSITIONS_MAP,
    QUALITY_SETTINGS_KR, QUALITY_SETTINGS_MAP,
    NEGATIVE_PROMPTS_KR, NEGATIVE_PROMPTS_MAP,
)
from .utils import validate_korean_prompt, sanitize_text, validate_option
from .prompt_engineer import PromptEngineer
from .llm_manager import LLMManager

logger = get_logger(__name__)

# LLMManager 인스턴스를 생성하여 사용 가능한 프로바이더 목록을 가져옵니다.
# 이 부분은 모듈 로드 시 한 번만 실행됩니다.
llm_manager_instance = LLMManager()
AVAILABLE_PROVIDERS = llm_manager_instance.get_available_providers()

def build_image_prompt_instruction(korean_prompt: str, options: dict) -> str:
    guidance = (
        "Please generate an English image generation prompt for a generative AI model (such as Stable Diffusion) "
        "using all of the following details. Do NOT include commentary, recommendations, questions, or conversational elements. "
        "Your output MUST be a single English prompt sentence for direct use in image generation: "
        "compact, descriptive, and professionally optimized. NO explanation — ONLY the prompt.\n"
        "Details:\n"
        f"- Korean description: {korean_prompt}\n"
    )
    for k, v in options.items():
        if v:
            guidance += f"- {k}: {v}\n"
    guidance += (
        "Output only the complete English prompt. Do NOT generate anything else."
    )
    return guidance

class KoreanPromptEngineer:
    display_name = "Korean Prompt Engineer 🇰🇷"
    description = "한국어 프롬프트를 멀티 LLM으로 확장"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_text", "negative_text")
    FUNCTION = "execute"
    CATEGORY = "conditioning/prompt"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "korean_prompt": ("STRING", {"multiline": True, "default": "미래 도시의 밤거리를 걷는 사이버펑크 고양이", "forceInput": False, "label": "한국어 프롬프트"}),
            },
            "optional": {
                "camera_angle": (CAMERA_ANGLES_KR, {"default": "오버헤드", "label": "카메라 앵글"}),
                "camera_lens": (CAMERA_LENSES_KR, {"default": "50mm (표준)", "label": "카메라 렌즈"}),
                "lighting_setup": (LIGHTING_SETUPS_KR, {"default": "스튜디오 조명", "label": "조명 설정"}),
                "mood_atmosphere": (MOOD_ATMOSPHERES_KR, {"default": "극적인", "label": "무드/분위기"}),
                "color_grade": (COLOR_GRADES_KR, {"default": "생생한", "label": "색감 보정"}),
                "composition": (COMPOSITIONS_KR, {"default": "삼분할 구도", "label": "구도"}),
                "quality_settings": (QUALITY_SETTINGS_KR, {"default": "고품질", "label": "화질 설정"}),
                "negative_prompt_style": (NEGATIVE_PROMPTS_KR, {"default": "표준", "label": "네거티브 프롬프트 스타일"}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0, "step": 0.1, "label": "창의성 (Temperature)"}),
                "max_tokens": ("INT", {"default": 1000, "min": 100, "max": 2000, "step": 100, "label": "최대 토큰 수"}),
                "provider_name": (AVAILABLE_PROVIDERS, {"default": "openai", "label": "LLM 프로바이더"}),
                "custom_instructions": ("STRING", {"multiline": True, "default": "", "label": "사용자 정의 지침 (영문)"}),
            }
        }

    async def execute(
        self, korean_prompt: str,
        camera_angle="오버헤드", camera_lens="50mm (표준)",
        lighting_setup="스튜디오 조명", mood_atmosphere="극적인",
        color_grade="생생한", composition="삼분할 구도",
        quality_settings="고품질", negative_prompt_style="표준",
        temperature=0.7, max_tokens=1000, provider_name="openai", custom_instructions=""
    ) -> Tuple[str, str]:
        try:
            logger.info("KoreanPromptEngineer execute started")
            validate_korean_prompt(korean_prompt)
            
            # 한국어 옵션을 영어 값으로 매핑
            mapped_camera_angle = CAMERA_ANGLES_MAP.get(camera_angle, camera_angle)
            mapped_camera_lens = CAMERA_LENSES_MAP.get(camera_lens, camera_lens)
            mapped_lighting_setup = LIGHTING_SETUPS_MAP.get(lighting_setup, lighting_setup)
            mapped_mood_atmosphere = MOOD_ATMOSPHERES_MAP.get(mood_atmosphere, mood_atmosphere)
            mapped_color_grade = COLOR_GRADES_MAP.get(color_grade, color_grade)
            mapped_composition = COMPOSITIONS_MAP.get(composition, composition)
            mapped_quality_settings = QUALITY_SETTINGS_MAP.get(quality_settings, quality_settings)
            mapped_negative_prompt_style = NEGATIVE_PROMPTS_MAP.get(negative_prompt_style, negative_prompt_style)

            valid_options = {
                "camera_angle": CAMERA_ANGLES_KR,
                "camera_lens": CAMERA_LENSES_KR,
                "lighting_setup": LIGHTING_SETUPS_KR,
                "mood_atmosphere": MOOD_ATMOSPHERES_KR,
                "color_grade": COLOR_GRADES_KR,
                "composition": COMPOSITIONS_KR,
                "quality_settings": QUALITY_SETTINGS_KR,
                "negative_prompt_style": NEGATIVE_PROMPTS_KR,
            }
            for option_name, valid_values in valid_options.items():
                validate_option(option_name, locals()[option_name], valid_values)

            options = {
                "camera_angle": mapped_camera_angle,
                "camera_lens": mapped_camera_lens,
                "lighting_setup": mapped_lighting_setup,
                "mood_atmosphere": mapped_mood_atmosphere,
                "color_grade": mapped_color_grade,
                "composition": mapped_composition,
                "quality_settings": mapped_quality_settings,
                "custom_instructions": custom_instructions,
            }
            llm = LLMManager()
            instruction = build_image_prompt_instruction(korean_prompt, options)
            english_prompt = await llm.call(provider_name, instruction, temperature, max_tokens)

            # 프롬프트 확장 (문자열 최종 병합)
            engineer = PromptEngineer()
            positive_text = engineer.apply_photography_techniques(english_prompt,
                                                                 camera_angle=camera_angle,
                                                                 camera_lens=camera_lens,
                                                                 lighting_setup=lighting_setup,
                                                                 mood_atmosphere=mood_atmosphere,
                                                                 color_grade=color_grade,
                                                                 composition=composition,
                                                                 quality_settings=quality_settings,
                                                                 custom_instructions=custom_instructions)
            negative_text = engineer.generate_negative_prompt(negative_prompt_style)
            return (positive_text, negative_text)

        except ValidationError as e:
            logger.error(f"Validation error: {str(e)}")
            raise e
        except CLIPEncodingError as e:
            logger.error(f"CLIP encoding error: {str(e)}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            raise KoreanPromptEngineerError(f"Unexpected error: {str(e)}")

NODE_CLASS_MAPPINGS = {
    "KoreanPromptEngineer": KoreanPromptEngineer
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "KoreanPromptEngineer": KoreanPromptEngineer.display_name,
}
