"""프롬프트 엔지니어링 템플릿 모듈.

이 모듈은 사진 촬영 기법을 위한 다양한 템플릿을 제공합니다.
"""

# 카메라 앵글 템플릿
CAMERA_ANGLES_EN = [
    "front", "3/4_angle", "profile", "overhead", "low_angle", "dutch_angle"
]
CAMERA_ANGLES_KR = [
    "정면", "3/4 각도", "측면", "오버헤드", "로우 앵글", "더치 앵글"
]
CAMERA_ANGLES_MAP = {
    "정면": "front-facing shot, direct eye contact, centered composition",
    "3/4 각도": "three-quarter view, subtle shoulder rotation, engaging angle",
    "측면": "side profile, sharp profile line, defined features",
    "오버헤드": "overhead shot, top-down perspective, bird's eye view",
    "로우 앵글": "low angle shot, looking upward, heroic perspective",
    "더치 앵글": "dutch angle, diagonal horizon, 15-30 degree tilt"
}

# 렌즈 템플릿
CAMERA_LENSES_EN = [
    "24mm", "35mm", "50mm", "85mm", "135mm", "macro"
]
CAMERA_LENSES_KR = [
    "24mm (초광각)", "35mm (광각)", "50mm (표준)", "85mm (망원)", "135mm (장망원)", "매크로 (접사)"
]
CAMERA_LENSES_MAP = {
    "24mm (초광각)": "24mm lens, ultra-wide angle, expansive environmental context, slight distortion at edges",
    "35mm (광각)": "35mm lens, standard-wide angle, natural field of view, minimal distortion",
    "50mm (표준)": "50mm lens, standard prime lens, natural perspective, sharp focus, versatile",
    "85mm (망원)": "85mm telephoto prime, shallow depth of field, beautiful bokeh, subject isolation",
    "135mm (장망원)": "135mm telephoto lens, strong background compression, narrow field of view",
    "매크로 (접사)": "macro lens, extreme close-up, sharp fine details, shallow depth of field"
}

# 조명 설정
LIGHTING_SETUPS_EN = [
    "studio", "cinematic", "natural", "golden_hour", "backlit", "rim_lighting", "chiaroscuro", "neon"
]
LIGHTING_SETUPS_KR = [
    "스튜디오 조명", "시네마틱 조명", "자연광", "골든 아워", "역광", "림 라이팅", "키아로스쿠로", "네온 조명"
]
LIGHTING_SETUPS_MAP = {
    "스튜디오 조명": "professional studio lighting, key light, fill light, rim light, three-point lighting setup, controlled shadows",
    "시네마틱 조명": "cinematic lighting, dramatic shadows, single key light source, moody atmosphere, chiaroscuro elements",
    "자연광": "natural window light, soft diffused daylight, warm color temperature, gentle shadows",
    "골든 아워": "golden hour lighting, sunset/sunrise, warm golden tones, long shadows, lens flare possible",
    "역광": "backlit subject, rim lighting, silhouette effect, bright background",
    "림 라이팅": "rim light from behind, edge highlighting, luminous contours, dark subject",
    "키아로스쿠로": "dramatic chiaroscuro, strong contrast between light and shadow, theatrical",
    "네온 조명": "neon ambient lighting, cyberpunk atmosphere, saturated colored lights, modern urban"
}

# 무드/분위기
MOOD_ATMOSPHERES_EN = [
    "dramatic", "moody", "bright_cheerful", "melancholic", "mysterious", "romantic", "dystopian", "ethereal"
]
MOOD_ATMOSPHERES_KR = [
    "극적인", "음울한", "밝고 쾌활한", "멜랑콜리한", "신비로운", "낭만적인", "디스토피아적인", "영묘한"
]
MOOD_ATMOSPHERES_MAP = {
    "극적인": "dramatic atmosphere, strong emotions, contrast, theatrical elements, intense",
    "음울한": "dark atmosphere, mysterious, tension, emotional depth, moody",
    "밝고 쾌활한": "bright atmosphere, hopeful, vibrant, positive emotions, uplifting",
    "멜랑콜리한": "melancholic, sentimental, bittersweet tone, deep emotion",
    "신비로운": "mysterious, enigmatic, unexplained mood",
    "낭만적인": "romantic atmosphere, love, emotion, warm feelings, intimate",
    "디스토피아적인": "dystopian mood, bleak feeling, futuristic pessimism",
    "영묘한": "ethereal, otherworldly, light and dreamlike"
}

# 색감 템플릿
COLOR_GRADES_EN = [
    "vibrant", "desaturated", "warm_tones", "cool_tones", "monochrome", "duotone", "cinematic_color"
]
COLOR_GRADES_KR = [
    "생생한", "채도 낮은", "따뜻한 톤", "차가운 톤", "흑백", "듀오톤", "시네마틱 색감"
]
COLOR_GRADES_MAP = {
    "생생한": "vibrant color grading, saturated hues, lively contrast",
    "채도 낮은": "desaturated tones, reduced color intensity, understated mood",
    "따뜻한 톤": "warm tones, golden, orange tint, cozy feeling",
    "차가운 톤": "cool tones, blueish hue, modern clean look",
    "흑백": "monochrome, black and white, single color range",
    "듀오톤": "duotone, two color grading, artistic style",
    "시네마틱 색감": "cinematic color grading, film-like appearance, mood emphasis"
}

# 구성
COMPOSITIONS_EN = [
    "centered", "rule_of_thirds", "leading_lines", "depth_layers", "symmetrical", "diagonal"
]
COMPOSITIONS_KR = [
    "중앙 구도", "삼분할 구도", "리딩 라인", "깊이 레이어", "대칭 구도", "대각선 구도"
]
COMPOSITIONS_MAP = {
    "중앙 구도": "centered composition, focal point in the middle, balanced framing",
    "삼분할 구도": "rule of thirds composition, leading lines, balanced proportions",
    "리딩 라인": "leading lines composition, guiding the eye, directional flow",
    "깊이 레이어": "depth layer composition, foreground/background separation",
    "대칭 구도": "symmetrical composition, balanced elements, stability and harmony",
    "대각선 구도": "diagonal composition, dynamic movement, visual interest"
}

# 화질
QUALITY_SETTINGS_EN = [
    "ultra_detailed", "high_quality", "professional", "cinematic_quality"
]
QUALITY_SETTINGS_KR = [
    "초고화질", "고품질", "전문적인", "시네마틱 품질"
]
QUALITY_SETTINGS_MAP = {
    "초고화질": "ultra detailed, highest resolution, intricate textures",
    "고품질": "high quality image, optimized performance, best results, professional",
    "전문적인": "professional quality, commercial finish, flawless result",
    "시네마틱 품질": "cinematic quality, film aesthetics, premium quality"
}

# 부정 프롬프트
NEGATIVE_PROMPTS_EN = [
    "standard", "strict", "minimal"
]
NEGATIVE_PROMPTS_KR = [
    "표준", "엄격한", "최소한의"
]
NEGATIVE_PROMPTS_MAP = {
    "표준": "standard negative prompt, remove low quality, artifacts",
    "엄격한": "strict negative prompt, enforce natural appearance, remove all imperfections",
    "최소한의": "minimal negative, focus only on primary flaws"
}
