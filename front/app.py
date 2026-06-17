import base64
import json
import mimetypes
from pathlib import Path

import streamlit as st


# =========================================================
# 기본 설정
# =========================================================

st.set_page_config(
    page_title="Find Your Hero",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

FRONT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = FRONT_DIR / "assets"

BACKGROUND_PATH = ASSETS_DIR / "backgrounds" / "home_background.png"
SYMBOL_PATH = ASSETS_DIR / "logos" / "overwatch_symbol.png"
WORDMARK_PATH = ASSETS_DIR / "logos" / "overwatch_wordmark.png"
CHARACTER_PATH = ASSETS_DIR / "heroes" / "character.png"

ROLE_TANK_ICON_PATH = ASSETS_DIR / "icons" / "role_tank.png"
ROLE_DAMAGE_ICON_PATH = ASSETS_DIR / "icons" / "role_damage.png"
ROLE_SUPPORT_ICON_PATH = ASSETS_DIR / "icons" / "role_support.png"
ROLE_FLEX_ICON_PATH = ASSETS_DIR / "icons" / "role_flex.png"

ARROW_LEFT_GRAY_PATH = ASSETS_DIR / "icons" / "arrow_left_gray.png"
ARROW_LEFT_WHITE_PATH = ASSETS_DIR / "icons" / "arrow_left_white.png"
ARROW_LEFT_ORANGE_PATH = ASSETS_DIR / "icons" / "arrow_left_orange.png"
ARROW_RIGHT_GRAY_PATH = ASSETS_DIR / "icons" / "arrow_right_gray.png"
ARROW_RIGHT_WHITE_PATH = ASSETS_DIR / "icons" / "arrow_right_white.png"
ARROW_RIGHT_ORANGE_PATH = ASSETS_DIR / "icons" / "arrow_right_orange.png"

STUDENT_INFO = "2023204017 최유진"


# =========================================================
# 이미지 처리
# =========================================================

@st.cache_data(show_spinner=False)
def image_to_data_uri(image_path: Path) -> str:
    """로컬 이미지를 Custom Component에서 사용할 Data URI로 변환합니다."""
    if not image_path.exists():
        st.error(
            "이미지 파일을 찾을 수 없습니다.\n\n"
            f"`{image_path}`"
        )
        st.stop()

    mime_type, _ = mimetypes.guess_type(image_path.name)
    mime_type = mime_type or "image/png"

    encoded_image = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded_image}"


# =========================================================
# Streamlit 기본 UI 숨기기
# =========================================================

def hide_streamlit_interface() -> None:
    st.html(
        """
        <style>
            html,
            body {
                margin: 0 !important;
                padding: 0 !important;
                width: 100% !important;
                height: 100% !important;
                overflow: hidden !important;
                background: #0a1420 !important;
            }

            [data-testid="stAppViewContainer"],
            [data-testid="stMain"] {
                width: 100% !important;
                height: 100% !important;
                overflow: hidden !important;
                background: #0a1420 !important;
            }

            [data-testid="stAppViewBlockContainer"],
            .block-container {
                max-width: none !important;
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }

            [data-testid="stHeader"],
            [data-testid="stToolbar"],
            [data-testid="stDecoration"],
            [data-testid="stStatusWidget"],
            #MainMenu,
            footer {
                display: none !important;
                visibility: hidden !important;
            }

            .stApp {
                margin: 0 !important;
                padding: 0 !important;
                overflow: hidden !important;
            }
        </style>
        """
    )


# =========================================================
# 이미지 Data URI 준비
# =========================================================

BACKGROUND_URI = image_to_data_uri(BACKGROUND_PATH)
SYMBOL_URI = image_to_data_uri(SYMBOL_PATH)
WORDMARK_URI = image_to_data_uri(WORDMARK_PATH)
CHARACTER_URI = image_to_data_uri(CHARACTER_PATH)

ROLE_TANK_ICON_URI = image_to_data_uri(ROLE_TANK_ICON_PATH)
ROLE_DAMAGE_ICON_URI = image_to_data_uri(ROLE_DAMAGE_ICON_PATH)
ROLE_SUPPORT_ICON_URI = image_to_data_uri(ROLE_SUPPORT_ICON_PATH)
ROLE_FLEX_ICON_URI = image_to_data_uri(ROLE_FLEX_ICON_PATH)

ARROW_LEFT_GRAY_URI = image_to_data_uri(ARROW_LEFT_GRAY_PATH)
ARROW_LEFT_WHITE_URI = image_to_data_uri(ARROW_LEFT_WHITE_PATH)
ARROW_LEFT_ORANGE_URI = image_to_data_uri(ARROW_LEFT_ORANGE_PATH)
ARROW_RIGHT_GRAY_URI = image_to_data_uri(ARROW_RIGHT_GRAY_PATH)
ARROW_RIGHT_WHITE_URI = image_to_data_uri(ARROW_RIGHT_WHITE_PATH)
ARROW_RIGHT_ORANGE_URI = image_to_data_uri(ARROW_RIGHT_ORANGE_PATH)


# =========================================================
# Custom Component HTML
# =========================================================

APP_HTML = f"""
<main id="ow-app" data-screen="home">
    <img
        class="background-image"
        src="{BACKGROUND_URI}"
        alt=""
        draggable="false"
        aria-hidden="true"
    />
    <div class="background-shade" aria-hidden="true"></div>

    <img
        class="character-image"
        src="{CHARACTER_URI}"
        alt="오버워치 캐릭터"
        draggable="false"
    />

    <header class="app-header">
        <button
            id="home-button"
            class="brand-button"
            type="button"
            aria-label="홈으로 이동"
        >
            <img
                class="brand-symbol"
                src="{SYMBOL_URI}"
                alt=""
                draggable="false"
            />
            <span class="brand-title">Open Source Software</span>
        </button>

        <div class="student-badge">
            {STUDENT_INFO}
        </div>
    </header>

    <section id="home-screen" class="screen home-screen active">
        <img
            class="home-wordmark"
            src="{WORDMARK_URI}"
            alt="Overwatch"
            draggable="false"
        />

        <h1 class="home-title">Find Your Hero</h1>

        <p class="home-description">
            당신의 플레이 스타일에 가장 잘 맞는 영웅을 찾아보세요
        </p>

        <button
            id="home-start-button"
            class="orange-button home-start-button"
            type="button"
        >
            지금 시작하기
        </button>
    </section>

    <section id="welcome-screen" class="screen welcome-screen">
        <div class="welcome-copy">
            <h1 class="welcome-title">
                안녕, 친구!<br />
                오버워치 세계에 온 걸 환영해.
            </h1>

            <p class="welcome-description">
                전장으로 나가기 전 영웅 선택은 필수야<br />
                너에게 딱 맞는 영웅을 찾아보자
            </p>
        </div>

        <button
            id="welcome-start-button"
            class="orange-button welcome-start-button"
            type="button"
        >
            시작하기
        </button>
    </section>

    <section id="quiz-screen" class="screen quiz-screen">
        <div id="question-viewport" class="question-viewport">
            <article id="question-1" class="question-panel question-one-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q1.</span>
                        <span>선호 역할</span>
                    </h1>

                    <p class="question-description">
                        어떤 역할로 팀에 기여하고 싶나요?
                    </p>
                </div>

                <div class="role-grid" role="radiogroup" aria-label="선호 역할">
                    <button
                        class="role-card"
                        type="button"
                        data-role="tank"
                        role="radio"
                        aria-checked="false"
                    >
                        <span class="role-icon-circle">
                            <img
                                class="role-icon"
                                src="{ROLE_TANK_ICON_URI}"
                                alt=""
                                draggable="false"
                            />
                        </span>
                        <strong class="role-card-title">TANK</strong>
                        <span class="role-card-description">
                            전방에서 팀을 이끌어요
                        </span>
                    </button>

                    <button
                        class="role-card"
                        type="button"
                        data-role="damage"
                        role="radio"
                        aria-checked="false"
                    >
                        <span class="role-icon-circle">
                            <img
                                class="role-icon"
                                src="{ROLE_DAMAGE_ICON_URI}"
                                alt=""
                                draggable="false"
                            />
                        </span>
                        <strong class="role-card-title">DAMAGE</strong>
                        <span class="role-card-description">
                            적을 직접 처치해요
                        </span>
                    </button>

                    <button
                        class="role-card"
                        type="button"
                        data-role="support"
                        role="radio"
                        aria-checked="false"
                    >
                        <span class="role-icon-circle">
                            <img
                                class="role-icon"
                                src="{ROLE_SUPPORT_ICON_URI}"
                                alt=""
                                draggable="false"
                            />
                        </span>
                        <strong class="role-card-title">SUPPORT</strong>
                        <span class="role-card-description">
                            팀원을 치유하고 강화해요
                        </span>
                    </button>

                    <button
                        class="role-card"
                        type="button"
                        data-role="flex"
                        role="radio"
                        aria-checked="false"
                    >
                        <span class="role-icon-circle">
                            <img
                                class="role-icon"
                                src="{ROLE_FLEX_ICON_URI}"
                                alt=""
                                draggable="false"
                            />
                        </span>
                        <strong class="role-card-title">NOT SURE</strong>
                        <span class="role-card-description">
                            잘 모르겠어요
                        </span>
                    </button>
                </div>
            </article>

            <!-- Q2. 선호 교전 거리 질문 -->
            <article id="question-2" class="question-panel question-two-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q2.</span>
                        <span>선호 교전 거리</span>
                    </h1>

                    <p class="question-description">
                        어느 거리에서 싸우는 것이 가장 편한가요?
                    </p>
                </div>

                <div
                    class="range-answer"
                    role="group"
                    aria-label="선호 교전 거리"
                >
                    <div class="range-label-row">
                        <button
                            class="range-option"
                            type="button"
                            data-range="1"
                            aria-pressed="false"
                        >
                            단거리
                        </button>

                        <button
                            class="range-option"
                            type="button"
                            data-range="3"
                            aria-pressed="false"
                        >
                            중거리
                        </button>

                        <button
                            class="range-option"
                            type="button"
                            data-range="5"
                            aria-pressed="false"
                        >
                            장거리
                        </button>
                    </div>

                    <div class="range-slider-wrapper">
                        <input
                            id="range-slider"
                            class="range-slider"
                            type="range"
                            min="1"
                            max="5"
                            step="2"
                            value="3"
                            aria-label="선호 교전 거리 선택"
                            aria-valuetext="선택하지 않음"
                        />
                    </div>

                    <div class="range-description-row">
                        <span>적에게 가까이 접근해서 싸워요</span>
                        <span>적당한 거리를 유지하며 싸워요</span>
                        <span>멀리서 안전하게 공격해요</span>
                    </div>
                </div>
            </article>

            <!-- Q3. 조준 자신감 질문 -->
            <article id="question-3" class="question-panel question-three-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q3.</span>
                        <span>조준 자신감</span>
                    </h1>

                    <p class="question-description">
                        정확한 조준에 얼마나 자신이 있나요?
                    </p>
                </div>

                <div
                    class="range-answer aim-answer"
                    role="group"
                    aria-label="조준 실력"
                >
                    <div class="range-label-row aim-label-row">
                        <button
                            class="range-option aim-option"
                            type="button"
                            data-aim="1"
                            aria-pressed="false"
                        >
                            조준 실력 낮음
                        </button>

                        <button
                            class="range-option aim-option"
                            type="button"
                            data-aim="5"
                            aria-pressed="false"
                        >
                            조준 실력 높음
                        </button>
                    </div>

                    <div class="range-slider-wrapper">
                        <input
                            id="aim-slider"
                            class="range-slider aim-slider"
                            type="range"
                            min="1"
                            max="5"
                            step="1"
                            value="3"
                            aria-label="조준 자신감 선택"
                            aria-valuetext="선택하지 않음"
                        />
                    </div>
                </div>
            </article>

            <!-- Q4. 기동성 선호도 질문 -->
            <article id="question-4" class="question-panel question-four-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q4.</span>
                        <span>기동성 선호도</span>
                    </h1>

                    <p class="question-description">
                        빠르게 이동하며 전장을 누비는 플레이를 좋아하나요?
                    </p>
                </div>

                <div
                    class="range-answer mobility-answer"
                    role="group"
                    aria-label="기동성 선호도"
                >
                    <div class="range-label-row mobility-label-row">
                        <button
                            class="range-option mobility-option"
                            type="button"
                            data-mobility="1"
                            aria-pressed="false"
                        >
                            안전 위치 유지
                        </button>

                        <button
                            class="range-option mobility-option"
                            type="button"
                            data-mobility="5"
                            aria-pressed="false"
                        >
                            빠른 전진 침투
                        </button>
                    </div>

                    <div class="range-slider-wrapper">
                        <input
                            id="mobility-slider"
                            class="range-slider mobility-slider"
                            type="range"
                            min="1"
                            max="5"
                            step="1"
                            value="3"
                            aria-label="기동성 선호도 선택"
                            aria-valuetext="선택하지 않음"
                        />
                    </div>
                </div>
            </article>

            <!-- Q5. 공격적인 플레이 성향 질문 -->
            <article id="question-5" class="question-panel question-five-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q5.</span>
                        <span>공격적인 플레이 성향</span>
                    </h1>

                    <p class="question-description">
                        얼마나 적극적으로 적에게 진입하고 싶나요?
                    </p>
                </div>

                <div
                    class="range-answer aggression-answer"
                    role="group"
                    aria-label="공격적인 플레이 성향"
                >
                    <div class="range-label-row aggression-label-row">
                        <button
                            class="range-option aggression-option"
                            type="button"
                            data-aggression="1"
                            aria-pressed="false"
                        >
                            신중하고 안정적
                        </button>

                        <button
                            class="range-option aggression-option"
                            type="button"
                            data-aggression="5"
                            aria-pressed="false"
                        >
                            과감하고 공격적
                        </button>
                    </div>

                    <div class="range-slider-wrapper">
                        <input
                            id="aggression-slider"
                            class="range-slider aggression-slider"
                            type="range"
                            min="1"
                            max="5"
                            step="1"
                            value="3"
                            aria-label="공격적인 플레이 성향 선택"
                            aria-valuetext="선택하지 않음"
                        />
                    </div>
                </div>
            </article>
        </div>

        <nav class="quiz-navigation" aria-label="질문 이동">
            <button
                id="previous-question-button"
                class="arrow-button disabled"
                type="button"
                disabled
                aria-label="이전 질문"
            >
                <img
                    class="arrow-single"
                    src="{ARROW_LEFT_GRAY_URI}"
                    alt=""
                    draggable="false"
                />
            </button>

            <div id="progress-dots" class="progress-dots" aria-label="질문 진행도">
                <span class="progress-dot current" data-index="1"></span>
                <span class="progress-dot pending" data-index="2"></span>
                <span class="progress-dot pending" data-index="3"></span>
                <span class="progress-dot pending" data-index="4"></span>
                <span class="progress-dot pending" data-index="5"></span>
                <span class="progress-dot pending" data-index="6"></span>
                <span class="progress-dot pending" data-index="7"></span>
                <span class="progress-dot pending" data-index="8"></span>
            </div>

            <button
                id="next-question-button"
                class="arrow-button disabled"
                type="button"
                disabled
                aria-label="다음 질문"
            >
                <img
                    class="arrow-single"
                    src="{ARROW_RIGHT_GRAY_URI}"
                    alt=""
                    draggable="false"
                />
            </button>
        </nav>
    </section>
</main>
"""


# =========================================================
# Custom Component CSS
# =========================================================

APP_CSS = r"""
:root {
    --accent-orange: #ed6c25;
    --accent-orange-hover: #ff7a2c;
    --accent-yellow: #ffb62e;
    --selected-blue: #4db5fb;
    --header-background: rgba(226, 227, 234, 0.96);
    --white: #ffffff;
    --muted-white: rgba(255, 255, 255, 0.72);
    --screen-dark: rgba(7, 16, 28, 0.89);
}

* {
    box-sizing: border-box;
}

button {
    font: inherit;
    -webkit-appearance: none;
    appearance: none;
    touch-action: manipulation;
}

button,
.orange-button,
.role-card,
.arrow-button,
.brand-button {
    -webkit-tap-highlight-color: transparent;
}

#ow-app {
    position: fixed;
    inset: 0;
    z-index: 99999;

    width: 100vw;
    height: 100vh;

    overflow: hidden;

    color: #ffffff;
    background: #0a1420;

    font-family:
        Arial,
        "Noto Sans KR",
        "Apple SD Gothic Neo",
        sans-serif;
}

.background-image,
.background-shade {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;
}

.background-image {
    z-index: 0;

    display: block;
    object-fit: cover;
    object-position: center center;

    transform: scale(1.002);

    pointer-events: none;
    user-select: none;
}

.background-shade {
    z-index: 1;

    background:
        linear-gradient(
            90deg,
            rgba(28, 49, 70, 0.48) 0%,
            rgba(28, 49, 70, 0.44) 52%,
            rgba(28, 49, 70, 0.38) 100%
        );

    transition:
        background 120ms ease,
        opacity 120ms ease;
}

#ow-app[data-screen="welcome"] .background-shade,
#ow-app[data-screen="quiz"] .background-shade {
    background:
        linear-gradient(
            90deg,
            rgba(7, 16, 28, 0.95) 0%,
            rgba(7, 16, 28, 0.91) 39%,
            rgba(7, 16, 28, 0.81) 68%,
            rgba(7, 16, 28, 0.71) 100%
        );
}

/* ========================================================
   고정 헤더
======================================================== */

.app-header {
    position: absolute;
    z-index: 30;

    top: 2.3vh;
    left: 2.7vw;
    right: 2.7vw;

    height: 10.8vh;
    min-height: 94px;
    max-height: 116px;

    padding: 0 22px 0 30px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background: var(--header-background);
    border-radius: 23px;

    box-shadow:
        0 6px 20px rgba(0, 0, 0, 0.10);

    backdrop-filter: blur(3px);
    -webkit-backdrop-filter: blur(3px);
}

.brand-button {
    display: flex;
    align-items: center;
    gap: 25px;

    margin: 0;
    padding: 0;

    color: #050505;
    background: transparent;
    border: 0;

    cursor: pointer;

    transition:
        opacity 150ms ease,
        transform 150ms ease;
}

.brand-button:hover {
    opacity: 0.82;
}

.brand-button:active {
    transform: scale(0.99);
}

.brand-symbol {
    width: 72px;
    height: 72px;

    flex-shrink: 0;
    object-fit: contain;

    pointer-events: none;
    user-select: none;
}

.brand-title {
    color: #050505;

    font-size: clamp(27px, 1.85vw, 36px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -1.1px;

    white-space: nowrap;
}

.student-badge {
    height: 78px;
    min-width: 312px;

    padding: 0 24px;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #ffffff;
    background: var(--accent-orange);

    border-radius: 16px;

    font-size: clamp(22px, 1.5vw, 30px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -0.7px;

    white-space: nowrap;
}

/* ========================================================
   캐릭터
======================================================== */

.character-image {
    position: absolute;
    z-index: 5;

    right: -0.5vw;
    bottom: -1.3vh;

    width: min(45.5vw, 875px);
    max-height: 89vh;

    object-fit: contain;
    object-position: right bottom;

    opacity: 0;
    transform: translateX(18px) scale(0.992);

    filter:
        drop-shadow(
            -12px 8px 20px
            rgba(0, 0, 0, 0.22)
        );

    transition:
        opacity 150ms ease,
        transform 210ms cubic-bezier(0.22, 1, 0.36, 1);

    pointer-events: none;
    user-select: none;
}

#ow-app[data-screen="welcome"] .character-image,
#ow-app[data-screen="quiz"] .character-image {
    opacity: 1;
    transform: translateX(0) scale(1);
}

/* ========================================================
   화면 공통
======================================================== */

.screen {
    position: absolute;
    inset: 0;
    z-index: 10;

    opacity: 0;
    visibility: hidden;
    pointer-events: none;

    transition:
        opacity 450ms ease,
        visibility 0s linear 450ms;
}

.screen:not(.active),
.screen:not(.active) * {
    pointer-events: none !important;
}

.screen.active {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    z-index: 20;

    transition:
        opacity 500ms ease,
        visibility 0s;
}

.orange-button {
    position: absolute;
    z-index: 24;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #ffffff;
    background: var(--accent-orange);
    border: 0;

    font-weight: 800;
    letter-spacing: -0.8px;

    cursor: pointer;
    pointer-events: auto;

    box-shadow:
        0 12px 28px rgba(0, 0, 0, 0.18);

    transition:
        background-color 90ms ease,
        transform 110ms cubic-bezier(0.22, 1, 0.36, 1),
        box-shadow 90ms ease;
}

.orange-button:hover {
    background: var(--accent-orange-hover);
    transform: translateY(-4px);

    box-shadow:
        0 17px 34px rgba(0, 0, 0, 0.28);
}

.orange-button:active {
    transform: translateY(0) scale(0.985);
}

/* ========================================================
   홈
======================================================== */

.home-wordmark {
    position: absolute;

    top: 24.7vh;
    left: 50%;

    width: min(63vw, 1210px);
    max-height: 155px;

    object-fit: contain;

    transform: translateX(-50%);

    pointer-events: none;
    user-select: none;
}

.home-title {
    position: absolute;

    top: 48.5vh;
    left: 50%;

    margin: 0;

    transform: translateX(-50%);

    color: #ffffff;

    font-size: clamp(50px, 4vw, 78px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -2.5px;

    white-space: nowrap;

    text-align: center;

    text-shadow:
        0 3px 12px rgba(0, 0, 0, 0.2);
}

.home-description {
    position: absolute;

    top: 59.7vh;
    left: 50%;

    width: 90%;
    margin: 0;

    transform: translateX(-50%);

    color: rgba(255, 255, 255, 0.76);

    font-size: clamp(23px, 1.9vw, 37px);
    line-height: 1.25;
    font-weight: 700;
    letter-spacing: -1.5px;

    text-align: center;
    white-space: nowrap;

    text-shadow:
        0 2px 10px rgba(0, 0, 0, 0.18);
}

.home-start-button {
    position: absolute;

    top: 79.5vh;
    left: 50%;

    width: 280px;
    height: 116px;

    transform: translateX(-50%);

    font-size: 31px;
}

.home-start-button:hover {
    transform:
        translateX(-50%)
        translateY(-4px);
}

.home-start-button:active {
    transform:
        translateX(-50%)
        translateY(0)
        scale(0.985);
}

/* ========================================================
   환영 화면
======================================================== */

.welcome-copy {
    position: absolute;

    top: 23.5vh;
    left: 6.1vw;

    z-index: 8;

    width: 52vw;
    max-width: 950px;
}

.welcome-title,
.welcome-description,
.welcome-start-button {
    opacity: 1;
    transform: translateY(0);
}

.welcome-screen.animate-in .welcome-title {
    animation:
        float-up 380ms
        cubic-bezier(0.22, 1, 0.36, 1)
        0ms both;
}

.welcome-screen.animate-in .welcome-description {
    animation:
        float-up 420ms
        cubic-bezier(0.22, 1, 0.36, 1)
        35ms both;
}

.welcome-screen.animate-in .welcome-start-button {
    animation:
        float-up 420ms
        cubic-bezier(0.22, 1, 0.36, 1)
        70ms both;
}

.welcome-title {
    margin: 0;

    color: #ffffff;

    font-size: clamp(47px, 3.75vw, 72px);
    line-height: 1.24;
    font-weight: 800;
    letter-spacing: -3px;

    text-shadow:
        0 4px 14px rgba(0, 0, 0, 0.30);
}

.welcome-description {
    margin: 43px 0 0;

    color: rgba(255, 255, 255, 0.92);

    font-size: clamp(25px, 2vw, 38px);
    line-height: 1.48;
    font-weight: 600;
    letter-spacing: -1.7px;

    text-shadow:
        0 3px 10px rgba(0, 0, 0, 0.28);
}

.welcome-start-button {
    position: absolute;

    left: 6.1vw;
    bottom: 12.9vh;

    z-index: 8;

    width: 280px;
    height: 118px;

    font-size: 34px;
}

/* ========================================================
   퀴즈 공통
======================================================== */

.quiz-screen {
    z-index: 12;
}

.question-viewport {
    position: absolute;

    z-index: 10;

    top: 21.5vh;
    left: 6.1vw;

    width: 58vw;
    max-width: 1115px;
    height: 66vh;

    overflow: visible;
}

.question-panel {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.question-panel.active {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
}

.quiz-screen.initial-entry .question-copy,
.quiz-screen.initial-entry .role-grid,
.quiz-screen.initial-entry .quiz-navigation {
    opacity: 0;
    transform: translateY(38px);
}

.quiz-screen.initial-entry .question-copy {
    animation:
        float-up 360ms
        cubic-bezier(0.22, 1, 0.36, 1)
        0ms both;
}

.quiz-screen.initial-entry .role-grid {
    animation:
        float-up 400ms
        cubic-bezier(0.22, 1, 0.36, 1)
        35ms both;
}

.quiz-screen.initial-entry .quiz-navigation {
    animation:
        float-up 400ms
        cubic-bezier(0.22, 1, 0.36, 1)
        70ms both;
}

.question-panel.enter-from-right {
    visibility: visible;
    pointer-events: auto;

    animation:
        slide-in-right 420ms
        cubic-bezier(0.22, 1, 0.36, 1)
        forwards;
}

.question-panel.leave-to-left {
    visibility: visible;

    animation:
        slide-out-left 360ms
        cubic-bezier(0.55, 0, 1, 0.45)
        forwards;
}

.question-panel.enter-from-left {
    visibility: visible;
    pointer-events: auto;

    animation:
        slide-in-left 420ms
        cubic-bezier(0.22, 1, 0.36, 1)
        forwards;
}

.question-panel.leave-to-right {
    visibility: visible;

    animation:
        slide-out-right 360ms
        cubic-bezier(0.55, 0, 1, 0.45)
        forwards;
}

.question-title {
    display: flex;
    align-items: baseline;
    gap: 16px;

    margin: 0;

    color: #ffffff;

    font-size: clamp(46px, 3.65vw, 70px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -2.4px;
}

.question-number {
    color: var(--accent-yellow);
}

.question-description {
    margin: 38px 0 0;

    color: #ffffff;

    font-size: clamp(25px, 1.9vw, 36px);
    line-height: 1.35;
    font-weight: 600;
    letter-spacing: -1.4px;
}

/* ========================================================
   Q1 역할 카드
======================================================== */

.role-grid {
    margin-top: 72px;

    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 16px;
}

.role-card {
    position: relative;

    height: 348px;

    padding: 70px 18px 32px;

    display: flex;
    flex-direction: column;
    align-items: center;

    color: #ffffff;
    background: rgba(10, 18, 32, 0.72);

    border:
        2px solid
        rgba(255, 255, 255, 0.18);

    border-radius: 14px;

    box-shadow:
        0 12px 28px
        rgba(0, 0, 0, 0.12);

    cursor: pointer;
    overflow: hidden;

    transition:
        transform 130ms cubic-bezier(0.22, 1, 0.36, 1),
        border-color 110ms ease,
        background-color 110ms ease,
        box-shadow 110ms ease;
}

.role-card::before {
    content: "";
    pointer-events: none;

    position: absolute;
    inset: 0;

    opacity: 0;

    background:
        linear-gradient(
            145deg,
            rgba(80, 183, 255, 0.28),
            rgba(52, 101, 164, 0.10)
        );

    transition:
        opacity 110ms ease;
}

.role-card:hover {
    transform: translateY(-12px);

    border-color:
        rgba(255, 255, 255, 0.40);

    box-shadow:
        0 22px 44px
        rgba(0, 0, 0, 0.28);
}

.role-card.selected {
    transform: translateY(-3px);

    border-color: var(--selected-blue);
    background: rgba(65, 119, 183, 0.44);

    box-shadow:
        inset 0 0 0 1px
        rgba(80, 183, 255, 0.34),
        0 18px 38px
        rgba(24, 117, 190, 0.18);
}

.role-card.selected::before {
    opacity: 1;
}

.role-card.selected:hover {
    transform: translateY(-12px);
}

.role-icon-circle,
.role-card-title,
.role-card-description {
    position: relative;
    z-index: 2;
}

.role-icon-circle {
    width: 96px;
    height: 96px;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        rgba(255, 255, 255, 0.07);

    border-radius: 50%;

    transition:
        background-color 110ms ease,
        transform 110ms ease;
}

.role-card:hover .role-icon-circle {
    transform: scale(1.06);
}

.role-card.selected .role-icon-circle {
    background:
        rgba(80, 183, 255, 0.96);
}

.role-icon {
    width: 53px;
    height: 53px;

    object-fit: contain;

    pointer-events: none;
    user-select: none;
}

.role-card-title {
    margin-top: 33px;

    color: #ffffff;

    font-size: clamp(22px, 1.65vw, 32px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: 1.4px;

    text-align: center;
}

.role-card.selected .role-card-title {
    color: var(--selected-blue);
}

.role-card-description {
    margin-top: 19px;

    color: var(--muted-white);

    font-size: clamp(14px, 0.95vw, 18px);
    line-height: 1.4;
    font-weight: 500;
    letter-spacing: -0.4px;

    text-align: center;
}

/* ========================================================
   Q2·Q3 공통 슬라이더
======================================================== */

.range-answer {
    margin-top: 105px;

    width: 100%;
    max-width: 1040px;

    padding: 0 18px;
}

.range-label-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    align-items: center;

    margin-bottom: 38px;
}

.range-option {
    margin: 0;
    padding: 8px 12px;

    color: #4db5fb;
    background: transparent;
    border: 0;

    font-size: clamp(25px, 1.75vw, 34px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -1px;

    cursor: pointer;

    transition:
        color 160ms ease,
        transform 160ms ease,
        text-shadow 160ms ease;
}

.range-option:first-child {
    text-align: left;
    justify-self: start;
}

.range-option:nth-child(2) {
    text-align: center;
    justify-self: center;
}

.range-option:last-child {
    text-align: right;
    justify-self: end;
}

.range-option:hover {
    color: #79c9ff;
    transform: translateY(-4px);
}

.range-option.selected {
    color: var(--accent-orange);

    text-shadow:
        0 0 18px rgba(237, 108, 37, 0.28);

    transform: translateY(-3px);
}

.range-slider-wrapper {
    width: 100%;
    padding: 0 4px;
}

.range-slider {
    width: 100%;
    height: 52px;

    margin: 0;

    background: transparent;
    cursor: pointer;

    -webkit-appearance: none;
    appearance: none;

    will-change: filter;
    transition:
        filter 180ms ease,
        opacity 180ms ease;
}

.range-slider.is-animating {
    filter:
        drop-shadow(
            0 0 12px
            rgba(237, 108, 37, 0.24)
        );
}

.range-slider.is-settling::-webkit-slider-thumb {
    animation:
        slider-snap-feedback
        240ms
        cubic-bezier(0.22, 1, 0.36, 1);
}

.range-slider.is-settling::-moz-range-thumb {
    animation:
        slider-snap-feedback
        240ms
        cubic-bezier(0.22, 1, 0.36, 1);
}

.range-slider::-webkit-slider-runnable-track {
    width: 100%;
    height: 18px;

    background: rgba(255, 255, 255, 0.94);
    border-radius: 999px;

    box-shadow:
        0 5px 16px rgba(0, 0, 0, 0.20);
}

.range-slider::-webkit-slider-thumb {
    width: 50px;
    height: 50px;

    margin-top: -16px;

    background: var(--accent-orange);
    border: 0;
    border-radius: 50%;

    box-shadow:
        0 7px 18px rgba(0, 0, 0, 0.28);

    cursor: grab;

    -webkit-appearance: none;
    appearance: none;

    transition:
        transform 140ms ease,
        background-color 140ms ease,
        box-shadow 140ms ease;
}

.range-slider:hover::-webkit-slider-thumb {
    background: var(--accent-orange-hover);
    transform: scale(1.08);

    box-shadow:
        0 9px 24px rgba(237, 108, 37, 0.38);
}

.range-slider:active::-webkit-slider-thumb {
    cursor: grabbing;
    transform: scale(0.98);
}

.range-slider::-moz-range-track {
    width: 100%;
    height: 18px;

    background: rgba(255, 255, 255, 0.94);
    border: 0;
    border-radius: 999px;

    box-shadow:
        0 5px 16px rgba(0, 0, 0, 0.20);
}

.range-slider::-moz-range-thumb {
    width: 50px;
    height: 50px;

    background: var(--accent-orange);
    border: 0;
    border-radius: 50%;

    box-shadow:
        0 7px 18px rgba(0, 0, 0, 0.28);

    cursor: grab;
}

.range-description-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);

    margin-top: 31px;

    color: rgba(255, 255, 255, 0.65);

    font-size: clamp(13px, 0.9vw, 17px);
    line-height: 1.4;
    font-weight: 500;
    letter-spacing: -0.4px;
}

.range-description-row span:first-child {
    text-align: left;
}

.range-description-row span:nth-child(2) {
    text-align: center;
}

.range-description-row span:last-child {
    text-align: right;
}

.range-slider:focus-visible {
    outline:
        3px solid
        rgba(77, 181, 251, 0.75);

    outline-offset: 8px;
}

.range-option:focus-visible {
    outline:
        2px solid
        rgba(77, 181, 251, 0.85);

    outline-offset: 4px;
    border-radius: 7px;
}

/* Q3·Q4·Q5는 슬라이더 양 끝의 의미만 표시합니다. */
.aim-label-row,
.mobility-label-row,
.aggression-label-row {
    display: flex;
    align-items: center;
    justify-content: space-between;

    grid-template-columns: none;
}

.aim-label-row .aim-option:first-child,
.mobility-label-row .mobility-option:first-child,
.aggression-label-row .aggression-option:first-child {
    justify-self: auto;
    text-align: left;
}

.aim-label-row .aim-option:last-child,
.mobility-label-row .mobility-option:last-child,
.aggression-label-row .aggression-option:last-child {
    justify-self: auto;
    text-align: right;
}

/* ========================================================
   하단 이동 및 진행도
======================================================== */

.quiz-navigation {
    position: absolute;

    z-index: 16;

    left: 6.1vw;
    bottom: 6.7vh;

    width: 58vw;
    max-width: 1115px;

    display: grid;
    grid-template-columns:
        80px
        minmax(300px, 1fr)
        80px;
    align-items: center;
    gap: 26px;
}

.arrow-button {
    position: relative;

    width: 72px;
    height: 72px;

    margin: 0;
    padding: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    background: transparent;
    border: 0;

    cursor: pointer;

    transition:
        transform 110ms ease;
}

.arrow-button:not(.disabled):hover {
    transform: translateY(-5px);
}

.arrow-button.disabled {
    cursor: default;
    opacity: 0.82;
}

.arrow-single,
.arrow-default,
.arrow-hover {
    position: absolute;

    width: 72px;
    height: 72px;

    object-fit: contain;

    pointer-events: none;
    user-select: none;
}

.arrow-default {
    opacity: 1;

    transition:
        opacity 90ms ease;
}

.arrow-hover {
    opacity: 0;

    transition:
        opacity 90ms ease;
}

.arrow-button:not(.disabled):hover .arrow-default {
    opacity: 0;
}

.arrow-button:not(.disabled):hover .arrow-hover {
    opacity: 1;
}

.progress-dots {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 27px;
}

.progress-dot {
    width: 22px;
    height: 22px;

    flex-shrink: 0;

    border-radius: 50%;

    transition:
        background-color 110ms ease,
        transform 110ms ease;
}

.progress-dot.pending {
    background:
        rgba(255, 255, 255, 0.58);
}

.progress-dot.completed {
    background: #ffffff;
}

.progress-dot.current {
    background: var(--accent-orange);
    transform: scale(1.04);
}

/* ========================================================
   애니메이션
======================================================== */

@keyframes slider-snap-feedback {
    0% {
        transform: scale(1);
        box-shadow:
            0 7px 18px
            rgba(0, 0, 0, 0.28);
    }

    48% {
        transform: scale(1.18);
        box-shadow:
            0 0 0 9px
            rgba(237, 108, 37, 0.16),
            0 10px 25px
            rgba(237, 108, 37, 0.38);
    }

    72% {
        transform: scale(0.96);
    }

    100% {
        transform: scale(1);
        box-shadow:
            0 7px 18px
            rgba(0, 0, 0, 0.28);
    }
}

@keyframes float-up {
    from {
        opacity: 0;
        transform: translateY(38px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slide-in-right {
    from {
        opacity: 0;
        transform: translateX(120px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slide-out-left {
    from {
        opacity: 1;
        transform: translateX(0);
    }

    to {
        opacity: 0;
        transform: translateX(-105px);
    }
}

@keyframes slide-in-left {
    from {
        opacity: 0;
        transform: translateX(-120px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slide-out-right {
    from {
        opacity: 1;
        transform: translateX(0);
    }

    to {
        opacity: 0;
        transform: translateX(105px);
    }
}

/* ========================================================
   반응형
======================================================== */

@media (max-width: 1300px) {
    .question-viewport {
        top: 20vh;
        left: 5vw;

        width: 65vw;
    }

    .quiz-navigation {
        left: 5vw;
        width: 65vw;
        bottom: 4vh;
    }

    .role-grid {
        margin-top: 50px;
    }

    .role-card {
        height: 310px;
        padding-top: 54px;
    }

    .character-image {
        right: -10vw;
        width: 54vw;
    }
}

@media (max-width: 950px) {
    .app-header {
        left: 18px;
        right: 18px;

        min-height: 82px;

        padding:
            0 15px
            0 20px;

        border-radius: 18px;
    }

    .brand-button {
        gap: 14px;
    }

    .brand-symbol {
        width: 54px;
        height: 54px;
    }

    .brand-title {
        font-size: 22px;
    }

    .student-badge {
        min-width: auto;
        height: 58px;

        padding: 0 16px;

        font-size: 17px;

        border-radius: 13px;
    }

    .home-wordmark {
        width: 78vw;
    }

    .home-title {
        font-size: 48px;
    }

    .home-description {
        width: 88%;
        font-size: 24px;
        white-space: normal;
    }

    .home-start-button {
        width: 230px;
        height: 86px;

        font-size: 26px;
    }

    .welcome-copy {
        top: 22vh;
        left: 6vw;
        width: 67vw;
    }

    .welcome-title {
        font-size: 42px;
    }

    .welcome-description {
        font-size: 23px;
    }

    .welcome-start-button {
        left: 6vw;
        bottom: 11vh;

        width: 240px;
        height: 92px;

        font-size: 28px;
    }

    .question-viewport {
        top: 19vh;
        left: 5vw;

        width: 90vw;
    }

    .quiz-navigation {
        left: 5vw;
        width: 90vw;
        bottom: 3.3vh;
    }

    .character-image {
        right: -26vw;
        width: 74vw;
        opacity: 0 !important;
    }

    #ow-app[data-screen="welcome"] .character-image,
    #ow-app[data-screen="quiz"] .character-image {
        opacity: 0.45 !important;
    }

    .role-grid {
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }

    .role-card {
        height: 255px;
        padding-top: 32px;
    }

    .role-icon-circle {
        width: 76px;
        height: 76px;
    }

    .role-icon {
        width: 42px;
        height: 42px;
    }

    .role-card-title {
        margin-top: 22px;
    }
}

@media (max-width: 620px) {
    .brand-title {
        font-size: 16px;
    }

    .student-badge {
        max-width: 150px;
        font-size: 13px;
        text-align: center;
    }

    .home-title {
        font-size: 39px;
    }

    .home-description {
        font-size: 20px;
    }

    .welcome-copy {
        top: 21vh;
        width: 86vw;
    }

    .welcome-title {
        font-size: 35px;
    }

    .welcome-description {
        margin-top: 25px;
        font-size: 20px;
    }

    .question-viewport {
        top: 17vh;
    }

    .question-title {
        font-size: 36px;
    }

    .question-description {
        margin-top: 22px;
        font-size: 20px;
    }

    .role-grid {
        margin-top: 30px;
        gap: 10px;
    }

    .role-card {
        height: 220px;
        padding:
            24px 10px
            20px;
    }

    .role-icon-circle {
        width: 64px;
        height: 64px;
    }

    .role-icon {
        width: 35px;
        height: 35px;
    }

    .role-card-title {
        font-size: 18px;
    }

    .role-card-description {
        margin-top: 12px;
        font-size: 12px;
    }

    .quiz-navigation {
        grid-template-columns:
            56px
            minmax(180px, 1fr)
            56px;

        gap: 10px;
    }

    .arrow-button,
    .arrow-single,
    .arrow-default,
    .arrow-hover {
        width: 54px;
        height: 54px;
    }

    .progress-dots {
        gap: 11px;
    }

    .progress-dot {
        width: 14px;
        height: 14px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.001ms !important;
        animation-delay: 0ms !important;
        transition-duration: 0.001ms !important;
        scroll-behavior: auto !important;
    }
}
"""


# =========================================================
# Custom Component JavaScript
# =========================================================

APP_JS_TEMPLATE = r"""
export default function(component) {
    const { parentElement } = component;

    const app = parentElement.querySelector("#ow-app");
    if (!app) {
        return;
    }


    const screens = {
        home: parentElement.querySelector("#home-screen"),
        welcome: parentElement.querySelector("#welcome-screen"),
        quiz: parentElement.querySelector("#quiz-screen"),
    };

    const questions = {
        1: parentElement.querySelector("#question-1"),
        2: parentElement.querySelector("#question-2"),
        3: parentElement.querySelector("#question-3"),
        4: parentElement.querySelector("#question-4"),
        5: parentElement.querySelector("#question-5"),
    };

    const homeButton = parentElement.querySelector("#home-button");
    const homeStartButton = parentElement.querySelector("#home-start-button");
    const welcomeStartButton = parentElement.querySelector("#welcome-start-button");

    const previousButton = parentElement.querySelector("#previous-question-button");
    const nextButton = parentElement.querySelector("#next-question-button");

    const roleCards = Array.from(
        parentElement.querySelectorAll(".role-card")
    );

    const rangeSlider =
        parentElement.querySelector("#range-slider");

    const rangeOptions = Array.from(
        parentElement.querySelectorAll(
            "#question-2 .range-option"
        )
    );

    const aimSlider =
        parentElement.querySelector("#aim-slider");

    const aimOptions = Array.from(
        parentElement.querySelectorAll(
            "#question-3 .aim-option"
        )
    );

    const mobilitySlider =
        parentElement.querySelector("#mobility-slider");

    const mobilityOptions = Array.from(
        parentElement.querySelectorAll(
            "#question-4 .mobility-option"
        )
    );

    const aggressionSlider =
        parentElement.querySelector("#aggression-slider");

    const aggressionOptions = Array.from(
        parentElement.querySelectorAll(
            "#question-5 .aggression-option"
        )
    );

    const progressDots = Array.from(
        parentElement.querySelectorAll(".progress-dot")
    );

    const imageUris = {
        leftGray: __ARROW_LEFT_GRAY_URI__,
        leftWhite: __ARROW_LEFT_WHITE_URI__,
        leftOrange: __ARROW_LEFT_ORANGE_URI__,
        rightGray: __ARROW_RIGHT_GRAY_URI__,
        rightWhite: __ARROW_RIGHT_WHITE_URI__,
        rightOrange: __ARROW_RIGHT_ORANGE_URI__,
    };

    const state = app.__owState ?? {
        screen: "home",
        currentQuestion: 1,
        answers: {
            role: null,
            range: null,
            aim: null,
            mobility: null,
            aggression: null,
        },
        isQuestionAnimating: false,
    };
    app.__owState = state;

    // 기존 상태 객체에 새 질문 값이 없을 때를 대비합니다.
    state.answers.range ??= null;
    state.answers.aim ??= null;
    state.answers.mobility ??= null;
    state.answers.aggression ??= null;

    const sliderAnimationFrames = new WeakMap();
    const sliderOriginalSteps = new WeakMap();

    function clearAnimationClass(element, className, timeout = 900) {
        window.setTimeout(() => {
            element.classList.remove(className);
        }, timeout);
    }

    function restartClassAnimation(element, className) {
        element.classList.remove(className);
        void element.offsetWidth;
        element.classList.add(className);
    }

    function triggerSliderSnapFeedback(slider) {
        slider.classList.remove("is-settling");
        void slider.offsetWidth;
        slider.classList.add("is-settling");

        window.setTimeout(() => {
            slider.classList.remove("is-settling");
        }, 260);
    }

    function cancelSliderAnimation(slider) {
        const animationFrame =
            sliderAnimationFrames.get(slider);

        if (animationFrame !== undefined) {
            window.cancelAnimationFrame(animationFrame);
            sliderAnimationFrames.delete(slider);
        }

        const originalStep =
            sliderOriginalSteps.get(slider);

        if (originalStep !== undefined) {
            slider.step = originalStep;
            sliderOriginalSteps.delete(slider);
        }

        slider.classList.remove("is-animating");
    }

    function animateSliderTo(
        slider,
        targetValue,
        commitValue
    ) {
        cancelSliderAnimation(slider);

        const startValue =
            Number(slider.value);

        const finalValue =
            Number(targetValue);

        if (
            !Number.isFinite(startValue)
            || !Number.isFinite(finalValue)
        ) {
            return;
        }

        if (startValue === finalValue) {
            commitValue(finalValue);
            triggerSliderSnapFeedback(slider);
            return;
        }

        const originalStep =
            slider.step || "1";

        sliderOriginalSteps.set(
            slider,
            originalStep
        );

        /*
        애니메이션 도중에는 소수점 값을 허용해서
        손잡이가 구간 사이를 부드럽게 이동하도록 합니다.
        마지막에는 원래 step을 복구하고 정확한 점수에 고정합니다.
        */
        slider.step = "any";
        slider.classList.add("is-animating");

        const distance =
            Math.abs(finalValue - startValue);

        const duration =
            220 + distance * 55;

        const startedAt =
            performance.now();

        function animateFrame(currentTime) {
            const progress =
                Math.min(
                    (currentTime - startedAt) / duration,
                    1
                );

            const easedProgress =
                1 - Math.pow(1 - progress, 3);

            const animatedValue =
                startValue
                + (
                    finalValue - startValue
                ) * easedProgress;

            slider.value =
                String(animatedValue);

            if (progress < 1) {
                const nextFrame =
                    window.requestAnimationFrame(
                        animateFrame
                    );

                sliderAnimationFrames.set(
                    slider,
                    nextFrame
                );

                return;
            }

            slider.step = originalStep;
            slider.value = String(finalValue);

            sliderOriginalSteps.delete(slider);
            sliderAnimationFrames.delete(slider);
            slider.classList.remove("is-animating");

            commitValue(finalValue);
            triggerSliderSnapFeedback(slider);
        }

        const firstFrame =
            window.requestAnimationFrame(
                animateFrame
            );

        sliderAnimationFrames.set(
            slider,
            firstFrame
        );
    }

    function ensureDefaultAnswerForQuestion(
        questionNumber
    ) {
        if (
            questionNumber === 2
            && state.answers.range === null
        ) {
            state.answers.range = 3;
            updateRangeUI();
            return;
        }

        if (
            questionNumber === 3
            && state.answers.aim === null
        ) {
            state.answers.aim = 3;
            updateAimUI();
            return;
        }

        if (
            questionNumber === 4
            && state.answers.mobility === null
        ) {
            state.answers.mobility = 3;
            updateMobilityUI();
            return;
        }

        if (
            questionNumber === 5
            && state.answers.aggression === null
        ) {
            state.answers.aggression = 3;
            updateAggressionUI();
        }
    }

    function showScreen(screenName) {
        if (!screens[screenName]) {
            return;
        }

        Object.values(screens).forEach((screen) => {
            screen.classList.remove("active");
        });

        state.screen = screenName;
        app.dataset.screen = screenName;
        screens[screenName].classList.add("active");

        if (screenName === "welcome") {
            restartClassAnimation(
                screens.welcome,
                "animate-in"
            );
            clearAnimationClass(
                screens.welcome,
                "animate-in",
                650
            );
        }

        if (screenName === "quiz") {
            state.currentQuestion = 1;
            setQuestionInstantly(1);

            restartClassAnimation(
                screens.quiz,
                "initial-entry"
            );
            clearAnimationClass(
                screens.quiz,
                "initial-entry",
                650
            );

            updateQuizUI();
        }
    }

    function resetQuiz() {
        state.currentQuestion = 1;
        state.answers.role = null;
        state.answers.range = null;
        state.answers.aim = null;
        state.answers.mobility = null;
        state.answers.aggression = null;

        roleCards.forEach((card) => {
            card.classList.remove("selected");
            card.setAttribute("aria-checked", "false");
        });

        updateRangeUI();
        updateAimUI();
        updateMobilityUI();
        updateAggressionUI();
        setQuestionInstantly(1);
        updateQuizUI();
    }

    function goHome() {
        resetQuiz();
        showScreen("home");
    }

    function setQuestionInstantly(questionNumber) {
        ensureDefaultAnswerForQuestion(
            questionNumber
        );

        Object.entries(questions).forEach(([number, panel]) => {
            const isCurrent = Number(number) === questionNumber;

            panel.classList.remove(
                "active",
                "enter-from-right",
                "leave-to-left",
                "enter-from-left",
                "leave-to-right"
            );

            if (isCurrent) {
                panel.classList.add("active");
            }
        });

        state.currentQuestion = questionNumber;
    }

    function moveQuestion(nextQuestion, direction) {
        if (
            state.isQuestionAnimating
            || nextQuestion === state.currentQuestion
            || !questions[nextQuestion]
        ) {
            return;
        }

        state.isQuestionAnimating = true;

        ensureDefaultAnswerForQuestion(
            nextQuestion
        );

        const currentPanel =
            questions[state.currentQuestion];

        const nextPanel =
            questions[nextQuestion];

        const leavingClass =
            direction === "forward"
                ? "leave-to-left"
                : "leave-to-right";

        const enteringClass =
            direction === "forward"
                ? "enter-from-right"
                : "enter-from-left";

        // 기존 패널이 거의 사라진 뒤 새 패널을 등장시킵니다.
        const enterDelay = 330;
        const enterDuration = 420;
        const cleanupBuffer = 30;

        currentPanel.classList.remove("active");
        currentPanel.classList.add(leavingClass);

        nextPanel.classList.remove(
            "active",
            "leave-to-left",
            "leave-to-right",
            "enter-from-left",
            "enter-from-right"
        );

        window.setTimeout(() => {
            nextPanel.classList.add(enteringClass);
        }, enterDelay);

        window.setTimeout(() => {
            currentPanel.classList.remove(leavingClass);
            nextPanel.classList.remove(enteringClass);
            nextPanel.classList.add("active");

            state.currentQuestion = nextQuestion;
            state.isQuestionAnimating = false;

            updateQuizUI();
        }, enterDelay + enterDuration + cleanupBuffer);
    }

    function setArrowContent(
        button,
        direction,
        enabled
    ) {
        button.replaceChildren();

        const defaultImage = document.createElement("img");
        defaultImage.alt = "";
        defaultImage.draggable = false;

        if (!enabled) {
            defaultImage.className = "arrow-single";
            defaultImage.src =
                direction === "left"
                    ? imageUris.leftGray
                    : imageUris.rightGray;

            button.append(defaultImage);
            button.classList.add("disabled");
            button.disabled = true;
            return;
        }

        const hoverImage = document.createElement("img");
        hoverImage.alt = "";
        hoverImage.draggable = false;

        defaultImage.className = "arrow-default";
        hoverImage.className = "arrow-hover";

        if (direction === "left") {
            defaultImage.src = imageUris.leftWhite;
            hoverImage.src = imageUris.leftOrange;
        } else {
            defaultImage.src = imageUris.rightWhite;
            hoverImage.src = imageUris.rightOrange;
        }

        button.append(defaultImage, hoverImage);
        button.classList.remove("disabled");
        button.disabled = false;
    }

    function updateProgressDots() {
        progressDots.forEach((dot, index) => {
            const questionNumber = index + 1;

            dot.classList.remove(
                "pending",
                "completed",
                "current"
            );

            if (questionNumber === state.currentQuestion) {
                dot.classList.add("current");
                return;
            }

            const completedQuestions = {
                1: state.answers.role !== null,
                2: state.answers.range !== null,
                3: state.answers.aim !== null,
                4: state.answers.mobility !== null,
                5: state.answers.aggression !== null,
            };

            const isCompleted =
                completedQuestions[questionNumber]
                ?? false;

            dot.classList.add(
                isCompleted
                    ? "completed"
                    : "pending"
            );
        });
    }

    function updateNavigation() {
        const previousEnabled =
            state.currentQuestion > 1;

        const answerReadyByQuestion = {
            1: state.answers.role !== null,
            2: true,
            3: true,
            4: true,
            5: true,
        };

        /*
        슬라이더 질문은 화면에 들어오는 순간 기본값 3이
        실제 답변으로 저장되므로 별도 클릭 없이도 이동할 수 있습니다.
        다만 다음 질문 화면이 실제로 존재할 때만 화살표를 활성화합니다.
        */
        const hasNextQuestion =
            Boolean(
                questions[
                    state.currentQuestion + 1
                ]
            );

        const nextEnabled =
            hasNextQuestion
            && Boolean(
                answerReadyByQuestion[
                    state.currentQuestion
                ]
            );

        setArrowContent(
            previousButton,
            "left",
            previousEnabled
        );

        setArrowContent(
            nextButton,
            "right",
            nextEnabled
        );
    }

    function updateQuizUI() {
        updateProgressDots();
        updateNavigation();
    }

    function selectRole(card) {
        const selectedRole = card.dataset.role;
        state.answers.role = selectedRole;

        roleCards.forEach((roleCard) => {
            const isSelected =
                roleCard.dataset.role === selectedRole;

            roleCard.classList.toggle(
                "selected",
                isSelected
            );

            roleCard.setAttribute(
                "aria-checked",
                String(isSelected)
            );
        });

        updateQuizUI();
    }

    function getRangeLabel(value) {
        const labels = {
            1: "단거리",
            3: "중거리",
            5: "장거리",
        };

        return labels[value] ?? "선택하지 않음";
    }

    function updateRangeUI() {
        const displayValue =
            state.answers.range ?? 3;

        rangeSlider.value =
            String(displayValue);

        rangeSlider.setAttribute(
            "aria-valuetext",
            state.answers.range === null
                ? "선택하지 않음"
                : getRangeLabel(displayValue)
        );

        rangeOptions.forEach((option) => {
            const optionValue =
                Number(option.dataset.range);

            const isSelected =
                state.answers.range === optionValue;

            option.classList.toggle(
                "selected",
                isSelected
            );

            option.setAttribute(
                "aria-pressed",
                String(isSelected)
            );
        });
    }

    function selectRange(value) {
        const numericValue = Number(value);
        const validValues = [1, 3, 5];

        if (!validValues.includes(numericValue)) {
            return;
        }

        state.answers.range = numericValue;
        updateRangeUI();
        updateQuizUI();
    }

    function getAimLabel(value) {
        const labels = {
            1: "조준 부담 적음",
            2: "조준 자신감 낮음",
            3: "보통",
            4: "조준 자신감 높음",
            5: "정밀 조준 필요",
        };

        return labels[value] ?? "선택하지 않음";
    }

    function updateAimUI() {
        const displayValue =
            state.answers.aim ?? 3;

        aimSlider.value =
            String(displayValue);

        aimSlider.setAttribute(
            "aria-valuetext",
            state.answers.aim === null
                ? "선택하지 않음"
                : getAimLabel(displayValue)
        );

        aimOptions.forEach((option) => {
            const optionValue =
                Number(option.dataset.aim);

            const isSelected =
                state.answers.aim === optionValue;

            option.classList.toggle(
                "selected",
                isSelected
            );

            option.setAttribute(
                "aria-pressed",
                String(isSelected)
            );
        });
    }

    function selectAim(value) {
        const numericValue = Number(value);
        const validValues = [1, 2, 3, 4, 5];

        if (!validValues.includes(numericValue)) {
            return;
        }

        state.answers.aim = numericValue;
        updateAimUI();
        updateQuizUI();
    }

    function getMobilityLabel(value) {
        const labels = {
            1: "한 자리를 안정적으로 지키고 싶어요",
            2: "이동이 많지 않은 플레이를 선호해요",
            3: "상황에 따라 움직이고 싶어요",
            4: "빠른 이동과 재배치를 좋아해요",
            5: "끊임없이 전장을 누비고 싶어요",
        };

        return labels[value] ?? "선택하지 않음";
    }

    function updateMobilityUI() {
        const displayValue =
            state.answers.mobility ?? 3;

        mobilitySlider.value =
            String(displayValue);

        mobilitySlider.setAttribute(
            "aria-valuetext",
            state.answers.mobility === null
                ? "선택하지 않음"
                : getMobilityLabel(displayValue)
        );

        mobilityOptions.forEach((option) => {
            const optionValue =
                Number(option.dataset.mobility);

            const isSelected =
                state.answers.mobility === optionValue;

            option.classList.toggle(
                "selected",
                isSelected
            );

            option.setAttribute(
                "aria-pressed",
                String(isSelected)
            );
        });
    }

    function selectMobility(value) {
        const numericValue = Number(value);
        const validValues = [1, 2, 3, 4, 5];

        if (!validValues.includes(numericValue)) {
            return;
        }

        state.answers.mobility = numericValue;
        updateMobilityUI();
        updateQuizUI();
    }

    function getAggressionLabel(value) {
        const labels = {
            1: "안전하게 기다리며 기회를 보고 싶어요",
            2: "방어적인 플레이를 선호해요",
            3: "상황에 따라 진입하고 싶어요",
            4: "적극적으로 교전을 시작하고 싶어요",
            5: "적진 깊숙이 뛰어들고 싶어요",
        };

        return labels[value] ?? "선택하지 않음";
    }

    function updateAggressionUI() {
        const displayValue =
            state.answers.aggression ?? 3;

        aggressionSlider.value =
            String(displayValue);

        aggressionSlider.setAttribute(
            "aria-valuetext",
            state.answers.aggression === null
                ? "선택하지 않음"
                : getAggressionLabel(displayValue)
        );

        aggressionOptions.forEach((option) => {
            const optionValue =
                Number(option.dataset.aggression);

            const isSelected =
                state.answers.aggression === optionValue;

            option.classList.toggle(
                "selected",
                isSelected
            );

            option.setAttribute(
                "aria-pressed",
                String(isSelected)
            );
        });
    }

    function selectAggression(value) {
        const numericValue = Number(value);
        const validValues = [1, 2, 3, 4, 5];

        if (!validValues.includes(numericValue)) {
            return;
        }

        state.answers.aggression = numericValue;
        updateAggressionUI();
        updateQuizUI();
    }

    function handlePrevious() {
        if (state.currentQuestion === 5) {
            moveQuestion(4, "backward");
            return;
        }

        if (state.currentQuestion === 4) {
            moveQuestion(3, "backward");
            return;
        }

        if (state.currentQuestion === 3) {
            moveQuestion(2, "backward");
            return;
        }

        if (state.currentQuestion === 2) {
            moveQuestion(1, "backward");
        }
    }

    function handleNext() {
        if (
            state.currentQuestion === 1
            && state.answers.role !== null
        ) {
            moveQuestion(2, "forward");
            return;
        }

        if (
            state.currentQuestion === 2
            && state.answers.range !== null
        ) {
            moveQuestion(3, "forward");
            return;
        }

        if (
            state.currentQuestion === 3
            && state.answers.aim !== null
        ) {
            moveQuestion(4, "forward");
            return;
        }

        if (
            state.currentQuestion === 4
            && state.answers.mobility !== null
        ) {
            moveQuestion(5, "forward");
        }
    }

    function handleAppClick(event) {
        const target = event.target instanceof Element
            ? event.target
            : null;

        if (!target) {
            return;
        }

        const button = target.closest("button");
        if (!button || !app.contains(button) || button.disabled) {
            return;
        }

        if (button === homeButton) {
            goHome();
            return;
        }

        if (button === homeStartButton) {
            showScreen("welcome");
            return;
        }

        if (button === welcomeStartButton) {
            showScreen("quiz");
            return;
        }

        if (button === previousButton) {
            handlePrevious();
            return;
        }

        if (button === nextButton) {
            handleNext();
            return;
        }

        if (button.classList.contains("role-card")) {
            selectRole(button);
            return;
        }

        if (
            button.classList.contains("range-option")
            && button.dataset.range
        ) {
            animateSliderTo(
                rangeSlider,
                button.dataset.range,
                selectRange
            );
            return;
        }

        if (button.classList.contains("aim-option")) {
            animateSliderTo(
                aimSlider,
                button.dataset.aim,
                selectAim
            );
            return;
        }

        if (button.classList.contains("mobility-option")) {
            animateSliderTo(
                mobilitySlider,
                button.dataset.mobility,
                selectMobility
            );
            return;
        }

        if (button.classList.contains("aggression-option")) {
            animateSliderTo(
                aggressionSlider,
                button.dataset.aggression,
                selectAggression
            );
        }
    }

    function getSliderCommitFunction(slider) {
        if (slider === rangeSlider) {
            return selectRange;
        }

        if (slider === aimSlider) {
            return selectAim;
        }

        if (slider === mobilitySlider) {
            return selectMobility;
        }

        if (slider === aggressionSlider) {
            return selectAggression;
        }

        return null;
    }

    function handleAppInput(event) {
        const target =
            event.target instanceof HTMLInputElement
                ? event.target
                : null;

        if (!target) {
            return;
        }

        /*
        마우스나 터치로 드래그하는 동안에는 step="any"를 사용해
        손잡이가 연속적으로 움직이게 합니다.
        실제 점수 저장은 드래그가 끝난 뒤 가장 가까운 단계로
        스냅될 때 한 번만 수행합니다.
        */
        if (target.dataset.dragging === "true") {
            return;
        }

        const commitValue =
            getSliderCommitFunction(target);

        if (commitValue) {
            commitValue(target.value);
        }
    }

    function handleSliderPointerDown(event) {
        const target =
            event.target instanceof HTMLInputElement
                ? event.target
                : null;

        if (
            !target
            || !target.classList.contains(
                "range-slider"
            )
        ) {
            return;
        }

        cancelSliderAnimation(target);

        const originalStep =
            target.step || "1";

        sliderOriginalSteps.set(
            target,
            originalStep
        );

        target.dataset.dragging = "true";
        target.step = "any";
        target.classList.add("is-animating");
    }

    function handleSliderChange(event) {
        const target =
            event.target instanceof HTMLInputElement
                ? event.target
                : null;

        if (
            !target
            || !target.classList.contains(
                "range-slider"
            )
        ) {
            return;
        }

        const commitValue =
            getSliderCommitFunction(target);

        if (!commitValue) {
            return;
        }

        const originalStep =
            Number(
                sliderOriginalSteps.get(target)
                ?? target.step
                ?? 1
            );

        const minimum =
            Number(target.min);

        const maximum =
            Number(target.max);

        const rawValue =
            Number(target.value);

        const snappedValue =
            Math.min(
                maximum,
                Math.max(
                    minimum,
                    minimum
                    + Math.round(
                        (rawValue - minimum)
                        / originalStep
                    ) * originalStep
                )
            );

        delete target.dataset.dragging;

        /*
        드래그가 끝나는 순간 가장 가까운 유효 점수로
        짧게 끌려가며 고정되는 스냅 애니메이션을 실행합니다.
        */
        animateSliderTo(
            target,
            snappedValue,
            commitValue
        );
    }

    const abortController = new AbortController();

    app.addEventListener(
        "click",
        handleAppClick,
        { signal: abortController.signal }
    );

    app.addEventListener(
        "input",
        handleAppInput,
        { signal: abortController.signal }
    );

    app.addEventListener(
        "pointerdown",
        handleSliderPointerDown,
        { signal: abortController.signal }
    );

    app.addEventListener(
        "change",
        handleSliderChange,
        { signal: abortController.signal }
    );

    // Streamlit이 컴포넌트를 다시 렌더링해도
    // 현재 화면과 선택 상태를 즉시 복구합니다.
    app.dataset.screen = state.screen;
    Object.values(screens).forEach((screen) => {
        screen.classList.toggle(
            "active",
            screen === screens[state.screen]
        );
    });
    setQuestionInstantly(state.currentQuestion);

    roleCards.forEach((card) => {
        const isSelected =
            card.dataset.role === state.answers.role;

        card.classList.toggle("selected", isSelected);
        card.setAttribute("aria-checked", String(isSelected));
    });

    updateRangeUI();
    updateAimUI();
    updateMobilityUI();
    updateAggressionUI();
    updateQuizUI();

    return () => {
        abortController.abort();
    };
}
"""

APP_JS = (
    APP_JS_TEMPLATE
    .replace("__ARROW_LEFT_GRAY_URI__", json.dumps(ARROW_LEFT_GRAY_URI))
    .replace("__ARROW_LEFT_WHITE_URI__", json.dumps(ARROW_LEFT_WHITE_URI))
    .replace("__ARROW_LEFT_ORANGE_URI__", json.dumps(ARROW_LEFT_ORANGE_URI))
    .replace("__ARROW_RIGHT_GRAY_URI__", json.dumps(ARROW_RIGHT_GRAY_URI))
    .replace("__ARROW_RIGHT_WHITE_URI__", json.dumps(ARROW_RIGHT_WHITE_URI))
    .replace("__ARROW_RIGHT_ORANGE_URI__", json.dumps(ARROW_RIGHT_ORANGE_URI))
)


# =========================================================
# Component 등록 및 실행
# =========================================================

app_component = st.components.v2.component(
    name="overwatch_recommendation_shell",
    html=APP_HTML,
    css=APP_CSS,
    js=APP_JS,
    isolate_styles=False,
)


def main() -> None:
    hide_streamlit_interface()

    app_component(
        key="overwatch-recommendation-shell",
        width="stretch",
        height=1000,
    )


if __name__ == "__main__":
    main()
