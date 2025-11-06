# Korean Prompt Engineer (한국어 프롬프트 엔지니어)

ComfyUI를 위한 한국어 기반의 전문 이미지 프롬프트 생성 노드입니다. 간단한 한국어 설명과 전문 사진/영상 기법 옵션을 조합하여, Stable Diffusion과 같은 이미지 생성 AI에 최적화된 상세한 영어 프롬프트를 자동으로 생성합니다.

![버전](https://img.shields.io/badge/version-0.1.0-blue)
![라이선스](https://img.shields.io/badge/license-MIT-green)
![개발자](https://img.shields.io/badge/developer-GARURA-orange)

## 📦 주요 기능

- **한국어 자연어 입력**: 간단한 한국어 아이디어를 입력하면 전문적인 영어 프롬프트로 자동 번역 및 확장됩니다.
- **다양한 LLM 지원**: OpenAI, Anthropic (Claude), Google (Gemini) 등 여러 LLM 프로바이더를 선택하여 프롬프트를 생성할 수 있습니다.
- **전문가 수준의 옵션**: 카메라 앵글, 렌즈, 조명, 색감 등 세부적인 사진/영상 기법을 메뉴에서 선택하여 프롬프트에 반영할 수 있습니다.
- **자동 네거티브 프롬프트**: 이미지 품질 저하 요소를 방지하기 위한 네거티브 프롬프트를 스타일별로 자동 생성합니다.
- **사용자 정의 지침**: 자신만의 특별한 스타일이나 요구사항을 `custom_instructions`에 추가하여 프롬프트 생성을 제어할 수 있습니다.

## 🛠 설치 방법

1. **저장소 복제**: ComfyUI의 `custom_nodes` 디렉토리 안에서 다음 명령어를 실행하여 프로젝트를 복제합니다.
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/your-repo-path/korean_prompt_engineer.git
   ```
   *(참고: `your-repo-path`는 실제 저장소 주소로 변경해주세요.)*

2. **의존성 설치**: 생성된 디렉토리로 이동하여 필요한 Python 패키지를 설치합니다.
   ```bash
   cd korean_prompt_engineer
   pip install -r requirements.txt
   ```

3. **ComfyUI 재시작**: ComfyUI를 완전히 종료한 후 다시 시작해야 노드가 정상적으로 로드됩니다.

## 📁 프로젝트 구조

프로젝트의 주요 디렉토리 및 파일 구조는 다음과 같습니다.

```
korean_prompt_engineer/
├── __init__.py             # ComfyUI 노드 등록 및 초기화
├── .env.example            # 환경 변수 설정 예시 파일
├── .gitignore              # Git 버전 관리 제외 파일
├── cache_manager.py        # 캐시 관리 로직
├── exceptions.py           # 사용자 정의 예외 처리
├── LICENSE                 # MIT 라이선스 정보
├── llm_manager.py          # LLM 프로바이더 관리 및 호출
├── logger.py               # 로깅 설정
├── nodes.py                # ComfyUI 커스텀 노드 정의
├── presets.py              # 프롬프트 생성에 사용되는 사전 설정 데이터
├── prompt_engineer.py      # 핵심 프롬프트 생성 로직
├── README.md               # 프로젝트 설명 (현재 파일)
├── requirements.txt        # Python 의존성 목록
├── templates.py            # 프롬프트 템플릿 정의
├── utils.py                # 유틸리티 함수 모음
└── llm_providers/          # LLM 프로바이더 모듈
    ├── __init__.py         # 프로바이더 패키지 초기화
    ├── base.py             # 기본 프로바이더 인터페이스
    ├── claude_provider.py  # Anthropic Claude 프로바이더 구현
    ├── gemini_provider.py  # Google Gemini 프로바이더 구현
    ├── ollama_provider.py  # Ollama 프로바이더 구현
    └── openai_provider.py  # OpenAI 프로바이더 구현
```

## ⚙️ 초기 설정: API 키 및 LLM 프로바이더 연동

이 노드를 사용하려면 최소 하나 이상의 LLM 서비스 API 키가 필요합니다.

1. **`.env` 파일 생성**: 프로젝트 루트 디렉토리의 `.env.example` 파일을 복사하여 `.env` 파일을 생성합니다.
   ```bash
   cp .env.example .env
   ```

2. **API 키 및 모델명 입력**: 생성된 `.env` 파일을 열고, 사용하고자 하는 LLM 서비스의 API 키와 모델명을 입력합니다. 사용하지 않는 서비스는 비워두거나 주석 처리할 수 있습니다.

   **지원되는 LLM 프로바이더 및 설정 예시:**

   *   **OpenAI**:
       ```ini
       OPENAI_API_KEY="sk-..."
       OPENAI_MODEL_NAME="gpt-4-turbo" # 또는 gpt-3.5-turbo 등
       ```
   *   **Anthropic (Claude)**:
       ```ini
       ANTHROPIC_API_KEY="sk-ant-..."
       ANTHROPIC_MODEL_NAME="claude-3-opus-20240229" # 또는 claude-3-sonnet-20240229 등
       ```
   *   **Google (Gemini)**:
       ```ini
       GEMINI_API_KEY="AIza..."
       GEMINI_MODEL_NAME="gemini-1.5-flash" # 또는 gemini-1.5-pro 등
       ```
   *   **Ollama**:
       ```ini
       OLLAMA_BASE_URL="http://localhost:11434" # Ollama 서버 URL
       OLLAMA_MODEL_NAME="llama3" # 로컬에 설치된 모델명
       ```
   *   **참고**: `provider_name`은 ComfyUI 노드에서 선택하는 이름과 일치해야 합니다. (예: `openai`, `anthropic`, `gemini`, `ollama`)

## 🚀 ComfyUI에서 사용하기

1. **노드 추가**: ComfyUI 워크플로우에서 마우스 오른쪽 버튼을 클릭하고 `Add Node` > `conditioning/prompt` > `Korean Prompt Engineer 🇰🇷`를 선택하여 노드를 추가합니다.

2. **입력값 설정**:
   - **`korean_prompt`**: 생성하고 싶은 이미지에 대한 아이디어를 한국어로 자유롭게 작성합니다. (예: `미래 도시의 밤거리를 걷는 사이버펑크 고양이`)
   - **`provider_name`**: 프롬프트 생성에 사용할 LLM 서비스를 선택합니다. (예: `openai`, `anthropic`, `gemini`). 이 이름은 `.env` 파일에 설정한 서비스와 일치해야 합니다.
   - **각종 옵션 (카메라, 조명 등)**: 원하는 스타일과 분위기에 맞춰 드롭다운 메뉴에서 다양한 사진/영상 기법을 선택합니다.
   - **`custom_instructions`**: 프롬프트에 꼭 포함하고 싶은 특별한 지시사항을 영어로 작성합니다. (예: `in the style of Blade Runner 2049`)

3. **출력 연결**:
   - **`positive_text`**: 생성된 긍정 프롬프트를 `CLIP Text Encode` 노드의 `text` 입력에 연결합니다.
   - **`negative_text`**: 생성된 부정 프롬프트를 `CLIP Text Encode` 노드의 `text` 입력에 연결합니다. (별도의 인코더 사용)

### 🎨 노드 파라미터 상세 설명

| 파라미터명 | 설명 | 선택 옵션 (예시) |
| --- | --- | --- |
| `한국어 프롬프트` | 이미지 아이디어를 담은 한국어 텍스트 | (자유 입력) |
| `LLM 프로바이더` | 사용할 LLM 서비스 이름 | `openai`, `anthropic`, `gemini`, `ollama` (드롭다운 선택) |
| `카메라 앵글` | 카메라 촬영 각도 | `정면` (front-facing), `3/4 각도` (three-quarter view), `측면` (side profile), `오버헤드` (top-down), `로우 앵글` (looking upward), `더치 앵글` (diagonal horizon) |
| `카메라 렌즈` | 카메라 렌즈 종류 | `24mm (초광각)` (ultra-wide), `35mm (광각)` (standard-wide), `50mm (표준)` (standard prime), `85mm (망원)` (telephoto prime), `135mm (장망원)` (telephoto), `매크로 (접사)` (extreme close-up) |
| `조명 설정` | 조명 스타일 | `스튜디오 조명` (professional studio lighting), `시네마틱 조명` (dramatic shadows), `자연광` (soft diffused daylight), `골든 아워` (sunset/sunrise), `역광` (silhouette effect), `림 라이팅` (edge highlighting), `키아로스쿠로` (strong contrast), `네온 조명` (cyberpunk atmosphere) |
| `무드/분위기` | 전체적인 분위기 | `극적인` (strong emotions), `음울한` (dark, mysterious), `밝고 쾌활한` (hopeful, vibrant), `멜랑콜리한` (sentimental, bittersweet), `신비로운` (enigmatic, unexplained), `낭만적인` (love, warm feelings), `디스토피아적인` (bleak, futuristic pessimism), `영묘한` (otherworldly, dreamlike) |
| `색감 보정` | 색감 보정 스타일 | `생생한` (saturated hues), `채도 낮은` (reduced color intensity), `따뜻한 톤` (golden, orange tint), `차가운 톤` (blueish hue), `흑백` (black and white), `듀오톤` (two color grading), `시네마틱 색감` (film-like appearance) |
| `구도` | 구도 기법 | `중앙 구도` (focal point in middle), `삼분할 구도` (balanced proportions), `리딩 라인` (guiding the eye), `깊이 레이어` (foreground/background separation), `대칭 구도` (balanced elements), `대각선 구도` (dynamic movement) |
| `화질 설정` | 이미지 품질 관련 키워드 | `초고화질` (highest resolution), `고품질` (optimized performance), `전문적인` (commercial finish), `시네마틱 품질` (film aesthetics) |
| `네거티브 프롬프트 스타일` | 네거티브 프롬프트의 강도/스타일 | `표준` (remove low quality, artifacts), `엄격한` (enforce natural appearance), `최소한의` (focus only on primary flaws) |
| `창의성 (Temperature)` | LLM의 창의성 (높을수록 다양) | 0.0 ~ 2.0 |
| `최대 토큰 수` | 생성될 프롬프트의 최대 길이 | 100 ~ 2000 |
| `사용자 정의 지침 (영문)` | 사용자 정의 추가 지침 (영문) | (자유 입력) |

## 📜 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)에 따라 배포됩니다.

---

# English Version

## Korean Prompt Engineer for ComfyUI

This is a Korean-based professional image prompt generation node for ComfyUI. It combines simple Korean descriptions with professional photography/videography options to automatically generate detailed English prompts optimized for image generation AIs like Stable Diffusion.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Developer](https://img.shields.io/badge/developer-GARURA-orange)

## 📦 Key Features

-   **Korean Natural Language Input**: Simply input your ideas in Korean, and they will be automatically translated and expanded into professional English prompts.
-   **Diverse LLM Support**: Choose from various LLM providers like OpenAI, Anthropic (Claude), Google (Gemini), and Ollama to generate prompts.
-   **Expert-Level Options**: Select detailed photography/videography techniques from menus, such as camera angles, lenses, lighting, and color grading, to reflect them in your prompts.
-   **Automatic Negative Prompts**: Automatically generates negative prompts by style to prevent image quality degradation factors.
-   **Custom Instructions**: Add your specific styles or requirements to `custom_instructions` to control prompt generation.

## 🛠 Installation

1.  **Clone the Repository**: Navigate to your ComfyUI's `custom_nodes` directory and clone the project:
    ```bash
    cd /path/to/ComfyUI/custom_nodes
    git clone https://github.com/your-repo-path/korean_prompt_engineer.git
    ```
    *(Note: Replace `your-repo-path` with the actual repository URL.)*

2.  **Install Dependencies**: Change into the newly created directory and install the required Python packages:
    ```bash
    cd korean_prompt_engineer
    pip install -r requirements.txt
    ```

3.  **Restart ComfyUI**: Fully shut down and restart ComfyUI for the node to load correctly.

## 📁 Project Structure

The main directory and file structure of the project is as follows:

```
korean_prompt_engineer/
├── __init__.py             # ComfyUI node registration and initialization
├── .env.example            # Example environment variable settings file
├── .gitignore              # Git version control exclusion file
├── cache_manager.py        # Cache management logic
├── exceptions.py           # Custom exception handling
├── LICENSE                 # MIT License information
├── llm_manager.py          # LLM provider management and calls
├── logger.py               # Logging configuration
├── nodes.py                # ComfyUI custom node definitions
├── presets.py              # Preset data used for prompt generation
├── prompt_engineer.py      # Core prompt generation logic
├── README.md               # Project description (this file)
├── requirements.txt        # Python dependency list
├── templates.py            # Prompt template definitions
├── utils.py                # Collection of utility functions
└── llm_providers/          # LLM provider modules
    ├── __init__.py         # Provider package initialization
    ├── base.py             # Base provider interface
    ├── claude_provider.py  # Anthropic Claude provider implementation
    ├── gemini_provider.py  # Google Gemini provider implementation
    ├── ollama_provider.py  # Ollama provider implementation
    └── openai_provider.py  # OpenAI provider implementation
```

## ⚙️ Initial Setup: API Key and LLM Provider Integration

To use this node, you need at least one LLM service API key.

1.  **Create `.env` file**: Copy the `.env.example` file in the project root directory to create a `.env` file.
    ```bash
    cp .env.example .env
    ```

2.  **Enter API Keys and Model Names**: Open the created `.env` file and enter the API keys and model names for the LLM services you wish to use. Services you are not using can be left blank or commented out.

    **Supported LLM Providers and Configuration Examples:**

    *   **OpenAI**:
        ```ini
        OPENAI_API_KEY="sk-..."
        OPENAI_MODEL_NAME="gpt-4-turbo" # or gpt-3.5-turbo, etc.
        ```
    *   **Anthropic (Claude)**:
        ```ini
        ANTHROPIC_API_KEY="sk-ant-..."
        ANTHROPIC_MODEL_NAME="claude-3-opus-20240229" # or claude-3-sonnet-20240229, etc.
        ```
    *   **Google (Gemini)**:
        ```ini
        GEMINI_API_KEY="AIza..."
        GEMINI_MODEL_NAME="gemini-1.5-flash" # or gemini-1.5-pro, etc.
        ```
    *   **Ollama**:
        ```ini
        OLLAMA_BASE_URL="http://localhost:11434" # Ollama server URL
        OLLAMA_MODEL_NAME="llama3" # Model name installed locally
        ```
    *   **Note**: The `provider_name` must match the name selected in the ComfyUI node. (e.g., `openai`, `anthropic`, `gemini`, `ollama`)

## 🚀 How to Use in ComfyUI

1.  **Add Node**: In the ComfyUI workflow, right-click and select `Add Node` > `conditioning/prompt` > `Korean Prompt Engineer 🇰🇷` to add the node.

2.  **Set Input Values**:
    -   **`korean_prompt`**: Freely write your image idea in Korean. (e.g., `사이버펑크 고양이가 미래 도시의 밤거리를 걷는 모습`)
    -   **`provider_name`**: Select the LLM service to use for prompt generation. (e.g., `openai`, `anthropic`, `gemini`, `ollama`). This name must match the service configured in your `.env` file.
    -   **Various Options (Camera, Lighting, etc.)**: Select various photography/videography techniques from the dropdown menus to match your desired style and atmosphere.
    -   **`custom_instructions`**: Write any special instructions you want to include in the prompt in English. (e.g., `in the style of Blade Runner 2049`)

3.  **Connect Outputs**:
    -   **`positive_text`**: Connect the generated positive prompt to the `text` input of a `CLIP Text Encode` node.
    -   **`negative_text`**: Connect the generated negative prompt to the `text` input of a separate `CLIP Text Encode` node.

### 🎨 Node Parameter Details

| Parameter Name | Description | Selection Options (Example) |
| --- | --- | --- |
| `korean_prompt` | Korean text containing the image idea | (Free input) |
| `provider_name` | Name of the LLM service to use | `openai`, `anthropic`, `gemini`, `ollama` (dropdown selection) |
| `Camera Angle` | Camera shooting angle | `front` (정면), `3/4_angle` (3/4 각도), `profile` (측면), `overhead` (오버헤드), `low_angle` (로우 앵글), `dutch_angle` (더치 앵글) |
| `Camera Lens` | Type of camera lens | `24mm` (초광각), `35mm` (광각), `50mm` (표준), `85mm` (망원), `135mm` (장망원), `macro` (접사) |
| `Lighting Setup` | Lighting style | `studio` (스튜디오 조명), `cinematic` (시네마틱 조명), `natural` (자연광), `golden_hour` (골든 아워), `backlit` (역광), `rim_lighting` (림 라이팅), `chiaroscuro` (키아로스쿠로), `neon` (네온 조명) |
| `Mood/Atmosphere` | Overall mood | `dramatic` (극적인), `moody` (음울한), `bright_cheerful` (밝고 쾌활한), `melancholic` (멜랑콜리한), `mysterious` (신비로운), `romantic` (낭만적인), `dystopian` (디스토피아적인), `ethereal` (영묘한) |
| `Color Grade` | Color grading style | `vibrant` (생생한), `desaturated` (채도 낮은), `warm_tones` (따뜻한 톤), `cool_tones` (차가운 톤), `monochrome` (흑백), `duotone` (듀오톤), `cinematic_color` (시네마틱 색감) |
| `Composition` | Composition technique | `centered` (중앙 구도), `rule_of_thirds` (삼분할 구도), `leading_lines` (리딩 라인), `depth_layers` (깊이 레이어), `symmetrical` (대칭 구도), `diagonal` (대각선 구도) |
| `Quality Settings` | Image quality related keywords | `ultra_detailed` (초고화질), `high_quality` (고품질), `professional` (전문적인), `cinematic_quality` (필름 미학) |
| `Negative Prompt Style` | Intensity/style of negative prompt | `standard` (저품질, 아티팩트 제거), `strict` (자연스러운 외관 강조), `minimal` (주요 결함에만 집중) |
| `temperature` | LLM creativity (higher for more diversity) | 0.0 ~ 2.0 |
| `max_tokens` | Maximum length of the generated prompt | 100 ~ 2000 |
| `custom_instructions` | User-defined additional instructions (English) | (Free input) |

## 📜 License

This project is distributed under the [MIT License](LICENSE).
# ComfyUI-Korean-Prompt-Engineer-with-LLM
