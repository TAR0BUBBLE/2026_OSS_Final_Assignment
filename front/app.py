import json
import os

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

# 비워 두면 브라우저의 현재 호스트와 8000번 포트를 자동으로 사용합니다.
# EC2에서 별도 주소가 필요하면 FASTAPI_PUBLIC_URL 환경변수로 지정할 수 있습니다.
API_BASE_URL = os.getenv("FASTAPI_PUBLIC_URL", "").strip().rstrip("/")

STUDENT_INFO = "2023204017 최유진"


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
# Custom Component HTML
# =========================================================

APP_HTML = f"""
<div id="ow-viewport" class="assets-loading">
    <div id="asset-loading-screen" role="status" aria-live="polite">
        <span class="asset-loading-spinner" aria-hidden="true"></span>
        <strong>화면을 준비하고 있어...</strong>
    </div>
<main id="ow-app" data-screen="home">
    <img
        class="background-image"
        src="" data-asset-path="backgrounds/home_background.png" fetchpriority="high" data-essential-asset="true"
        alt=""
        draggable="false"
        aria-hidden="true"
    />
    <div class="background-shade" aria-hidden="true"></div>

    <img
        class="character-image"
        src="" data-asset-path="heroes/character.png" fetchpriority="high"
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
                src="" data-asset-path="logos/overwatch_symbol.png" fetchpriority="high" data-essential-asset="true"
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
            src="" data-asset-path="logos/overwatch_wordmark.png" fetchpriority="high" data-essential-asset="true"
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
                                src="" data-asset-path="icons/role_tank.png"
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
                                src="" data-asset-path="icons/role_damage.png"
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
                                src="" data-asset-path="icons/role_support.png"
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
                                src="" data-asset-path="icons/role_flex.png"
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

            <!-- Q6. 선호 전투 위치 질문 -->
            <article id="question-6" class="question-panel question-six-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q6.</span>
                        <span>선호 전투 위치</span>
                    </h1>

                    <p class="question-description">
                        전투가 시작된다면 주로 어디에서 활약하고 싶나요?
                    </p>
                </div>

                <div
                    class="position-grid"
                    role="radiogroup"
                    aria-label="선호 전투 위치"
                >
                    <button
                        class="position-card"
                        type="button"
                        data-position="frontline"
                        role="radio"
                        aria-checked="false"
                    >
                        최전방 - 적과 가장 가까운 곳에서 싸워요
                    </button>

                    <button
                        class="position-card"
                        type="button"
                        data-position="midline"
                        role="radio"
                        aria-checked="false"
                    >
                        중간 전선 - 공격과 지원을 유연하게 수행해요
                    </button>

                    <button
                        class="position-card"
                        type="button"
                        data-position="backline"
                        role="radio"
                        aria-checked="false"
                    >
                        후방 - 안전한 거리에서 팀을 지원해요
                    </button>

                    <button
                        class="position-card"
                        type="button"
                        data-position="flank"
                        role="radio"
                        aria-checked="false"
                    >
                        측면·적 후방 - 몰래 접근해 적을 흔들어요
                    </button>

                    <button
                        class="position-card"
                        type="button"
                        data-position="flexible"
                        role="radio"
                        aria-checked="false"
                    >
                        상황에 따라 달라요
                    </button>
                </div>
            </article>

            <!-- Q7. 가장 중요한 능력 질문 -->
            <article id="question-7" class="question-panel question-seven-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q7.</span>
                        <span>가장 중요한 능력</span>
                    </h1>

                    <p class="question-description">
                        영웅을 선택할 때 가장 중요하게 생각하는 능력은 무엇인가요?
                    </p>
                </div>

                <div
                    class="priority-grid"
                    role="radiogroup"
                    aria-label="가장 중요한 능력"
                >
                    <button
                        class="priority-card"
                        type="button"
                        data-priority="damage"
                        role="radio"
                        aria-checked="false"
                    >
                        높은 공격력
                    </button>

                    <button
                        class="priority-card"
                        type="button"
                        data-priority="healing"
                        role="radio"
                        aria-checked="false"
                    >
                        강력한 치유
                    </button>

                    <button
                        class="priority-card"
                        type="button"
                        data-priority="survival"
                        role="radio"
                        aria-checked="false"
                    >
                        튼튼한 생존력
                    </button>

                    <button
                        class="priority-card"
                        type="button"
                        data-priority="control"
                        role="radio"
                        aria-checked="false"
                    >
                        적 방해 및 전장 제어
                    </button>

                    <button
                        class="priority-card"
                        type="button"
                        data-priority="protection"
                        role="radio"
                        aria-checked="false"
                    >
                        아군 보호와 구조
                    </button>

                    <button
                        class="priority-card"
                        type="button"
                        data-priority="easy"
                        role="radio"
                        aria-checked="false"
                    >
                        쉬운 조작과 입문 난이도
                    </button>
                </div>
            </article>

            <!-- Q8. 게임 경험 수준 질문 -->
            <article id="question-8" class="question-panel question-eight-panel">
                <div class="question-copy">
                    <h1 class="question-title">
                        <span class="question-number">Q8.</span>
                        <span>게임 경험 수준</span>
                    </h1>

                    <p class="question-description">
                        FPS 또는 오버워치 경험은 어느 정도인가요?
                    </p>
                </div>

                <div
                    class="experience-grid"
                    role="radiogroup"
                    aria-label="게임 경험 수준"
                >
                    <button
                        class="experience-card"
                        type="button"
                        data-experience="beginner"
                        role="radio"
                        aria-checked="false"
                        aria-label="입문자 — 처음 시작하거나 아직 익숙하지 않아요"
                    >
                        <strong class="experience-card-title">입문자</strong>
                    </button>

                    <button
                        class="experience-card"
                        type="button"
                        data-experience="intermediate"
                        role="radio"
                        aria-checked="false"
                        aria-label="중급자 — 기본적인 조작과 게임 규칙을 알고 있어요"
                    >
                        <strong class="experience-card-title">중급자</strong>
                    </button>

                    <button
                        class="experience-card"
                        type="button"
                        data-experience="advanced"
                        role="radio"
                        aria-checked="false"
                        aria-label="숙련자 — 어려운 영웅과 복잡한 운영도 괜찮아요"
                    >
                        <strong class="experience-card-title">숙련자</strong>
                    </button>
                </div>
            </article>
        </div>

        <button
            id="result-button"
            class="result-button"
            type="button"
            disabled
            aria-hidden="true"
        >
            결과보기
        </button>

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
                    src="" data-asset-path="icons/arrow_left_gray.png"
                    alt=""
                    draggable="false"
                />
            </button>

            <div id="progress-dots" class="progress-dots" aria-label="질문 진행도">
                <button class="progress-dot current" type="button" data-index="1" aria-label="1번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="2" aria-label="2번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="3" aria-label="3번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="4" aria-label="4번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="5" aria-label="5번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="6" aria-label="6번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="7" aria-label="7번 질문" disabled></button>
                <button class="progress-dot pending" type="button" data-index="8" aria-label="8번 질문" disabled></button>
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
                    src="" data-asset-path="icons/arrow_right_gray.png"
                    alt=""
                    draggable="false"
                />
            </button>
        </nav>
    </section>

    <!-- 추천 결과 화면 -->
    <section id="result-screen" class="screen result-screen" aria-live="polite">
        <div class="result-heading">
            <h1 class="result-title">
                너에게 <span>딱 맞는</span> 영웅 추천 순위!
            </h1>

            <p class="result-description">
                너의 성향을 분석한 결과야! 가장 마음에 드는 영웅을 선택해봐
            </p>
        </div>

        <div class="result-scroll-shell">
            <div
                id="result-scroll-container"
                class="result-scroll-container"
                tabindex="0"
                aria-label="추천 영웅 결과 목록"
            >
                <div id="result-loading" class="result-loading">
                    <span class="result-spinner" aria-hidden="true"></span>
                    <strong>너에게 맞는 영웅을 분석하고 있어...</strong>
                    <span>잠시만 기다려줘!</span>
                </div>

                <div id="result-error" class="result-error" hidden>
                    <strong>추천 결과를 불러오지 못했어.</strong>
                    <p id="result-error-message"></p>
                    <button
                        class="result-retry-button"
                        type="button"
                    >
                        다시 계산하기
                    </button>
                </div>

                <div id="result-content" class="result-content" hidden></div>
            </div>
        </div>

        <button
            id="restart-button"
            class="orange-button result-restart-button"
            type="button"
        >
            처음으로
        </button>
    </section>
</main>
</div>
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
.position-card,
.priority-card,
.experience-card,
.result-button,
.result-retry-button,
.result-restart-button,
.progress-dot,
.arrow-button,
.brand-button {
    -webkit-tap-highlight-color: transparent;
}

#ow-viewport {
    position: fixed;
    inset: 0;
    z-index: 99999;

    width: 100%;
    height: 100%;

    overflow: hidden;
    background: #0a1420;
}

#ow-app {
    position: absolute;
    top: 0;
    left: 0;

    width: 1920px;
    height: 1080px;

    overflow: hidden;

    color: #ffffff;
    background: #0a1420;

    opacity: 0;
    transform-origin: top left;
    will-change: transform;

    font-family:
        Arial,
        "Noto Sans KR",
        "Apple SD Gothic Neo",
        sans-serif;

    transition: opacity 120ms ease;
}

#ow-viewport.is-fitted.assets-ready #ow-app {
    opacity: 1;
}

#asset-loading-screen {
    position: absolute;
    inset: 0;
    z-index: 100000;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 18px;

    color: rgba(255, 255, 255, 0.86);
    background: #0a1420;

    font-size: 20px;
    font-weight: 800;
    letter-spacing: -0.4px;

    opacity: 1;
    visibility: visible;

    transition:
        opacity 180ms ease,
        visibility 0s linear 180ms;
}

#ow-viewport.assets-ready #asset-loading-screen {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.asset-loading-spinner {
    width: 52px;
    height: 52px;

    border:
        6px solid
        rgba(255, 255, 255, 0.16);

    border-top-color: var(--accent-orange);
    border-radius: 50%;

    animation:
        result-spinner-rotate
        760ms linear infinite;
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
#ow-app[data-screen="quiz"] .background-shade,
#ow-app[data-screen="result"] .background-shade {
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

    top: 24.84px;
    left: 51.84px;
    right: 51.84px;

    height: 116.64px;
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

    font-size: clamp(27px, 35.52px, 36px);
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

    font-size: clamp(22px, 28.8px, 30px);
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

    right: -9.6px;
    bottom: -14.04px;

    width: min(873.6px, 875px);
    max-height: 961.2px;

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
#ow-app[data-screen="quiz"] .character-image,
#ow-app[data-screen="result"] .character-image {
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

    top: 266.76px;
    left: 50%;

    width: min(1209.6px, 1210px);
    max-height: 155px;

    object-fit: contain;

    transform: translateX(-50%);

    pointer-events: none;
    user-select: none;
}

.home-title {
    position: absolute;

    top: 523.8px;
    left: 50%;

    margin: 0;

    transform: translateX(-50%);

    color: #ffffff;

    font-size: clamp(50px, 76.8px, 78px);
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

    top: 644.76px;
    left: 50%;

    width: 90%;
    margin: 0;

    transform: translateX(-50%);

    color: rgba(255, 255, 255, 0.76);

    font-size: clamp(23px, 36.48px, 37px);
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

    top: 858.6px;
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

    top: 253.8px;
    left: 117.12px;

    z-index: 8;

    width: 998.4px;
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

    font-size: clamp(47px, 72px, 72px);
    line-height: 1.24;
    font-weight: 800;
    letter-spacing: -3px;

    text-shadow:
        0 4px 14px rgba(0, 0, 0, 0.30);
}

.welcome-description {
    margin: 43px 0 0;

    color: rgba(255, 255, 255, 0.92);

    font-size: clamp(25px, 38.4px, 38px);
    line-height: 1.48;
    font-weight: 600;
    letter-spacing: -1.7px;

    text-shadow:
        0 3px 10px rgba(0, 0, 0, 0.28);
}

.welcome-start-button {
    position: absolute;

    left: 117.12px;
    bottom: 139.32px;

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

    top: 232.2px;
    left: 117.12px;

    width: 1113.6px;
    max-width: 1115px;
    height: 712.8px;

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

    font-size: clamp(46px, 70.08px, 70px);
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

    font-size: clamp(25px, 36.48px, 36px);
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

    font-size: clamp(22px, 31.68px, 32px);
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

    font-size: clamp(14px, 18.24px, 18px);
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

    font-size: clamp(25px, 33.6px, 34px);
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

    font-size: clamp(13px, 17.28px, 17px);
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
   Q6 선호 전투 위치 카드
======================================================== */

.position-grid {
    margin-top: 38px;
    margin-inline: auto;

    width: min(680px, 100%);

    display: grid;
    grid-template-columns: 1fr;
    gap: 18px;
}

.position-card {
    position: relative;

    width: 100%;
    min-height: 78px;

    margin: 0;
    padding: 0 38px;

    display: flex;
    align-items: center;

    color: rgba(255, 255, 255, 0.84);
    background:
        linear-gradient(
            90deg,
            rgba(20, 29, 44, 0.82),
            rgba(13, 21, 35, 0.74)
        );

    border:
        2px solid
        rgba(255, 255, 255, 0.20);

    border-radius: 13px;

    box-shadow:
        0 10px 24px
        rgba(0, 0, 0, 0.14);

    font-size: clamp(17px, 20.736px, 22px);
    line-height: 1.35;
    font-weight: 700;
    letter-spacing: -0.6px;

    text-align: left;

    cursor: pointer;
    overflow: hidden;

    transition:
        transform 150ms cubic-bezier(0.22, 1, 0.36, 1),
        color 140ms ease,
        border-color 140ms ease,
        background-color 140ms ease,
        box-shadow 140ms ease;
}

.position-card::before {
    content: "";

    position: absolute;
    inset: 0;

    opacity: 0;

    background:
        linear-gradient(
            100deg,
            rgba(77, 181, 251, 0.22),
            rgba(42, 94, 150, 0.08)
        );

    pointer-events: none;

    transition:
        opacity 140ms ease;
}

.position-card:hover {
    transform: translateY(-5px);

    color: #ffffff;

    border-color:
        rgba(255, 255, 255, 0.42);

    box-shadow:
        0 17px 34px
        rgba(0, 0, 0, 0.25);
}

.position-card.selected {
    transform: translateY(-2px);

    color: #ffffff;

    border-color: var(--selected-blue);

    background:
        rgba(48, 99, 158, 0.46);

    box-shadow:
        inset 0 0 0 1px
        rgba(77, 181, 251, 0.28),
        0 15px 32px
        rgba(24, 117, 190, 0.20);
}

.position-card.selected::before {
    opacity: 1;
}

.position-card.selected:hover {
    transform: translateY(-5px);
}

.position-card:focus-visible {
    outline:
        3px solid
        rgba(77, 181, 251, 0.78);

    outline-offset: 4px;
}

/* ========================================================
   Q7 가장 중요한 능력 카드
======================================================== */

.priority-grid {
    margin-top: 94px;
    margin-inline: auto;

    width: min(640px, 100%);

    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 22px 28px;
}

.priority-card {
    position: relative;

    width: 100%;
    min-height: 82px;

    margin: 0;
    padding: 0 38px;

    display: flex;
    align-items: center;

    color: rgba(255, 255, 255, 0.84);
    background:
        linear-gradient(
            100deg,
            rgba(20, 29, 44, 0.84),
            rgba(13, 21, 35, 0.76)
        );

    border:
        2px solid
        rgba(255, 255, 255, 0.20);

    border-radius: 13px;

    box-shadow:
        0 10px 24px
        rgba(0, 0, 0, 0.14);

    font-size: clamp(17px, 20.736px, 22px);
    line-height: 1.35;
    font-weight: 700;
    letter-spacing: -0.6px;

    text-align: left;

    cursor: pointer;
    overflow: hidden;

    transition:
        transform 150ms cubic-bezier(0.22, 1, 0.36, 1),
        color 140ms ease,
        border-color 140ms ease,
        background-color 140ms ease,
        box-shadow 140ms ease;
}

.priority-card::before {
    content: "";

    position: absolute;
    inset: 0;

    opacity: 0;

    background:
        linear-gradient(
            100deg,
            rgba(77, 181, 251, 0.22),
            rgba(42, 94, 150, 0.08)
        );

    pointer-events: none;

    transition:
        opacity 140ms ease;
}

.priority-card:hover {
    transform: translateY(-6px);

    color: #ffffff;

    border-color:
        rgba(255, 255, 255, 0.42);

    box-shadow:
        0 17px 34px
        rgba(0, 0, 0, 0.25);
}

.priority-card.selected {
    transform: translateY(-2px);

    color: #ffffff;

    border-color: var(--selected-blue);

    background:
        rgba(48, 99, 158, 0.46);

    box-shadow:
        inset 0 0 0 1px
        rgba(77, 181, 251, 0.28),
        0 15px 32px
        rgba(24, 117, 190, 0.20);
}

.priority-card.selected::before {
    opacity: 1;
}

.priority-card.selected:hover {
    transform: translateY(-6px);
}

.priority-card:focus-visible {
    outline:
        3px solid
        rgba(77, 181, 251, 0.78);

    outline-offset: 4px;
}

/* ========================================================
   Q8 게임 경험 수준 카드
======================================================== */

.experience-grid {
    margin-top: 60px;
    margin-inline: auto;

    width: min(680px, 100%);

    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}

.experience-card {
    position: relative;

    width: 100%;
    min-height: 82px;

    margin: 0;
    padding: 16px 38px;

    display: flex;
    align-items: center;
    justify-content: flex-start;

    color: rgba(255, 255, 255, 0.84);
    background:
        linear-gradient(
            100deg,
            rgba(20, 29, 44, 0.84),
            rgba(13, 21, 35, 0.76)
        );

    border:
        2px solid
        rgba(255, 255, 255, 0.20);

    border-radius: 13px;

    box-shadow:
        0 10px 24px
        rgba(0, 0, 0, 0.14);

    text-align: left;
    cursor: pointer;
    overflow: hidden;

    transition:
        transform 150ms cubic-bezier(0.22, 1, 0.36, 1),
        color 140ms ease,
        border-color 140ms ease,
        background-color 140ms ease,
        box-shadow 140ms ease;
}

.experience-card::before {
    content: "";

    position: absolute;
    inset: 0;

    opacity: 0;

    background:
        linear-gradient(
            100deg,
            rgba(77, 181, 251, 0.22),
            rgba(42, 94, 150, 0.08)
        );

    pointer-events: none;

    transition:
        opacity 140ms ease;
}

.experience-card-title {
    position: relative;
    z-index: 2;
    flex-shrink: 0;

    font-size: clamp(18px, 22.656px, 24px);
    line-height: 1.2;
    font-weight: 800;
    letter-spacing: -0.6px;
}


.experience-card:hover {
    transform: translateY(-6px);

    color: #ffffff;

    border-color:
        rgba(255, 255, 255, 0.42);

    box-shadow:
        0 17px 34px
        rgba(0, 0, 0, 0.25);
}

.experience-card.selected {
    transform: translateY(-2px);

    color: #ffffff;

    border-color: var(--selected-blue);
    background: rgba(48, 99, 158, 0.46);

    box-shadow:
        inset 0 0 0 1px
        rgba(77, 181, 251, 0.28),
        0 15px 32px
        rgba(24, 117, 190, 0.20);
}

.experience-card.selected::before {
    opacity: 1;
}

.experience-card.selected:hover {
    transform: translateY(-6px);
}

.experience-card:focus-visible {
    outline:
        3px solid
        rgba(77, 181, 251, 0.78);

    outline-offset: 4px;
}

/* ========================================================
   모든 답변 완료 후 표시되는 결과보기 버튼
======================================================== */

.result-button {
    position: absolute;
    z-index: 18;

    left: calc(117.12px + min(556.8px, 557.5px));
    bottom: 170.64px;

    width: 280px;
    height: 104px;

    margin: 0;
    padding: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #ffffff;
    background: var(--accent-orange);
    border: 0;
    border-radius: 0;

    font-size: clamp(26px, 34.56px, 36px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: -1px;

    opacity: 0;
    visibility: hidden;
    transform: translate(-50%, 14px);
    pointer-events: none;
    cursor: pointer;

    box-shadow:
        0 14px 30px
        rgba(0, 0, 0, 0.24);

    transition:
        opacity 220ms ease,
        visibility 0s linear 220ms,
        transform 220ms cubic-bezier(0.22, 1, 0.36, 1),
        background-color 130ms ease,
        box-shadow 130ms ease;
}

.result-button.visible {
    opacity: 1;
    visibility: visible;
    transform: translate(-50%, 0);
    pointer-events: auto;

    transition:
        opacity 220ms ease,
        visibility 0s,
        transform 220ms cubic-bezier(0.22, 1, 0.36, 1),
        background-color 130ms ease,
        box-shadow 130ms ease;
}

.result-button.visible:hover {
    background: var(--accent-orange-hover);
    transform: translate(-50%, -5px);

    box-shadow:
        0 20px 38px
        rgba(0, 0, 0, 0.30);
}

.result-button.visible:active {
    transform: translate(-50%, 0) scale(0.988);
}

.result-button.submitted {
    background: #3f9fe0;
}

/* ========================================================
   추천 결과 화면
======================================================== */

.result-screen {
    z-index: 14;
}

.result-heading {
    position: absolute;
    z-index: 12;

    top: 196.56px;
    left: 182.4px;

    width: min(931.2px, 930px);

    text-align: center;
}

.result-title {
    margin: 0;

    color: #ffffff;

    font-size: clamp(44px, 68.16px, 68px);
    line-height: 1.04;
    font-weight: 850;
    letter-spacing: -3px;

    text-shadow:
        0 4px 14px
        rgba(0, 0, 0, 0.28);
}

.result-title span {
    color: var(--accent-yellow);
}

.result-description {
    margin: 28px 0 0;

    color: rgba(255, 255, 255, 0.80);

    font-size: clamp(19px, 27.264px, 28px);
    line-height: 1.35;
    font-weight: 650;
    letter-spacing: -1px;
}

.result-scroll-shell {
    position: absolute;
    z-index: 13;

    top: 394.2px;
    left: 182.4px;

    width: min(931.2px, 930px);
    height: 459px;

    min-height: 390px;
    max-height: 500px;
}

.result-scroll-container {
    width: 100%;
    height: 100%;

    padding: 0 14px 28px 0;

    overflow-x: hidden;
    overflow-y: scroll;
    overscroll-behavior: contain;
    scrollbar-gutter: stable;

    scroll-behavior: smooth;

    scrollbar-width: thin;
    scrollbar-color:
        rgba(237, 108, 37, 0.92)
        rgba(255, 255, 255, 0.10);
}

.result-scroll-container::-webkit-scrollbar {
    width: 12px;
}

.result-scroll-container::-webkit-scrollbar-track {
    background:
        rgba(255, 255, 255, 0.09);

    border-radius: 999px;
}

.result-scroll-container::-webkit-scrollbar-thumb {
    min-height: 74px;

    background:
        linear-gradient(
            180deg,
            var(--accent-orange-hover),
            var(--accent-orange)
        );

    border:
        3px solid
        rgba(12, 20, 34, 0.82);

    border-radius: 999px;
}

.result-scroll-container::-webkit-scrollbar-thumb:hover {
    background: var(--accent-orange-hover);
}

.result-content {
    min-height: 100%;

    padding: 0 2px 32px;
}

.result-content[hidden],
.result-loading[hidden],
.result-error[hidden] {
    display: none !important;
}

.result-loading,
.result-error {
    width: 100%;
    min-height: 360px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 14px;

    color: rgba(255, 255, 255, 0.78);

    background:
        rgba(14, 21, 35, 0.74);

    border:
        1px solid
        rgba(255, 255, 255, 0.15);

    border-radius: 18px;

    box-shadow:
        0 18px 42px
        rgba(0, 0, 0, 0.22);
}

.result-loading strong,
.result-error strong {
    color: #ffffff;
    font-size: clamp(20px, 25.92px, 27px);
}

.result-loading span:last-child,
.result-error p {
    margin: 0;

    font-size: clamp(14px, 18.24px, 18px);
    text-align: center;
}

.result-spinner {
    width: 54px;
    height: 54px;

    border:
        6px solid
        rgba(255, 255, 255, 0.18);

    border-top-color: var(--accent-orange);
    border-radius: 50%;

    animation:
        result-spinner-rotate
        760ms linear infinite;
}

.result-retry-button {
    min-width: 180px;
    height: 58px;

    margin-top: 10px;
    padding: 0 24px;

    color: #ffffff;
    background: var(--accent-orange);

    border: 0;
    border-radius: 8px;

    font-size: 18px;
    font-weight: 800;

    cursor: pointer;

    transition:
        transform 140ms ease,
        background-color 140ms ease;
}

.result-retry-button:hover {
    background: var(--accent-orange-hover);
    transform: translateY(-3px);
}

.recommendation-card {
    position: relative;

    color: #ffffff;

    background:
        linear-gradient(
            110deg,
            rgba(28, 28, 33, 0.87),
            rgba(13, 20, 36, 0.83)
        );

    border:
        1px solid
        rgba(255, 255, 255, 0.14);

    box-shadow:
        0 18px 42px
        rgba(0, 0, 0, 0.22);

    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

.primary-recommendation {
    min-height: 365px;

    padding: 30px;

    display: grid;
    grid-template-columns: 285px minmax(0, 1fr);
    gap: 34px;

    border-radius: 18px;
}

.hero-image-wrap {
    position: relative;

    overflow: hidden;

    background:
        linear-gradient(
            145deg,
            rgba(255, 255, 255, 0.09),
            rgba(0, 0, 0, 0.18)
        );

    border-radius: 12px;
}

.primary-image-wrap {
    width: 285px;
    height: 305px;
}

.hero-image {
    width: 100%;
    height: 100%;

    display: block;
    object-fit: cover;
    object-position: center;

    user-select: none;
}

.hero-image-wrap.image-missing {
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-image-fallback {
    padding: 20px;

    color: rgba(255, 255, 255, 0.72);

    font-size: 22px;
    font-weight: 800;
    text-align: center;
}

.rank-chip {
    position: absolute;
    z-index: 3;

    min-width: 64px;
    height: 34px;

    padding: 0 12px;

    display: flex;
    align-items: center;
    justify-content: center;

    color: #15100a;
    background: var(--accent-yellow);

    border:
        1px solid
        rgba(255, 255, 255, 0.22);

    border-radius: 999px;

    font-size: 14px;
    font-weight: 900;
    letter-spacing: 0.5px;

    box-shadow:
        0 5px 14px
        rgba(0, 0, 0, 0.30);
}

/* 1순위: 금색 */
.rank-one-chip {
    top: 14px;
    left: 14px;

    color: #2b1b05;

    background:
        linear-gradient(
            135deg,
            #fff4b8 0%,
            #ffd86a 30%,
            #f0b62e 62%,
            #b9780f 100%
        );

    border-color:
        rgba(255, 245, 191, 0.62);

    box-shadow:
        inset 0 1px 0
        rgba(255, 255, 255, 0.78),
        0 0 16px
        rgba(255, 182, 46, 0.22),
        0 5px 14px
        rgba(0, 0, 0, 0.30);
}

.compact-rank-chip {
    top: 10px;
    left: 10px;
}

/* 2순위: 은색 */
.rank-second-chip {
    color: #202833;

    background:
        linear-gradient(
            135deg,
            #f7f9fc 0%,
            #d6dce5 38%,
            #aeb7c4 68%,
            #8793a2 100%
        );

    border-color:
        rgba(255, 255, 255, 0.56);

    box-shadow:
        inset 0 1px 0
        rgba(255, 255, 255, 0.72),
        0 5px 14px
        rgba(0, 0, 0, 0.30);
}

/* 3순위: 동색 */
.rank-third-chip {
    color: #2c160d;

    background:
        linear-gradient(
            135deg,
            #e8ad78 0%,
            #c27a48 40%,
            #9c5934 70%,
            #743c25 100%
        );

    border-color:
        rgba(255, 221, 190, 0.48);

    box-shadow:
        inset 0 1px 0
        rgba(255, 235, 215, 0.44),
        0 5px 14px
        rgba(0, 0, 0, 0.30);
}

.primary-result-info {
    min-width: 0;

    padding: 8px 0 0;
}

.result-hero-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
}

.result-hero-name-block {
    min-width: 0;

    display: flex;
    align-items: baseline;
    gap: 12px;
}

.result-hero-name-en {
    overflow: hidden;

    color: #ffffff;

    font-size: clamp(25px, 34.176px, 34px);
    line-height: 1.1;
    font-weight: 900;
    letter-spacing: 0.7px;

    text-overflow: ellipsis;
    white-space: nowrap;
}

.result-hero-name-ko {
    color: rgba(255, 255, 255, 0.68);

    font-size: clamp(17px, 20.16px, 21px);
    font-weight: 750;

    white-space: nowrap;
}

.match-pill {
    flex-shrink: 0;

    min-width: 144px;
    height: 48px;

    padding: 0 20px;

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 9px;

    color: var(--accent-yellow);
    background: rgba(13, 18, 30, 0.70);

    border:
        1px solid
        rgba(255, 182, 46, 0.50);

    border-radius: 999px;

    font-size: 17px;
    font-weight: 850;
}

.match-pill::before {
    content: "";

    width: 10px;
    height: 10px;

    background: var(--accent-yellow);
    border-radius: 50%;

    box-shadow:
        0 0 12px
        rgba(255, 182, 46, 0.60);
}

.primary-summary {
    margin: 26px 0 0;

    color: rgba(255, 255, 255, 0.88);

    font-size: clamp(17px, 20.736px, 21px);
    line-height: 1.7;
    font-weight: 620;
    letter-spacing: -0.3px;
}

.result-divider {
    width: 100%;
    height: 1px;

    margin: 26px 0 22px;

    background:
        rgba(255, 255, 255, 0.15);
}

.reason-title {
    margin: 0 0 16px;

    color: var(--accent-yellow);

    font-size: 19px;
    font-weight: 850;
}

.reason-list {
    margin: 0;
    padding: 0;

    display: grid;
    gap: 13px;

    list-style: none;
}

.reason-item {
    display: grid;
    grid-template-columns: 22px minmax(0, 1fr);
    align-items: start;
    gap: 12px;

    color: rgba(255, 255, 255, 0.72);

    font-size: clamp(14px, 17.664px, 18px);
    line-height: 1.5;
}

.reason-check-icon {
    width: 20px;
    height: 20px;

    margin-top: 1px;

    object-fit: contain;
}

.secondary-result-grid {
    margin-top: 28px;

    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 24px;
}

.compact-recommendation {
    min-height: 235px;

    padding: 20px;

    display: grid;
    grid-template-columns: 174px minmax(0, 1fr);
    gap: 20px;

    border-radius: 18px;
}

.compact-image-wrap {
    width: 174px;
    height: 190px;
}


.compact-result-info {
    min-width: 0;

    padding-top: 5px;
}

.compact-match {
    width: fit-content;

    margin-left: auto;
    padding: 7px 12px;

    color: var(--accent-yellow);
    background: rgba(10, 16, 28, 0.72);

    border-radius: 7px;

    font-size: 14px;
    font-weight: 850;
}

.compact-name-en {
    margin: 15px 0 0;

    overflow: hidden;

    color: #ffffff;

    font-size: clamp(20px, 24.576px, 25px);
    line-height: 1.1;
    font-weight: 900;

    text-overflow: ellipsis;
    white-space: nowrap;
}

.compact-name-ko {
    margin: 8px 0 0;

    color: rgba(255, 255, 255, 0.60);

    font-size: 15px;
    font-weight: 700;
}

.compact-summary {
    margin: 22px 0 0;

    display: -webkit-box;
    overflow: hidden;

    color: rgba(255, 255, 255, 0.72);

    font-size: 14px;
    line-height: 1.62;
    font-weight: 590;

    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

.result-restart-button {
    position: absolute;

    left: calc(182.4px + min(465.6px, 465px));
    bottom: 63.72px;

    width: 280px;
    height: 104px;

    transform: translateX(-50%);

    font-size: 32px;
}

.result-restart-button:hover {
    transform:
        translateX(-50%)
        translateY(-4px);
}

.result-restart-button:active {
    transform:
        translateX(-50%)
        translateY(0)
        scale(0.985);
}

.result-screen.animate-in .result-heading {
    animation:
        float-up 420ms
        cubic-bezier(0.22, 1, 0.36, 1)
        0ms both;
}

.result-screen.animate-in .result-scroll-shell {
    animation:
        float-up 460ms
        cubic-bezier(0.22, 1, 0.36, 1)
        70ms both;
}

.result-screen.animate-in .result-restart-button {
    animation:
        float-up-centered 460ms
        cubic-bezier(0.22, 1, 0.36, 1)
        130ms both;
}

@keyframes result-spinner-rotate {
    to {
        transform: rotate(360deg);
    }
}

@keyframes float-up-centered {
    from {
        opacity: 0;
        transform:
            translateX(-50%)
            translateY(30px);
    }

    to {
        opacity: 1;
        transform:
            translateX(-50%)
            translateY(0);
    }
}

/* ========================================================
   하단 이동 및 진행도
======================================================== */

.quiz-navigation {
    position: absolute;

    z-index: 16;

    left: 117.12px;
    bottom: 72.36px;

    width: 1113.6px;
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

    margin: 0;
    padding: 0;

    background: transparent;
    border: 0;
    border-radius: 50%;

    cursor: default;

    transition:
        background-color 110ms ease,
        transform 140ms cubic-bezier(0.22, 1, 0.36, 1),
        box-shadow 140ms ease,
        opacity 110ms ease;
}

.progress-dot:disabled {
    opacity: 1;
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

.progress-dot.clickable {
    cursor: pointer;
}

.progress-dot.clickable:hover {
    transform: scale(1.28);

    box-shadow:
        0 0 0 7px
        rgba(255, 255, 255, 0.11);
}

.progress-dot.clickable:focus-visible {
    outline:
        3px solid
        rgba(77, 181, 251, 0.82);

    outline-offset: 5px;
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
   고정 디자인 캔버스

   1920 × 1080 기준으로 모든 요소를 배치한 뒤, JavaScript가
   브라우저의 실제 표시 영역에 맞게 캔버스 전체를 동일 비율로
   축소 또는 확대합니다. 따라서 화면 크기가 달라도 요소 간
   비율과 중심축이 유지됩니다.
======================================================== */

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

    const viewport = parentElement.querySelector("#ow-viewport");
    const app = parentElement.querySelector("#ow-app");

    if (!viewport || !app) {
        return;
    }

    const DESIGN_WIDTH = 1920;
    const DESIGN_HEIGHT = 1080;
    const viewportResizeController = new AbortController();

    function fitDesignCanvas() {
        const viewportWidth = Math.max(1, window.innerWidth);
        const viewportHeight = Math.max(1, window.innerHeight);

        /*
        모든 화면을 1920×1080 기준 비율로 동일하게 축소합니다.
        cover 방식은 화면 너비를 채우는 대신 UI 전체를 확대하고
        하단 요소를 아래로 밀어낼 수 있으므로 사용하지 않습니다.
        */
        const scale = Math.max(
            0.1,
            Math.min(
                viewportWidth / DESIGN_WIDTH,
                viewportHeight / DESIGN_HEIGHT
            )
        );

        const renderedWidth = DESIGN_WIDTH * scale;
        const renderedHeight = DESIGN_HEIGHT * scale;

        /*
        남는 공간은 좌우 또는 상하에 동일하게 배분합니다.
        따라서 창 크기가 달라져도 질문, 카드, 화살표와 진행도의
        크기 및 상대 위치가 항상 같은 비율로 유지됩니다.
        */
        const offsetX =
            (viewportWidth - renderedWidth) / 2;

        const offsetY =
            (viewportHeight - renderedHeight) / 2;

        app.style.transform =
            `translate3d(${offsetX}px, ${offsetY}px, 0) scale(${scale})`;

        app.dataset.viewportScale = String(scale);
        app.dataset.fitMode = "contain";

        viewport.classList.add("is-fitted");
    }

    fitDesignCanvas();

    window.addEventListener(
        "resize",
        fitDesignCanvas,
        { signal: viewportResizeController.signal }
    );

    if (window.visualViewport) {
        window.visualViewport.addEventListener(
            "resize",
            fitDesignCanvas,
            { signal: viewportResizeController.signal }
        );
    }

    const screenFitObserver =
        new MutationObserver(() => {
            fitDesignCanvas();
        });

    screenFitObserver.observe(
        app,
        {
            attributes: true,
            attributeFilter: ["data-screen"],
        }
    );


    const screens = {
        home: parentElement.querySelector("#home-screen"),
        welcome: parentElement.querySelector("#welcome-screen"),
        quiz: parentElement.querySelector("#quiz-screen"),
        result: parentElement.querySelector("#result-screen"),
    };

    const questions = {
        1: parentElement.querySelector("#question-1"),
        2: parentElement.querySelector("#question-2"),
        3: parentElement.querySelector("#question-3"),
        4: parentElement.querySelector("#question-4"),
        5: parentElement.querySelector("#question-5"),
        6: parentElement.querySelector("#question-6"),
        7: parentElement.querySelector("#question-7"),
        8: parentElement.querySelector("#question-8"),
    };

    const homeButton = parentElement.querySelector("#home-button");
    const homeStartButton = parentElement.querySelector("#home-start-button");
    const welcomeStartButton = parentElement.querySelector("#welcome-start-button");

    const previousButton = parentElement.querySelector("#previous-question-button");
    const nextButton = parentElement.querySelector("#next-question-button");
    const resultButton = parentElement.querySelector("#result-button");
    const restartButton = parentElement.querySelector("#restart-button");
    const resultScrollContainer = parentElement.querySelector("#result-scroll-container");
    const resultLoading = parentElement.querySelector("#result-loading");
    const resultError = parentElement.querySelector("#result-error");
    const resultErrorMessage = parentElement.querySelector("#result-error-message");
    const resultContent = parentElement.querySelector("#result-content");

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

    const positionCards = Array.from(
        parentElement.querySelectorAll(
            "#question-6 .position-card"
        )
    );

    const priorityCards = Array.from(
        parentElement.querySelectorAll(
            "#question-7 .priority-card"
        )
    );

    const experienceCards = Array.from(
        parentElement.querySelectorAll(
            "#question-8 .experience-card"
        )
    );

    const progressDots = Array.from(
        parentElement.querySelectorAll(".progress-dot")
    );

    const configuredApiBaseUrl = __API_BASE_URL__;

    const apiBaseUrl =
        configuredApiBaseUrl
        || `${window.location.protocol}//${window.location.hostname}:8000`;

    const assetVersion = "20260617-2";

    function uiAssetUrl(assetPath) {
        const encodedPath = String(assetPath)
            .split("/")
            .map((part) => encodeURIComponent(part))
            .join("/");

        return `${apiBaseUrl}/assets/${encodedPath}?v=${assetVersion}`;
    }

    const imageUris = {
        leftGray: uiAssetUrl("icons/arrow_left_gray.png"),
        leftWhite: uiAssetUrl("icons/arrow_left_white.png"),
        leftOrange: uiAssetUrl("icons/arrow_left_orange.png"),
        rightGray: uiAssetUrl("icons/arrow_right_gray.png"),
        rightWhite: uiAssetUrl("icons/arrow_right_white.png"),
        rightOrange: uiAssetUrl("icons/arrow_right_orange.png"),
        check: uiAssetUrl("icons/check_icon.png"),
    };

    const uiAssetImages = Array.from(
        parentElement.querySelectorAll(
            "img[data-asset-path]"
        )
    );

    const essentialAssetPromises = [];

    uiAssetImages.forEach((image) => {
        const assetPath = image.dataset.assetPath;

        if (!assetPath) {
            return;
        }

        if (image.dataset.essentialAsset === "true") {
            essentialAssetPromises.push(
                new Promise((resolve) => {
                    if (image.complete) {
                        resolve();
                        return;
                    }

                    image.addEventListener(
                        "load",
                        resolve,
                        { once: true }
                    );

                    image.addEventListener(
                        "error",
                        resolve,
                        { once: true }
                    );
                })
            );
        }

        image.src = uiAssetUrl(assetPath);
    });

    Promise.race([
        Promise.allSettled(essentialAssetPromises),
        new Promise((resolve) => {
            window.setTimeout(resolve, 4000);
        }),
    ]).finally(() => {
        viewport.classList.remove("assets-loading");
        viewport.classList.add("assets-ready");
    });

    const state = app.__owState ?? {
        screen: "home",
        currentQuestion: 1,
        answers: {
            role: null,
            range: null,
            aim: null,
            mobility: null,
            aggression: null,
            position: null,
            priority: null,
            experience: null,
        },
        isQuestionAnimating: false,
        isResultLoading: false,
        recommendations: null,
        resultError: null,
    };
    app.__owState = state;

    // 기존 상태 객체에 새 질문 값이 없을 때를 대비합니다.
    state.answers.range ??= null;
    state.answers.aim ??= null;
    state.answers.mobility ??= null;
    state.answers.aggression ??= null;
    state.answers.position ??= null;
    state.answers.priority ??= null;
    state.answers.experience ??= null;
    state.isResultLoading ??= false;
    state.recommendations ??= null;
    state.resultError ??= null;

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

        if (screenName === "result") {
            restartClassAnimation(
                screens.result,
                "animate-in"
            );
            clearAnimationClass(
                screens.result,
                "animate-in",
                760
            );

            resultScrollContainer.scrollTop = 0;
        }
    }

    function resetQuiz() {
        state.currentQuestion = 1;
        state.answers.role = null;
        state.answers.range = null;
        state.answers.aim = null;
        state.answers.mobility = null;
        state.answers.aggression = null;
        state.answers.position = null;
        state.answers.priority = null;
        state.answers.experience = null;

        roleCards.forEach((card) => {
            card.classList.remove("selected");
            card.setAttribute("aria-checked", "false");
        });

        positionCards.forEach((card) => {
            card.classList.remove("selected");
            card.setAttribute("aria-checked", "false");
        });

        priorityCards.forEach((card) => {
            card.classList.remove("selected");
            card.setAttribute("aria-checked", "false");
        });

        experienceCards.forEach((card) => {
            card.classList.remove("selected");
            card.setAttribute("aria-checked", "false");
        });

        state.isResultLoading = false;
        state.recommendations = null;
        state.resultError = null;
        resultContent.replaceChildren();
        resultContent.hidden = true;
        resultLoading.hidden = false;
        resultError.hidden = true;

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

        resultButton.classList.remove("visible", "submitted");
        resultButton.disabled = true;
        resultButton.setAttribute("aria-hidden", "true");

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

    function getCompletedQuestions() {
        return {
            1: state.answers.role !== null,
            2: state.answers.range !== null,
            3: state.answers.aim !== null,
            4: state.answers.mobility !== null,
            5: state.answers.aggression !== null,
            6: state.answers.position !== null,
            7: state.answers.priority !== null,
            8: state.answers.experience !== null,
        };
    }

    function areAllAnswersComplete() {
        return Object.values(
            getCompletedQuestions()
        ).every(Boolean);
    }

    function updateProgressDots() {
        const completedQuestions =
            getCompletedQuestions();

        progressDots.forEach((dot, index) => {
            const questionNumber = index + 1;
            const isCurrent =
                questionNumber === state.currentQuestion;
            const isCompleted =
                completedQuestions[questionNumber] ?? false;

            dot.classList.remove(
                "pending",
                "completed",
                "current",
                "clickable"
            );

            dot.removeAttribute("aria-current");

            if (isCurrent) {
                dot.classList.add("current");
                dot.disabled = true;
                dot.setAttribute("aria-current", "step");
                dot.setAttribute(
                    "aria-label",
                    `${questionNumber}번 질문, 현재 화면`
                );
                return;
            }

            if (isCompleted) {
                dot.classList.add(
                    "completed",
                    "clickable"
                );
                dot.disabled = false;
                dot.setAttribute(
                    "aria-label",
                    `${questionNumber}번 질문으로 이동`
                );
                return;
            }

            dot.classList.add("pending");
            dot.disabled = true;
            dot.setAttribute(
                "aria-label",
                `${questionNumber}번 질문, 아직 답변하지 않음`
            );
        });
    }

    function updateResultButton() {
        const shouldShow =
            state.currentQuestion === 8
            && areAllAnswersComplete();

        resultButton.classList.toggle(
            "visible",
            shouldShow
        );

        resultButton.classList.remove("submitted");
        resultButton.textContent = "결과보기";
        resultButton.disabled = !shouldShow;
        resultButton.setAttribute(
            "aria-hidden",
            String(!shouldShow)
        );
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
            6: state.answers.position !== null,
            7: state.answers.priority !== null,
            8: state.answers.experience !== null,
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
        updateResultButton();
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

    function selectPosition(card) {
        const selectedPosition =
            card.dataset.position;

        const validPositions = [
            "frontline",
            "midline",
            "backline",
            "flank",
            "flexible",
        ];

        if (
            !validPositions.includes(
                selectedPosition
            )
        ) {
            return;
        }

        state.answers.position =
            selectedPosition;

        positionCards.forEach((positionCard) => {
            const isSelected =
                positionCard.dataset.position
                === selectedPosition;

            positionCard.classList.toggle(
                "selected",
                isSelected
            );

            positionCard.setAttribute(
                "aria-checked",
                String(isSelected)
            );
        });

        updateQuizUI();
    }

    function selectPriority(card) {
        const selectedPriority =
            card.dataset.priority;

        const validPriorities = [
            "damage",
            "survival",
            "protection",
            "healing",
            "control",
            "easy",
        ];

        if (
            !validPriorities.includes(
                selectedPriority
            )
        ) {
            return;
        }

        state.answers.priority =
            selectedPriority;

        priorityCards.forEach((priorityCard) => {
            const isSelected =
                priorityCard.dataset.priority
                === selectedPriority;

            priorityCard.classList.toggle(
                "selected",
                isSelected
            );

            priorityCard.setAttribute(
                "aria-checked",
                String(isSelected)
            );
        });

        updateQuizUI();
    }

    function selectExperience(card) {
        const selectedExperience =
            card.dataset.experience;

        const validExperiences = [
            "beginner",
            "intermediate",
            "advanced",
        ];

        if (
            !validExperiences.includes(
                selectedExperience
            )
        ) {
            return;
        }

        state.answers.experience =
            selectedExperience;

        experienceCards.forEach((experienceCard) => {
            const isSelected =
                experienceCard.dataset.experience
                === selectedExperience;

            experienceCard.classList.toggle(
                "selected",
                isSelected
            );

            experienceCard.setAttribute(
                "aria-checked",
                String(isSelected)
            );
        });

        updateQuizUI();
    }

    function handleProgressDotClick(dot) {
        const targetQuestion =
            Number(dot.dataset.index);

        if (
            !Number.isInteger(targetQuestion)
            || targetQuestion === state.currentQuestion
            || !questions[targetQuestion]
        ) {
            return;
        }

        const completedQuestions =
            getCompletedQuestions();

        /*
        아직 답변하지 않은 미래 질문은 건너뛸 수 없고,
        이미 답변을 완료한 질문만 자유롭게 다시 확인합니다.
        */
        if (!completedQuestions[targetQuestion]) {
            return;
        }

        const direction =
            targetQuestion > state.currentQuestion
                ? "forward"
                : "backward";

        moveQuestion(
            targetQuestion,
            direction
        );
    }

    function escapeHtml(value) {
        return String(value ?? "")
            .replaceAll("&", "&amp;")
            .replaceAll("<", "&lt;")
            .replaceAll(">", "&gt;")
            .replaceAll('"', "&quot;")
            .replaceAll("'", "&#039;");
    }

    function formatMatchPercentage(value) {
        const numericValue = Number(value);

        if (!Number.isFinite(numericValue)) {
            return "0.0";
        }

        return numericValue.toFixed(1);
    }

    function heroImageUrl(heroId) {
        return `${apiBaseUrl}/hero-images/${encodeURIComponent(heroId)}.png`;
    }

    function createReasonItems(reasons) {
        const safeReasons = Array.isArray(reasons)
            ? reasons.slice(0, 3)
            : [];

        return safeReasons
            .map((reason) => `
                <li class="reason-item">
                    <img
                        class="reason-check-icon"
                        src="${imageUris.check}"
                        alt=""
                        draggable="false"
                    />
                    <span>${escapeHtml(reason)}</span>
                </li>
            `)
            .join("");
    }

    function createPrimaryResultCard(hero) {
        return `
            <article class="recommendation-card primary-recommendation">
                <div class="hero-image-wrap primary-image-wrap">
                    <img
                        class="hero-image"
                        src="${heroImageUrl(hero.hero_id)}"
                        alt="${escapeHtml(hero.name_ko)} 영웅 이미지"
                        draggable="false"
                    />
                    <span class="rank-chip rank-one-chip">1ST</span>
                </div>

                <div class="primary-result-info">
                    <div class="result-hero-heading">
                        <div class="result-hero-name-block">
                            <strong class="result-hero-name-en">
                                ${escapeHtml(hero.name_en)}
                            </strong>
                            <span class="result-hero-name-ko">
                                ${escapeHtml(hero.name_ko)}
                            </span>
                        </div>

                        <span class="match-pill">
                            일치율 ${formatMatchPercentage(hero.match_percentage)}%
                        </span>
                    </div>

                    <p class="primary-summary">
                        “${escapeHtml(hero.summary)}”
                    </p>

                    <div class="result-divider"></div>

                    <h3 class="reason-title">추천 이유</h3>
                    <ul class="reason-list">
                        ${createReasonItems(hero.reasons)}
                    </ul>
                </div>
            </article>
        `;
    }

    function createCompactResultCard(hero, rank) {
        const rankLabel =
            rank === 2
                ? "2ND"
                : "3RD";

        const rankColorClass =
            rank === 2
                ? "rank-second-chip"
                : "rank-third-chip";

        return `
            <article class="recommendation-card compact-recommendation">
                <div class="hero-image-wrap compact-image-wrap">
                    <img
                        class="hero-image"
                        src="${heroImageUrl(hero.hero_id)}"
                        alt="${escapeHtml(hero.name_ko)} 영웅 이미지"
                        draggable="false"
                    />
                    <span
                        class="rank-chip compact-rank-chip ${rankColorClass}"
                        aria-label="${rank}순위"
                    >
                        ${rankLabel}
                    </span>
                </div>

                <div class="compact-result-info">
                    <div class="compact-match">
                        일치율 ${formatMatchPercentage(hero.match_percentage)}%
                    </div>

                    <h2 class="compact-name-en">
                        ${escapeHtml(hero.name_en)}
                    </h2>

                    <p class="compact-name-ko">
                        ${escapeHtml(hero.name_ko)}
                    </p>

                    <p class="compact-summary">
                        ${escapeHtml(hero.summary)}
                    </p>
                </div>
            </article>
        `;
    }

    function installHeroImageFallbacks() {
        const images = Array.from(
            resultContent.querySelectorAll(".hero-image")
        );

        images.forEach((image) => {
            image.addEventListener("error", () => {
                const wrapper = image.closest(".hero-image-wrap");

                if (!wrapper) {
                    return;
                }

                const heroName = image.alt
                    .replace(" 영웅 이미지", "");

                image.remove();
                wrapper.classList.add("image-missing");

                const fallback = document.createElement("span");
                fallback.className = "hero-image-fallback";
                fallback.textContent = heroName;
                wrapper.prepend(fallback);
            }, { once: true });
        });
    }

    function renderRecommendations(recommendations) {
        if (
            !Array.isArray(recommendations)
            || recommendations.length < 1
        ) {
            throw new Error("추천 결과가 비어 있습니다.");
        }

        const primaryHero = recommendations[0];
        const secondaryHeroes = recommendations.slice(1, 3);

        resultContent.innerHTML = `
            ${createPrimaryResultCard(primaryHero)}
            <div class="secondary-result-grid">
                ${secondaryHeroes
                    .map((hero, index) =>
                        createCompactResultCard(hero, index + 2)
                    )
                    .join("")}
            </div>
        `;

        installHeroImageFallbacks();

        resultLoading.hidden = true;
        resultError.hidden = true;
        resultContent.hidden = false;
        resultScrollContainer.scrollTop = 0;
    }

    function showResultLoading() {
        resultContent.hidden = true;
        resultError.hidden = true;
        resultLoading.hidden = false;
        resultScrollContainer.scrollTop = 0;
    }

    function showResultError(message) {
        resultLoading.hidden = true;
        resultContent.hidden = true;
        resultError.hidden = false;
        resultErrorMessage.textContent = message;
        resultScrollContainer.scrollTop = 0;
    }

    async function requestRecommendations() {
        if (
            !areAllAnswersComplete()
            || state.isResultLoading
        ) {
            return;
        }

        state.isResultLoading = true;
        state.resultError = null;

        showResultLoading();
        showScreen("result");

        try {
            const response = await fetch(
                `${apiBaseUrl}/recommend`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(state.answers),
                }
            );

            let payload = null;

            try {
                payload = await response.json();
            } catch {
                payload = null;
            }

            if (!response.ok) {
                const errorMessage =
                    payload?.detail
                    || payload?.message
                    || `추천 API 요청에 실패했습니다. (${response.status})`;

                throw new Error(errorMessage);
            }

            const recommendations = payload?.recommendations;

            if (!Array.isArray(recommendations)) {
                throw new Error("추천 API 응답 형식이 올바르지 않습니다.");
            }

            state.recommendations = recommendations;
            state.submittedAnswers = { ...state.answers };
            renderRecommendations(recommendations);
        } catch (error) {
            const message = error instanceof Error
                ? error.message
                : "추천 결과를 불러오는 중 오류가 발생했습니다.";

            state.resultError = message;
            showResultError(message);
        } finally {
            state.isResultLoading = false;
        }
    }

    function handleResultButton() {
        requestRecommendations();
    }

    function handlePrevious() {
        if (state.currentQuestion === 8) {
            moveQuestion(7, "backward");
            return;
        }

        if (state.currentQuestion === 7) {
            moveQuestion(6, "backward");
            return;
        }

        if (state.currentQuestion === 6) {
            moveQuestion(5, "backward");
            return;
        }

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
            return;
        }

        if (
            state.currentQuestion === 5
            && state.answers.aggression !== null
        ) {
            moveQuestion(6, "forward");
            return;
        }

        if (
            state.currentQuestion === 6
            && state.answers.position !== null
        ) {
            moveQuestion(7, "forward");
            return;
        }

        if (
            state.currentQuestion === 7
            && state.answers.priority !== null
        ) {
            moveQuestion(8, "forward");
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

        if (button === resultButton) {
            handleResultButton();
            return;
        }

        if (button === restartButton) {
            goHome();
            return;
        }

        if (button.classList.contains("result-retry-button")) {
            requestRecommendations();
            return;
        }

        if (button.classList.contains("progress-dot")) {
            handleProgressDotClick(button);
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
            return;
        }

        if (button.classList.contains("position-card")) {
            selectPosition(button);
            return;
        }

        if (button.classList.contains("priority-card")) {
            selectPriority(button);
            return;
        }

        if (button.classList.contains("experience-card")) {
            selectExperience(button);
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

    positionCards.forEach((card) => {
        const isSelected =
            card.dataset.position
            === state.answers.position;

        card.classList.toggle(
            "selected",
            isSelected
        );

        card.setAttribute(
            "aria-checked",
            String(isSelected)
        );
    });

    priorityCards.forEach((card) => {
        const isSelected =
            card.dataset.priority
            === state.answers.priority;

        card.classList.toggle(
            "selected",
            isSelected
        );

        card.setAttribute(
            "aria-checked",
            String(isSelected)
        );
    });

    experienceCards.forEach((card) => {
        const isSelected =
            card.dataset.experience
            === state.answers.experience;

        card.classList.toggle(
            "selected",
            isSelected
        );

        card.setAttribute(
            "aria-checked",
            String(isSelected)
        );
    });

    updateRangeUI();
    updateAimUI();
    updateMobilityUI();
    updateAggressionUI();
    updateQuizUI();

    if (
        state.screen === "result"
        && Array.isArray(state.recommendations)
    ) {
        renderRecommendations(
            state.recommendations
        );
    } else if (
        state.screen === "result"
        && state.resultError
    ) {
        showResultError(
            state.resultError
        );
    }

    return () => {
        abortController.abort();
        viewportResizeController.abort();
        screenFitObserver.disconnect();
    };
}
"""

APP_JS = (
    APP_JS_TEMPLATE
    .replace("__API_BASE_URL__", json.dumps(API_BASE_URL))
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
        height=1080,
    )


if __name__ == "__main__":
    main()
