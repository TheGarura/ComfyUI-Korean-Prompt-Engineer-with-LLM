# 🌟 ComfyUI 한국어 프롬프트 엔지니어 (Korean Prompt Engineer with LLM)

안녕하세요! ComfyUI를 사용하시는 여러분을 위한 특별한 노드를 소개합니다. 이 노드는 여러분이 **한국어로 상상하는 모든 것을 멋진 이미지로 만들어 줄 수 있도록 도와주는 도구**입니다. 코딩이나 복잡한 설정 없이도, 마치 전문가처럼 상세하고 멋진 영어 프롬프트를 자동으로 만들어줍니다.

**어떤 분들에게 좋을까요?**
*   ComfyUI를 처음 사용하시거나, 프롬프트 작성이 어려우신 분
*   한국어로 편하게 아이디어를 입력하고 싶으신 분
*   전문적인 사진/영상 기법을 프롬프트에 쉽게 적용하고 싶으신 분
*   다양한 AI 모델(Stable Diffusion 등)에 최적화된 프롬프트를 원하시는 분

이 노드는 여러분의 창의력을 최대한 발휘할 수 있도록 도와줄 것입니다!

![버전](https://img.shields.io/badge/version-0.1.0-blue)
![라이선스](https://img.shields.io/badge/license-MIT-green)
![개발자](https://img.shields.io/badge/developer-GARURA-orange)

## 🚀 주요 기능 (이 노드가 할 수 있는 일)

*   **한국어로 편하게 입력**: 여러분이 생각하는 이미지 아이디어를 한국어로 자유롭게 입력하세요. 이 노드가 알아서 전문적인 영어 프롬프트로 번역하고 확장해줍니다.
*   **다양한 AI 언어 모델(LLM) 지원**: OpenAI (GPT), Anthropic (Claude), Google (Gemini), Ollama 등 여러 인공지능 언어 모델 중에서 원하는 것을 선택하여 프롬프트를 만들 수 있습니다. 마치 여러 명의 똑똑한 비서 중에서 한 명을 고르는 것과 같아요!
*   **전문가처럼 상세한 옵션**: 카메라 앵글, 렌즈, 조명, 색감, 구도 등 전문 사진작가나 영상 감독이 사용하는 기법들을 메뉴에서 쉽게 선택할 수 있습니다. 복잡한 용어를 몰라도 멋진 효과를 낼 수 있습니다.
*   **자동으로 나쁜 프롬프트 제거**: 이미지 품질을 떨어뜨릴 수 있는 요소들(예: 흐릿함, 깨진 이미지)을 자동으로 걸러주는 '네거티브 프롬프트'를 만들어줍니다. 여러분은 좋은 이미지를 만드는 데만 집중하세요!
*   **나만의 스타일 추가**: `custom_instructions`라는 곳에 여러분만의 특별한 지시사항(예: 특정 화풍, 분위기)을 영어로 추가하여 프롬프트 생성에 반영할 수 있습니다.

## 🛠 설치 방법 (노드를 ComfyUI에 추가하기)

이 노드를 여러분의 ComfyUI에서 사용하려면 몇 가지 간단한 설치 과정이 필요합니다. 코딩을 몰라도 괜찮아요! 아래 단계를 천천히 따라오시면 됩니다.

1.  **ComfyUI 설치 폴더 찾기**:
    *   먼저, 여러분의 컴퓨터에 ComfyUI가 어디에 설치되어 있는지 알아야 합니다. 보통 `C:\ComfyUI` (Windows) 또는 `~/ComfyUI` (macOS/Linux)와 같은 곳에 있습니다.
    *   이 폴더 안에 `custom_nodes`라는 이름의 폴더가 있을 거예요. 이 폴더가 우리가 노드를 설치할 곳입니다.

2.  **터미널(명령 프롬프트) 열기**:
    *   **Windows**: 시작 메뉴에서 `cmd` 또는 `PowerShell`을 검색하여 실행합니다.
    *   **macOS/Linux**: `터미널` 앱을 실행합니다.
    *   터미널은 컴퓨터에 명령을 내리는 검은색(또는 흰색) 창입니다.

3.  **`custom_nodes` 폴더로 이동하기**:
    *   터미널에 다음 명령어를 입력하고 `Enter` 키를 누르세요.
    *   **주의**: `/path/to/ComfyUI` 부분은 여러분의 실제 ComfyUI 설치 경로로 바꿔야 합니다.
    ```bash
    cd /path/to/ComfyUI/custom_nodes
    ```
    *   **예시**: 만약 ComfyUI가 `C:\Users\YourName\ComfyUI`에 있다면, `cd C:\Users\YourName\ComfyUI\custom_nodes`라고 입력합니다.

4.  **노드 파일 다운로드 (복제)**:
    *   이제 `custom_nodes` 폴더 안에서 다음 명령어를 입력하고 `Enter` 키를 누르세요.
    ```bash
    git clone https://github.com/TheGarura/ComfyUI-Korean-Prompt-Engineer-with-LLM.git
    ```
    *   이 명령어는 인터넷에서 이 노드의 모든 파일을 여러분의 컴퓨터로 가져와 `korean_prompt_engineer`라는 새 폴더를 만듭니다.

5.  **새로 생긴 노드 폴더로 이동**:
    *   다운로드한 노드 폴더 안으로 들어가야 합니다. 다음 명령어를 입력하고 `Enter` 키를 누르세요.
    ```bash
    cd korean_prompt_engineer
    ```

6.  **필요한 도구들 설치**:
    *   이 노드가 작동하려면 몇 가지 추가적인 프로그램(Python 패키지)이 필요합니다. 다음 명령어를 입력하고 `Enter` 키를 누르세요.
    ```bash
    pip install -r requirements.txt
    ```
    *   이 과정은 인터넷 연결이 필요하며, 잠시 시간이 걸릴 수 있습니다. 화면에 여러 메시지가 나타나도 걱정하지 마세요.

7.  **ComfyUI 재시작**:
    *   모든 설치가 끝났습니다! 이제 ComfyUI 프로그램을 완전히 껐다가 다시 실행해주세요. 그래야 새로 설치된 노드를 ComfyUI가 인식하고 사용할 수 있습니다.

## 🔄 업데이트 방법 (새로운 기능이나 버그 수정 시)

이 노드에 새로운 기능이 추가되거나 버그가 수정되었을 때, 여러분의 ComfyUI에 최신 버전을 적용하는 방법입니다.

1.  **ComfyUI 종료**: 먼저 ComfyUI 프로그램을 완전히 종료해주세요.
2.  **노드 디렉토리로 이동**: 터미널(명령 프롬프트)을 열고, 이 노드가 설치된 디렉토리로 이동합니다.
    ```bash
    cd /path/to/ComfyUI/custom_nodes/korean_prompt_engineer
    ```
    (여기서 `/path/to/ComfyUI`는 여러분의 ComfyUI가 설치된 실제 경로입니다. 예를 들어, `C:\ComfyUI`나 `~/ComfyUI`와 같을 수 있습니다.)
3.  **최신 버전 다운로드**: 다음 명령어를 입력하여 최신 변경사항을 다운로드합니다.
    ```bash
    git pull
    ```
    이 명령어는 인터넷에서 최신 코드를 가져와 현재 설치된 노드를 업데이트해줍니다.
4.  **ComfyUI 재시작**: 업데이트가 완료되면 ComfyUI를 다시 시작하여 변경사항을 적용합니다.

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

## ⚙️ 초기 설정: AI 언어 모델(LLM) 연결하기 (API 키 설정)

이 노드는 여러분이 입력한 한국어 프롬프트를 영어로 번역하고 확장하기 위해 인공지능 언어 모델(LLM)의 도움을 받습니다. 따라서, 여러분이 사용하고 싶은 LLM 서비스(예: OpenAI, Google Gemini 등)의 **API 키**를 설정해주어야 합니다. API 키는 해당 서비스에 접근할 수 있는 비밀번호와 같습니다.

1.  **`.env` 파일 만들기**:
    *   이 노드 폴더(`korean_prompt_engineer`) 안에 `.env.example`이라는 파일이 있습니다. 이 파일을 복사해서 **`.env`**라는 이름으로 바꿔주세요. (파일 확장자가 없는 파일입니다.)
    *   **Windows**: 파일 탐색기에서 `.env.example`을 복사한 후, 이름을 `.env`로 변경합니다.
    *   **macOS/Linux**: 터미널에서 다음 명령어를 입력하고 `Enter` 키를 누르세요.
        ```bash
        cp .env.example .env
        ```
    *   `.env` 파일은 여러분의 API 키와 같은 중요한 정보를 안전하게 보관하는 역할을 합니다.

2.  **API 키와 모델 이름 입력하기**:
    *   이제 방금 만든 `.env` 파일을 메모장(Windows)이나 텍스트 편집기(macOS) 등으로 열어주세요.
    *   파일 안에는 다음과 같은 내용이 보일 것입니다.
        ```ini
        # OpenAI (ChatGPT 개발사)
        # OPENAI_API_KEY=""
        # OPENAI_MODEL_NAME="gpt-4-turbo"

        # Anthropic (Claude 개발사)
        # ANTHROPIC_API_KEY=""
        # ANTHROPIC_MODEL_NAME="claude-3-opus-20240229"

        # Google (Gemini 개발사)
        # GEMINI_API_KEY=""
        # GEMINI_MODEL_NAME="gemini-1.5-flash"

        # Ollama (로컬에서 AI 모델 실행)
        # OLLAMA_BASE_URL="http://localhost:11434"
        # OLLAMA_MODEL_NAME="llama3"
        ```
    *   여러분은 이 중에서 사용하고 싶은 LLM 서비스의 줄에 있는 `#` (주석)을 지우고, `""` 안에 여러분의 API 키와 모델 이름을 입력해야 합니다.
    *   **예시: OpenAI를 사용하고 싶다면**
        *   OpenAI 웹사이트에서 API 키를 발급받으세요. (보통 `sk-...`로 시작합니다.)
        *   `.env` 파일을 다음과 같이 수정합니다.
            ```ini
            OPENAI_API_KEY="여러분의_OPENAI_API_키를_여기에_붙여넣으세요"
            OPENAI_MODEL_NAME="gpt-4-turbo" # 또는 gpt-3.5-turbo 등, 사용하고 싶은 모델 이름
            ```
    *   **다른 LLM 서비스도 마찬가지**: Anthropic (Claude), Google (Gemini), Ollama 등 다른 서비스를 사용하고 싶다면 해당 서비스의 API 키를 발급받아 같은 방식으로 입력합니다.
    *   **중요**: 사용하지 않는 서비스는 `#`을 그대로 두거나 줄을 지워도 됩니다. 최소한 하나 이상의 서비스 API 키를 정확히 입력해야 노드가 작동합니다.
    *   **참고**: `provider_name`은 ComfyUI 노드에서 선택하는 이름(예: `openai`, `anthropic`, `gemini`, `ollama`)과 정확히 일치해야 합니다.

3.  **파일 저장**: `.env` 파일을 수정한 후 반드시 저장해주세요.

## 🚀 ComfyUI에서 노드 사용하기 (워크플로우에 추가하고 설정하기)

이제 ComfyUI에서 이 노드를 실제로 사용하는 방법을 알아볼까요? 아주 쉽습니다!

1.  **노드 추가하기**:
    *   ComfyUI 작업 화면의 빈 공간에서 마우스 오른쪽 버튼을 클릭하세요.
    *   메뉴가 나타나면 `Add Node` (노드 추가)를 선택합니다.
    *   그다음 `conditioning/prompt` (컨디셔닝/프롬프트)를 선택하고, 마지막으로 `Korean Prompt Engineer 🇰🇷`를 클릭하여 노드를 추가합니다.
    *   (화면에 새로운 노드 상자가 나타날 거예요!)

2.  **입력값 설정하기 (노드에 정보 주기)**:
    *   추가된 `Korean Prompt Engineer 🇰🇷` 노드를 보면 여러 가지 설정할 수 있는 부분이 있습니다.
    *   **`한국어 프롬프트`**: 여기에 여러분이 만들고 싶은 이미지에 대한 아이디어를 한국어로 자유롭게 적어주세요. 예를 들어, `미래 도시의 밤거리를 걷는 사이버펑크 고양이`처럼요.
    *   **`LLM 프로바이더`**: 드롭다운 메뉴를 클릭하여 `.env` 파일에 설정했던 AI 언어 모델(예: `openai`, `anthropic`, `gemini`, `ollama`) 중 하나를 선택합니다.
    *   **각종 옵션 (카메라 앵글, 조명 설정 등)**: 원하는 이미지의 스타일과 분위기에 맞춰 드롭다운 메뉴에서 다양한 사진/영상 기법을 선택하세요. 어떤 옵션을 선택하느냐에 따라 이미지가 크게 달라질 수 있습니다!
    *   **`사용자 정의 지침 (영문)`**: 만약 프롬프트에 꼭 포함하고 싶은 특별한 지시사항이 있다면, 여기에 영어로 작성합니다. 예를 들어, `in the style of Blade Runner 2049` (블레이드 러너 2049 스타일로)와 같이요.

3.  **출력 연결하기 (다른 노드와 연결)**:
    *   이 노드는 두 가지 중요한 결과(`positive_text`와 `negative_text`)를 만들어냅니다. 이 결과들을 다른 노드에 연결해야 이미지를 생성할 수 있습니다.
    *   **`positive_text`**: 이 노드의 `positive_text` 출력 부분을 마우스로 드래그하여, 보통 `CLIP Text Encode` 노드의 `text` 입력 부분에 연결합니다. (이것이 여러분이 원하는 이미지를 만드는 데 사용될 긍정적인 프롬프트입니다.)
    *   **`negative_text`**: 이 노드의 `negative_text` 출력 부분도 마찬가지로 다른 `CLIP Text Encode` 노드의 `text` 입력 부분에 연결합니다. (이것은 이미지에서 피하고 싶은 요소들을 알려주는 부정적인 프롬프트입니다.)

### 🎨 노드 파라미터 상세 설명 (각 설정의 의미)

| 파라미터명 | 설명 (무엇을 설정하는 건가요?) | 선택 옵션 (예시) |
| --- | --- | --- |
| `한국어 프롬프트` | 여러분이 만들고 싶은 이미지의 핵심 아이디어를 한국어로 입력하는 곳입니다. | (자유롭게 입력) |
| `LLM 프로바이더` | 프롬프트 번역 및 확장에 사용할 인공지능 언어 모델을 선택합니다. `.env` 파일에 설정한 이름과 같아야 해요. | `openai`, `anthropic`, `gemini`, `ollama` (드롭다운 메뉴에서 선택) |
| `카메라 앵글` | 이미지를 어떤 각도에서 찍을지 결정합니다. | `정면` (front-facing), `3/4 각도` (three-quarter view), `측면` (side profile), `오버헤드` (top-down), `로우 앵글` (looking upward), `더치 앵글` (diagonal horizon) |
| `카메라 렌즈` | 어떤 종류의 카메라 렌즈로 찍은 듯한 효과를 낼지 선택합니다. | `24mm (초광각)` (ultra-wide), `35mm (광각)` (standard-wide), `50mm (표준)` (standard prime), `85mm (망원)` (telephoto prime), `135mm (장망원)` (telephoto), `매크로 (접사)` (extreme close-up) |
| `조명 설정` | 이미지의 전체적인 조명 분위기를 결정합니다. | `스튜디오 조명` (professional studio lighting), `시네마틱 조명` (dramatic shadows), `자연광` (soft diffused daylight), `골든 아워` (sunset/sunrise), `역광` (silhouette effect), `림 라이팅` (edge highlighting), `키아로스쿠로` (strong contrast), `네온 조명` (cyberpunk atmosphere) |
| `무드/분위기` | 이미지의 전체적인 감성이나 분위기를 설정합니다. | `극적인` (strong emotions), `음울한` (dark, mysterious), `밝고 쾌활한` (hopeful, vibrant), `멜랑콜리한` (sentimental, bittersweet), `신비로운` (enigmatic, unexplained), `낭만적인` (love, warm feelings), `디스토피아적인` (bleak, futuristic pessimism), `영묘한` (otherworldly, dreamlike) |
| `색감 보정` | 이미지의 색상 스타일을 조절합니다. | `생생한` (saturated hues), `채도 낮은` (reduced color intensity), `따뜻한 톤` (golden, orange tint), `차가운 톤` (blueish hue), `흑백` (black and white), `듀오톤` (two color grading), `시네마틱 색감` (film-like appearance) |
| `구도` | 이미지의 구성 방식을 결정합니다. | `중앙 구도` (focal point in middle), `삼분할 구도` (balanced proportions), `리딩 라인` (guiding the eye), `깊이 레이어` (foreground/background separation), `대칭 구도` (balanced elements), `대각선 구도` (dynamic movement) |
| `화질 설정` | 이미지의 품질과 관련된 키워드를 추가합니다. | `초고화질` (highest resolution), `고품질` (optimized performance), `전문적인` (commercial finish), `시네마틱 품질` (film aesthetics) |
| `네거티브 프롬프트 스타일` | 이미지에서 피하고 싶은 요소들을 어떤 방식으로 제거할지 선택합니다. | `표준` (저품질, 아티팩트 제거), `엄격한` (자연스러운 외관 강조), `최소한의` (주요 결함에만 집중) |
| `창의성 (Temperature)` | LLM이 프롬프트를 얼마나 자유롭고 다양하게 만들지 조절합니다. 숫자가 높을수록 더 창의적입니다. | 0.0 ~ 2.0 사이의 숫자 |
| `최대 토큰 수` | 생성될 영어 프롬프트의 최대 길이를 제한합니다. | 100 ~ 2000 사이의 숫자 |
| `사용자 정의 지침 (영문)` | 여러분이 LLM에게 주고 싶은 특별한 추가 지시사항을 영어로 작성합니다. | (자유롭게 입력) |

## ❓ 문의하기 (궁금한 점이 있다면)

노드를 사용하시다가 궁금한 점이나 문제가 발생하면 언제든지 개발자에게 문의해주세요! 여러분의 피드백은 이 노드를 더 좋게 만드는 데 큰 도움이 됩니다.

*   **개발자 이메일**: `thegarura21@gmail.com`

**문의하실 때 다음 정보를 함께 알려주시면 더 빠르게 도와드릴 수 있습니다.**

*   **사용 중인 ComfyUI 버전**: (예: ComfyUI 2024-01-01 버전)
*   **운영체제**: (예: Windows 10, macOS Sonoma, Ubuntu 22.04)
*   **문제 발생 시점**: (예: 노드 설치 중, `.env` 파일 설정 후, 노드 실행 시)
*   **발생한 오류 메시지**: (터미널이나 ComfyUI 화면에 나타난 오류 메시지를 그대로 복사해서 붙여넣어 주세요. 스크린샷도 좋습니다!)
*   **시도해본 해결 방법**: (문제를 해결하기 위해 어떤 시도를 해보셨는지 알려주세요.)
*   **기타 관련 정보**: (문제를 재현할 수 있는 워크플로우 파일, 사용 중인 LLM 프로바이더 등)

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
    git clone https://github.com/TheGarura/ComfyUI-Korean-Prompt-Engineer-with-LLM.git
    ```

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
