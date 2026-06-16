import base64
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

BACKGROUND_PATH = (
    ASSETS_DIR
    / "backgrounds"
    / "home_background.png"
)

SYMBOL_PATH = (
    ASSETS_DIR
    / "logos"
    / "overwatch_symbol.png"
)

WORDMARK_PATH = (
    ASSETS_DIR
    / "logos"
    / "overwatch_wordmark.png"
)

CHARACTER_PATH = (
    ASSETS_DIR
    / "heroes"
    / "character.png"
)

ROLE_TANK_ICON_PATH = (
    ASSETS_DIR
    / "icons"
    / "role_tank.png"
)

ROLE_DAMAGE_ICON_PATH = (
    ASSETS_DIR
    / "icons"
    / "role_damage.png"
)

ROLE_SUPPORT_ICON_PATH = (
    ASSETS_DIR
    / "icons"
    / "role_support.png"
)

ROLE_FLEX_ICON_PATH = (
    ASSETS_DIR
    / "icons"
    / "role_flex.png"
)

ARROW_LEFT_GRAY_PATH = (
    ASSETS_DIR
    / "icons"
    / "arrow_left_gray.png"
)

ARROW_LEFT_WHITE_PATH = (
    ASSETS_DIR
    / "icons"
    / "arrow_left_white.png"
)

ARROW_LEFT_ORANGE_PATH = (
    ASSETS_DIR
    / "icons"
    / "arrow_left_orange.png"
)

ARROW_RIGHT_GRAY_PATH = (
    ASSETS_DIR
    / "icons"
    / "arrow_right_gray.png"
)

ARROW_RIGHT_WHITE_PATH = (
    ASSETS_DIR
    / "icons"
    / "arrow_right_white.png"
)

ARROW_RIGHT_ORANGE_PATH = (
    ASSETS_DIR
    / "icons"
    / "arrow_right_orange.png"
)

QUESTION_KEYS = [
    "role",
    "range",
    "aim",
    "mobility",
    "aggression",
    "position",
    "priority",
    "experience",
]


def initialize_quiz_state() -> None:
    """
    사용자의 답변을 질문 페이지 사이에서 유지합니다.
    """
    if "quiz_answers" not in st.session_state:
        st.session_state["quiz_answers"] = {}


def get_query_value(
    key: str,
    default: str | None = None,
) -> str | None:
    """
    URL 쿼리 파라미터를 문자열로 안전하게 읽습니다.
    """
    value = st.query_params.get(key, default)

    if isinstance(value, list):
        return value[0] if value else default

    return value


def build_progress_dots(
    current_question: int,
) -> str:
    """
    현재 문항은 주황색,
    완료한 이전 문항은 흰색,
    아직 답하지 않은 문항은 회색으로 표시합니다.
    """
    initialize_quiz_state()

    answers = st.session_state["quiz_answers"]
    dots: list[str] = []

    for index, question_key in enumerate(
        QUESTION_KEYS,
        start=1,
    ):
        if index == current_question:
            dot_class = "current"

        elif answers.get(question_key) is not None:
            dot_class = "completed"

        else:
            dot_class = "pending"

        dots.append(
            f'<span class="progress-dot {dot_class}"></span>'
        )

    return "".join(dots)


STUDENT_INFO = "2023204017 최유진"


# =========================================================
# 이미지 처리
# =========================================================

def image_to_data_uri(image_path: Path) -> str:
    """
    로컬 이미지 파일을 HTML/CSS에서 사용할 수 있도록
    Base64 Data URI 형태로 변환합니다.
    """
    if not image_path.exists():
        st.error(
            f"이미지 파일을 찾을 수 없습니다.\n\n"
            f"`{image_path}`"
        )
        st.stop()

    mime_type, _ = mimetypes.guess_type(image_path.name)

    if mime_type is None:
        mime_type = "image/png"

    encoded_image = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded_image}"


# =========================================================
# 공통 CSS
# =========================================================

def hide_streamlit_interface() -> None:
    """
    Figma 화면을 그대로 구현하기 위해 Streamlit의
    기본 헤더, 메뉴, 여백, 푸터를 숨깁니다.
    """
    st.html(
        """
        <style>
            html,
            body {
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
            }

            [data-testid="stAppViewContainer"] {
                background: #101923;
            }

            [data-testid="stAppViewBlockContainer"] {
                padding: 0 !important;
                margin: 0 !important;
                max-width: none !important;
                width: 100% !important;
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
                margin: 0;
                padding: 0;
            }
        </style>
        """
    )


# =========================================================
# 초기 화면
# =========================================================

def render_home_page() -> None:
    background_uri = image_to_data_uri(
        BACKGROUND_PATH
    )

    symbol_uri = image_to_data_uri(
        SYMBOL_PATH
    )

    wordmark_uri = image_to_data_uri(
        WORDMARK_PATH
    )

    home_html = f"""
    <style>
        :root {{
            --accent-color: #e66a28;
            --header-background: rgba(226, 227, 234, 0.94);
            --main-text-color: #ffffff;
            --sub-text-color: rgba(255, 255, 255, 0.76);
        }}

        * {{
            box-sizing: border-box;
        }}

        .home-screen {{
            position: fixed;
            inset: 0;
            z-index: 9999;

            width: 100vw;
            height: 100vh;

            overflow: hidden;

            background:
                linear-gradient(
                    rgba(24, 42, 62, 0.49),
                    rgba(24, 42, 62, 0.49)
                ),
                url("{background_uri}");

            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;

            font-family:
                Arial,
                "Noto Sans KR",
                "Apple SD Gothic Neo",
                sans-serif;
        }}

        /* ===============================
           상단 헤더
        =============================== */

        .home-header {{
            position: absolute;

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
                0 6px 20px rgba(0, 0, 0, 0.08);

            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);
        }}

        .home-brand {{
            display: flex;
            align-items: center;
            gap: 25px;

            color: #050505;
            text-decoration: none;

            cursor: pointer;
        }}

        .home-brand:hover {{
            opacity: 0.82;
        }}

        .home-brand:active {{
            transform: scale(0.99);
        }}

        .home-brand-symbol {{
            width: 72px;
            height: 72px;

            flex-shrink: 0;
            object-fit: contain;
        }}

        .home-brand-title {{
            margin: 0;

            font-size: clamp(
                27px,
                1.85vw,
                36px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -1.1px;

            white-space: nowrap;
        }}

        .student-badge {{
            height: 78px;
            min-width: 312px;

            padding: 0 24px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: var(--accent-color);
            color: #ffffff;

            border-radius: 16px;

            font-size: clamp(
                22px,
                1.5vw,
                30px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -0.7px;

            white-space: nowrap;
        }}

        /* ===============================
           중앙 콘텐츠
        =============================== */

        .overwatch-wordmark {{
            position: absolute;

            top: 24.7vh;
            left: 50%;

            width: min(63vw, 1210px);
            max-height: 155px;

            object-fit: contain;

            transform: translateX(-50%);

            user-select: none;
            pointer-events: none;
        }}

        .home-title {{
            position: absolute;

            top: 48.5vh;
            left: 50%;

            margin: 0;

            transform: translateX(-50%);

            color: var(--main-text-color);

            font-size: clamp(
                50px,
                4vw,
                78px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -2.5px;

            white-space: nowrap;

            text-align: center;

            text-shadow:
                0 3px 12px rgba(0, 0, 0, 0.2);
        }}

        .home-description {{
            position: absolute;

            top: 59.7vh;
            left: 50%;

            width: 90%;

            margin: 0;

            transform: translateX(-50%);

            color: var(--sub-text-color);

            font-size: clamp(
                23px,
                1.9vw,
                37px
            );

            line-height: 1.25;
            font-weight: 700;
            letter-spacing: -1.5px;

            text-align: center;

            white-space: nowrap;

            text-shadow:
                0 2px 10px rgba(0, 0, 0, 0.18);
        }}

        /* ===============================
           시작 버튼
        =============================== */

        .start-button {{
            position: absolute;

            top: 79.5vh;
            left: 50%;

            width: 280px;
            height: 116px;

            display: flex;
            align-items: center;
            justify-content: center;

            transform: translateX(-50%);

            background: var(--accent-color);
            color: #ffffff;

            border: 0;
            border-radius: 0;

            text-decoration: none;

            font-size: 31px;
            line-height: 1;
            font-weight: 800;
            letter-spacing: -0.8px;

            cursor: pointer;

            box-shadow:
                0 10px 24px rgba(0, 0, 0, 0.12);

            transition:
                background-color 0.15s ease,
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }}

        .start-button:hover {{
            background: #f27631;

            transform:
                translateX(-50%)
                translateY(-3px);

            box-shadow:
                0 14px 30px rgba(0, 0, 0, 0.2);
        }}

        .start-button:active {{
            transform:
                translateX(-50%)
                translateY(0)
                scale(0.98);
        }}

        /* ===============================
           작은 화면 대응
        =============================== */

        @media (max-width: 1000px) {{
            .home-header {{
                left: 18px;
                right: 18px;

                min-height: 82px;

                padding:
                    0 15px
                    0 20px;

                border-radius: 18px;
            }}

            .home-brand {{
                gap: 14px;
            }}

            .home-brand-symbol {{
                width: 54px;
                height: 54px;
            }}

            .home-brand-title {{
                font-size: 24px;
            }}

            .student-badge {{
                min-width: auto;
                height: 58px;

                padding: 0 16px;

                font-size: 18px;

                border-radius: 13px;
            }}

            .overwatch-wordmark {{
                top: 25vh;
                width: 78vw;
            }}

            .home-title {{
                top: 47vh;

                font-size: 48px;
            }}

            .home-description {{
                top: 57vh;

                width: 88%;

                font-size: 24px;

                white-space: normal;
            }}

            .start-button {{
                top: 76vh;

                width: 230px;
                height: 86px;

                font-size: 26px;
            }}
        }}

        @media (max-width: 650px) {{
            .home-brand-title {{
                font-size: 18px;
            }}

            .student-badge {{
                max-width: 155px;

                font-size: 15px;

                text-align: center;
            }}

            .overwatch-wordmark {{
                width: 88vw;
            }}

            .home-title {{
                font-size: 39px;
            }}

            .home-description {{
                font-size: 20px;
            }}
        }}
    </style>

    <main class="home-screen">
        <header class="home-header">
            <a
                class="home-brand"
                href="?page=home"
                target="_self"
                aria-label="홈으로 이동"
            >
                <img
                    class="home-brand-symbol"
                    src="{symbol_uri}"
                    alt="오버워치 로고"
                />

                <p class="home-brand-title">
                    Open Source Software
                </p>
            </a>

            <div class="student-badge">
                {STUDENT_INFO}
            </div>
        </header>

        <img
            class="overwatch-wordmark"
            src="{wordmark_uri}"
            alt="Overwatch"
        />

        <h1 class="home-title">
            Find Your Hero
        </h1>

        <p class="home-description">
            당신의 플레이 스타일에 가장 잘 맞는 영웅을 찾아보세요
        </p>

        <a
            class="start-button"
            href="?page=welcome"
            target="_self"
        >
            지금 시작하기
        </a>
    </main>
    """

    st.html(home_html)


# =========================================================
# 환영 화면
# =========================================================

def render_welcome_page() -> None:
    """
    홈 화면의 '지금 시작하기' 버튼을 누른 뒤 표시되는
    오버워치 환영 화면입니다.
    """
    background_uri = image_to_data_uri(
        BACKGROUND_PATH
    )

    symbol_uri = image_to_data_uri(
        SYMBOL_PATH
    )

    character_uri = image_to_data_uri(
        CHARACTER_PATH
    )

    welcome_html = f"""
    <style>
        :root {{
            --accent-color: #ef6c22;
            --header-background: rgba(226, 227, 234, 0.96);
            --main-text-color: #ffffff;
            --sub-text-color: rgba(255, 255, 255, 0.92);
        }}

        * {{
            box-sizing: border-box;
        }}

        /* ======================================
           화면 진입 애니메이션
        ====================================== */

        @keyframes fade-up {{
            0% {{
                opacity: 0;
                transform: translateY(38px);
                filter: blur(3px);
            }}

            100% {{
                opacity: 1;
                transform: translateY(0);
                filter: blur(0);
            }}
        }}

        @keyframes fade-in {{
            0% {{
                opacity: 0;
            }}

            100% {{
                opacity: 1;
            }}
        }}

        @keyframes character-enter {{
            0% {{
                opacity: 0;
                transform:
                    translateX(50px)
                    translateY(15px)
                    scale(0.97);
            }}

            100% {{
                opacity: 1;
                transform:
                    translateX(0)
                    translateY(0)
                    scale(1);
            }}
        }}

        @keyframes header-enter {{
            0% {{
                opacity: 0;
                transform: translateY(-22px);
            }}

            100% {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .welcome-screen {{
            position: fixed;
            inset: 0;
            z-index: 9999;

            width: 100vw;
            height: 100vh;

            overflow: hidden;

            background:
                linear-gradient(
                    90deg,
                    rgba(8, 17, 29, 0.94) 0%,
                    rgba(8, 17, 29, 0.91) 37%,
                    rgba(8, 17, 29, 0.82) 66%,
                    rgba(8, 17, 29, 0.72) 100%
                ),
                url("{background_uri}");

            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;

            font-family:
                Arial,
                "Noto Sans KR",
                "Apple SD Gothic Neo",
                sans-serif;

            animation:
                fade-in 0.45s ease-out both;
        }}

        /* ======================================
           상단 헤더
        ====================================== */

        .welcome-header {{
            position: absolute;

            /*
            캐릭터보다 높은 depth를 주어
            character.png가 상단바 뒤로 들어가도록 합니다.
            */
            z-index: 20;

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
                0 6px 20px rgba(0, 0, 0, 0.11);

            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);

            opacity: 0;

            animation:
                header-enter
                0.65s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.05s
                forwards;
        }}

        .welcome-brand {{
            display: flex;
            align-items: center;
            gap: 25px;

            color: #050505;
            text-decoration: none;

            cursor: pointer;

            transition:
                opacity 0.15s ease,
                transform 0.15s ease;
        }}

        .welcome-brand:hover {{
            opacity: 0.82;
        }}

        .welcome-brand:active {{
            transform: scale(0.99);
        }}

        .welcome-brand-symbol {{
            width: 72px;
            height: 72px;

            flex-shrink: 0;
            object-fit: contain;
        }}

        .welcome-brand-title {{
            margin: 0;

            color: #050505;

            font-size: clamp(
                27px,
                1.85vw,
                36px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -1.1px;

            white-space: nowrap;
        }}

        .student-badge {{
            height: 78px;
            min-width: 312px;

            padding: 0 24px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: var(--accent-color);
            color: #ffffff;

            border-radius: 16px;

            font-size: clamp(
                22px,
                1.5vw,
                30px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -0.7px;

            white-space: nowrap;
        }}

        /* ======================================
           왼쪽 텍스트 영역
        ====================================== */

        .welcome-content {{
            position: absolute;

            /*
            기존 27.2vh에서 위로 이동
            */
            top: 23.5vh;
            left: 6.1vw;

            z-index: 6;

            width: 51vw;
            max-width: 940px;
        }}

        .welcome-title {{
            margin: 0;

            color: var(--main-text-color);

            font-size: clamp(
                47px,
                3.75vw,
                72px
            );

            line-height: 1.24;
            font-weight: 800;
            letter-spacing: -3px;

            text-shadow:
                0 4px 14px rgba(0, 0, 0, 0.3);

            opacity: 0;

            animation:
                fade-up
                0.85s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.18s
                forwards;
        }}

        .welcome-description {{
            margin: 43px 0 0 0;

            color: var(--sub-text-color);

            font-size: clamp(
                25px,
                2vw,
                38px
            );

            line-height: 1.48;
            font-weight: 600;
            letter-spacing: -1.7px;

            text-shadow:
                0 3px 10px rgba(0, 0, 0, 0.28);

            opacity: 0;

            animation:
                fade-up
                0.85s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.38s
                forwards;
        }}

        /* ======================================
           시작 버튼
        ====================================== */

        .welcome-start-button {{
            position: absolute;

            left: 6.1vw;
            bottom: 12.9vh;

            z-index: 8;

            width: 280px;
            height: 118px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: var(--accent-color);
            color: #ffffff;

            border: 0;
            border-radius: 0;

            text-decoration: none;

            font-size: 34px;
            line-height: 1;
            font-weight: 800;
            letter-spacing: -1px;

            cursor: pointer;

            box-shadow:
                0 12px 28px rgba(0, 0, 0, 0.2);

            opacity: 0;

            animation:
                fade-up
                0.8s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.58s
                forwards;

            transition:
                background-color 0.16s ease,
                box-shadow 0.16s ease;
        }}

        .welcome-start-button:hover {{
            background: #ff7a2c;

            box-shadow:
                0 16px 34px rgba(0, 0, 0, 0.3);
        }}

        .welcome-start-button:active {{
            filter: brightness(0.92);
        }}

        /* ======================================
           캐릭터 이미지
        ====================================== */

        .character-image {{
            position: absolute;

            /*
            상단 헤더의 z-index 20보다 낮게 설정되어
            이미지가 상단바 뒤에 배치됩니다.
            */
            z-index: 2;

            right: -0.5vw;
            bottom: -1.3vh;

            width: min(
                45.5vw,
                875px
            );

            max-height: 89vh;

            object-fit: contain;
            object-position: right bottom;

            user-select: none;
            pointer-events: none;

            opacity: 0;

            filter:
                drop-shadow(
                    -12px 8px 20px
                    rgba(0, 0, 0, 0.22)
                );

            animation:
                character-enter
                1.05s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.12s
                forwards;
        }}

        .character-shadow {{
            position: absolute;

            z-index: 1;

            right: 0;
            bottom: 0;

            width: 51vw;
            height: 100vh;

            background:
                radial-gradient(
                    circle at 75% 55%,
                    rgba(21, 45, 74, 0.14) 0%,
                    rgba(9, 17, 27, 0.09) 43%,
                    rgba(9, 17, 27, 0) 73%
                );

            pointer-events: none;
        }}

        /* ======================================
           반응형
        ====================================== */

        @media (max-width: 1200px) {{
            .welcome-content {{
                top: 25vh;
                left: 5vw;

                width: 56vw;
            }}

            .welcome-title {{
                font-size: 50px;
            }}

            .welcome-description {{
                margin-top: 30px;

                font-size: 26px;
            }}

            .character-image {{
                right: -8vw;

                width: 54vw;
            }}

            .welcome-start-button {{
                left: 5vw;

                width: 240px;
                height: 92px;

                font-size: 28px;
            }}
        }}

        @media (max-width: 900px) {{
            .welcome-header {{
                left: 18px;
                right: 18px;

                min-height: 82px;

                padding:
                    0 15px
                    0 20px;

                border-radius: 18px;
            }}

            .welcome-brand {{
                gap: 14px;
            }}

            .welcome-brand-symbol {{
                width: 54px;
                height: 54px;
            }}

            .welcome-brand-title {{
                font-size: 23px;
            }}

            .student-badge {{
                min-width: auto;
                height: 58px;

                padding: 0 16px;

                border-radius: 13px;

                font-size: 17px;
            }}

            .welcome-content {{
                top: 22vh;
                left: 6vw;

                width: 67vw;
            }}

            .welcome-title {{
                font-size: 42px;
            }}

            .welcome-description {{
                font-size: 23px;
            }}

            .character-image {{
                right: -17vw;

                width: 68vw;
            }}

            .welcome-start-button {{
                left: 6vw;
                bottom: 11vh;
            }}
        }}

        @media (max-width: 650px) {{
            .welcome-brand-title {{
                font-size: 17px;
            }}

            .student-badge {{
                max-width: 152px;

                font-size: 14px;

                text-align: center;
            }}

            .welcome-content {{
                top: 21vh;

                width: 86vw;
            }}

            .welcome-title {{
                font-size: 35px;
            }}

            .welcome-description {{
                margin-top: 25px;

                font-size: 20px;
            }}

            .character-image {{
                right: -29vw;

                width: 88vw;

                opacity: 0;
            }}

            .welcome-start-button {{
                bottom: 9vh;

                width: 205px;
                height: 78px;

                font-size: 24px;
            }}
        }}

        /*
        운영체제에서 동작 줄이기를 설정한 사용자는
        애니메이션 없이 바로 화면을 표시합니다.
        */
        @media (prefers-reduced-motion: reduce) {{
            .welcome-screen,
            .welcome-header,
            .welcome-title,
            .welcome-description,
            .welcome-start-button,
            .character-image {{
                opacity: 1 !important;
                animation: none !important;
                transform: none !important;
                filter: none;
            }}
        }}
    </style>

    <main class="welcome-screen">
        <header class="welcome-header">
            <a
                class="welcome-brand"
                href="?page=home"
                target="_self"
                aria-label="홈으로 이동"
            >
                <img
                    class="welcome-brand-symbol"
                    src="{symbol_uri}"
                    alt="오버워치 로고"
                />

                <p class="welcome-brand-title">
                    Open Source Software
                </p>
            </a>

            <div class="student-badge">
                {STUDENT_INFO}
            </div>
        </header>

        <section class="welcome-content">
            <h1 class="welcome-title">
                안녕, 친구!<br />
                오버워치 세계에 온 걸 환영해.
            </h1>

            <p class="welcome-description">
                전장으로 나가기 전 영웅 선택은 필수야<br />
                너에게 딱 맞는 영웅을 찾아보자
            </p>
        </section>

        <div class="character-shadow"></div>

        <img
            class="character-image"
            src="{character_uri}"
            alt="오버워치 캐릭터"
        />

        <a
            class="welcome-start-button"
            href="?page=question_1"
            target="_self"
        >
            시작하기
        </a>
    </main>
    """

    st.html(welcome_html)

# =========================================================
# 질문 1 화면
# =========================================================

def render_question_1_page() -> None:
    """
    Q1. 선호 역할 선택 화면입니다.

    카드 선택 결과는 st.session_state에 저장하고,
    질문 화면의 이동 방향은 URL의 direction 값으로 결정합니다.
    """
    initialize_quiz_state()

    valid_roles = {
        "tank",
        "damage",
        "support",
        "flex",
    }

    selected_role_from_url = get_query_value("role")

    if selected_role_from_url in valid_roles:
        st.session_state["quiz_answers"]["role"] = (
            selected_role_from_url
        )

    selected_role = (
        st.session_state["quiz_answers"].get("role")
    )

    direction = get_query_value(
        "direction",
        "initial",
    )

    transition_class = {
        "initial": "initial-entry",
        "forward": "slide-forward",
        "backward": "slide-backward",
        "stay": "stay",
    }.get(
        direction,
        "initial-entry",
    )

    background_uri = image_to_data_uri(
        BACKGROUND_PATH
    )

    symbol_uri = image_to_data_uri(
        SYMBOL_PATH
    )

    character_uri = image_to_data_uri(
        CHARACTER_PATH
    )

    tank_icon_uri = image_to_data_uri(
        ROLE_TANK_ICON_PATH
    )

    damage_icon_uri = image_to_data_uri(
        ROLE_DAMAGE_ICON_PATH
    )

    support_icon_uri = image_to_data_uri(
        ROLE_SUPPORT_ICON_PATH
    )

    flex_icon_uri = image_to_data_uri(
        ROLE_FLEX_ICON_PATH
    )

    left_gray_uri = image_to_data_uri(
        ARROW_LEFT_GRAY_PATH
    )

    right_gray_uri = image_to_data_uri(
        ARROW_RIGHT_GRAY_PATH
    )

    right_white_uri = image_to_data_uri(
        ARROW_RIGHT_WHITE_PATH
    )

    right_orange_uri = image_to_data_uri(
        ARROW_RIGHT_ORANGE_PATH
    )

    role_cards = [
        {
            "value": "tank",
            "title": "TANK",
            "description": "전방에서 팀을 이끌어요",
            "icon": tank_icon_uri,
        },
        {
            "value": "damage",
            "title": "DAMAGE",
            "description": "적을 직접 처치해요",
            "icon": damage_icon_uri,
        },
        {
            "value": "support",
            "title": "SUPPORT",
            "description": "팀원을 치유하고 강화해요",
            "icon": support_icon_uri,
        },
        {
            "value": "flex",
            "title": "NOT SURE",
            "description": "잘 모르겠어요",
            "icon": flex_icon_uri,
        },
    ]

    role_cards_html: list[str] = []

    for card in role_cards:
        is_selected = (
            selected_role == card["value"]
        )

        selected_class = (
            "selected"
            if is_selected
            else ""
        )

        aria_pressed = (
            "true"
            if is_selected
            else "false"
        )

        role_cards_html.append(
            f"""
            <a
                class="role-card {selected_class}"
                href="?page=question_1&direction=stay&role={card['value']}"
                target="_self"
                aria-pressed="{aria_pressed}"
            >
                <div class="role-icon-circle">
                    <img
                        class="role-icon"
                        src="{card['icon']}"
                        alt=""
                    />
                </div>

                <h2 class="role-card-title">
                    {card['title']}
                </h2>

                <p class="role-card-description">
                    {card['description']}
                </p>
            </a>
            """
        )

    cards_html = "".join(role_cards_html)

    progress_dots_html = build_progress_dots(
        current_question=1
    )

    if selected_role is not None:
        next_arrow_html = f"""
        <a
            class="nav-arrow active-arrow"
            href="?page=question_2&direction=forward"
            target="_self"
            aria-label="다음 질문으로 이동"
        >
            <img
                class="arrow-image arrow-default"
                src="{right_white_uri}"
                alt=""
            />

            <img
                class="arrow-image arrow-hover"
                src="{right_orange_uri}"
                alt=""
            />
        </a>
        """

    else:
        next_arrow_html = f"""
        <div
            class="nav-arrow disabled-arrow"
            aria-label="답변을 선택해야 다음 질문으로 이동할 수 있습니다"
        >
            <img
                class="arrow-image"
                src="{right_gray_uri}"
                alt=""
            />
        </div>
        """

    question_html = f"""
    <style>
        :root {{
            --accent-orange: #ef6c22;
            --accent-yellow: #ffb62e;
            --selected-blue: #50b7ff;
            --header-background: rgba(226, 227, 234, 0.96);
            --white: #ffffff;
            --muted-white: rgba(255, 255, 255, 0.72);
        }}

        * {{
            box-sizing: border-box;
        }}

        /* ======================================
           질문 영역 전환 애니메이션
        ====================================== */

        @keyframes question-float-up {{
            0% {{
                opacity: 0;
                transform: translateY(38px);
                filter: blur(3px);
            }}

            100% {{
                opacity: 1;
                transform: translateY(0);
                filter: blur(0);
            }}
        }}

        @keyframes slide-in-from-right {{
            0% {{
                opacity: 0;
                transform: translateX(110px);
                filter: blur(3px);
            }}

            100% {{
                opacity: 1;
                transform: translateX(0);
                filter: blur(0);
            }}
        }}

        @keyframes slide-in-from-left {{
            0% {{
                opacity: 0;
                transform: translateX(-110px);
                filter: blur(3px);
            }}

            100% {{
                opacity: 1;
                transform: translateX(0);
                filter: blur(0);
            }}
        }}

        .question-screen {{
            position: fixed;
            inset: 0;
            z-index: 9999;

            width: 100vw;
            height: 100vh;

            overflow: hidden;

            background:
                linear-gradient(
                    90deg,
                    rgba(8, 17, 29, 0.93) 0%,
                    rgba(8, 17, 29, 0.89) 42%,
                    rgba(8, 17, 29, 0.79) 70%,
                    rgba(8, 17, 29, 0.70) 100%
                ),
                url("{background_uri}");

            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;

            font-family:
                Arial,
                "Noto Sans KR",
                "Apple SD Gothic Neo",
                sans-serif;
        }}

        /* ======================================
           고정 상단바
        ====================================== */

        .question-header {{
            position: absolute;

            z-index: 20;

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
                0 6px 20px rgba(0, 0, 0, 0.11);

            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);
        }}

        .question-brand {{
            display: flex;
            align-items: center;
            gap: 25px;

            color: #050505;
            text-decoration: none;

            cursor: pointer;

            transition:
                opacity 0.15s ease,
                transform 0.15s ease;
        }}

        .question-brand:hover {{
            opacity: 0.82;
        }}

        .question-brand:active {{
            transform: scale(0.99);
        }}

        .question-brand-symbol {{
            width: 72px;
            height: 72px;

            flex-shrink: 0;

            object-fit: contain;
        }}

        .question-brand-title {{
            margin: 0;

            color: #050505;

            font-size: clamp(
                27px,
                1.85vw,
                36px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -1.1px;

            white-space: nowrap;
        }}

        .student-badge {{
            height: 78px;
            min-width: 312px;

            padding: 0 24px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: var(--accent-orange);
            color: #ffffff;

            border-radius: 16px;

            font-size: clamp(
                22px,
                1.5vw,
                30px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -0.7px;

            white-space: nowrap;
        }}

        /* ======================================
           고정 캐릭터
        ====================================== */

        .question-character {{
            position: absolute;

            z-index: 2;

            right: -0.5vw;
            bottom: -1.3vh;

            width: min(
                45.5vw,
                875px
            );

            max-height: 89vh;

            object-fit: contain;
            object-position: right bottom;

            user-select: none;
            pointer-events: none;

            filter:
                drop-shadow(
                    -12px 8px 20px
                    rgba(0, 0, 0, 0.22)
                );
        }}

        /* ======================================
           움직이는 질문 영역
        ====================================== */

        .question-stage {{
            position: absolute;

            z-index: 7;

            top: 21.5vh;
            left: 6.1vw;

            width: 58vw;
            max-width: 1115px;
        }}

        .question-stage.slide-forward {{
            animation:
                slide-in-from-right
                0.58s
                cubic-bezier(0.22, 1, 0.36, 1)
                both;
        }}

        .question-stage.slide-backward {{
            animation:
                slide-in-from-left
                0.58s
                cubic-bezier(0.22, 1, 0.36, 1)
                both;
        }}

        .question-stage.stay {{
            animation: none;
        }}

        .initial-entry .question-copy {{
            opacity: 0;

            animation:
                question-float-up
                0.78s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.05s
                forwards;
        }}

        .initial-entry .role-grid {{
            opacity: 0;

            animation:
                question-float-up
                0.82s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.20s
                forwards;
        }}

        .initial-entry .question-navigation {{
            opacity: 0;

            animation:
                question-float-up
                0.82s
                cubic-bezier(0.22, 1, 0.36, 1)
                0.36s
                forwards;
        }}

        /* ======================================
           질문 제목
        ====================================== */

        .question-title {{
            display: flex;
            align-items: baseline;
            gap: 16px;

            margin: 0;

            color: var(--white);

            font-size: clamp(
                46px,
                3.65vw,
                70px
            );

            line-height: 1;
            font-weight: 800;
            letter-spacing: -2.4px;
        }}

        .question-number {{
            color: var(--accent-yellow);
        }}

        .question-description {{
            margin: 38px 0 0 0;

            color: var(--white);

            font-size: clamp(
                25px,
                1.9vw,
                36px
            );

            line-height: 1.35;
            font-weight: 600;
            letter-spacing: -1.4px;
        }}

        /* ======================================
           선택 카드
        ====================================== */

        .role-grid {{
            margin-top: 72px;

            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 16px;
        }}

        .role-card {{
            position: relative;

            height: 348px;

            padding: 70px 18px 32px;

            display: flex;
            flex-direction: column;
            align-items: center;

            color: var(--white);
            text-decoration: none;

            background:
                rgba(10, 18, 32, 0.72);

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
                transform 0.22s
                    cubic-bezier(0.22, 1, 0.36, 1),
                border-color 0.22s ease,
                background-color 0.22s ease,
                box-shadow 0.22s ease;
        }}

        .role-card::before {{
            content: "";

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
                opacity 0.22s ease;
        }}

        .role-card:hover {{
            transform: translateY(-12px);

            border-color:
                rgba(255, 255, 255, 0.40);

            box-shadow:
                0 22px 44px
                rgba(0, 0, 0, 0.28);
        }}

        .role-card.selected {{
            transform: translateY(-3px);

            border-color:
                var(--selected-blue);

            background:
                rgba(65, 119, 183, 0.44);

            box-shadow:
                inset 0 0 0 1px
                    rgba(80, 183, 255, 0.34),
                0 18px 38px
                    rgba(24, 117, 190, 0.18);
        }}

        .role-card.selected::before {{
            opacity: 1;
        }}

        .role-card.selected:hover {{
            transform: translateY(-12px);
        }}

        .role-icon-circle,
        .role-card-title,
        .role-card-description {{
            position: relative;
            z-index: 2;
        }}

        .role-icon-circle {{
            width: 96px;
            height: 96px;

            display: flex;
            align-items: center;
            justify-content: center;

            background:
                rgba(255, 255, 255, 0.07);

            border-radius: 50%;

            transition:
                background-color 0.22s ease,
                transform 0.22s ease;
        }}

        .role-card:hover .role-icon-circle {{
            transform: scale(1.06);
        }}

        .role-card.selected .role-icon-circle {{
            background:
                rgba(80, 183, 255, 0.96);
        }}

        .role-icon {{
            width: 53px;
            height: 53px;

            object-fit: contain;

            user-select: none;
            pointer-events: none;
        }}

        .role-card-title {{
            margin: 33px 0 0 0;

            color: #ffffff;

            font-size: clamp(
                22px,
                1.65vw,
                32px
            );

            line-height: 1;
            font-weight: 900;
            letter-spacing: 1.4px;

            text-align: center;
        }}

        .role-card.selected .role-card-title {{
            color: var(--selected-blue);
        }}

        .role-card-description {{
            margin: 19px 0 0 0;

            color: var(--muted-white);

            font-size: clamp(
                14px,
                0.95vw,
                18px
            );

            line-height: 1.4;
            font-weight: 500;
            letter-spacing: -0.4px;

            text-align: center;
        }}

        /* ======================================
           하단 내비게이션
        ====================================== */

        .question-navigation {{
            margin-top: 110px;

            display: grid;
            grid-template-columns:
                80px
                minmax(300px, 1fr)
                80px;
            align-items: center;
            gap: 26px;
        }}

        .nav-arrow {{
            position: relative;

            width: 72px;
            height: 72px;

            display: flex;
            align-items: center;
            justify-content: center;

            text-decoration: none;
        }}

        .active-arrow {{
            cursor: pointer;

            transition:
                transform 0.18s ease;
        }}

        .active-arrow:hover {{
            transform: translateY(-5px);
        }}

        .disabled-arrow {{
            cursor: default;
            opacity: 0.82;
        }}

        .arrow-image {{
            position: absolute;

            width: 72px;
            height: 72px;

            object-fit: contain;

            user-select: none;
            pointer-events: none;
        }}

        .arrow-default {{
            opacity: 1;

            transition:
                opacity 0.15s ease;
        }}

        .arrow-hover {{
            opacity: 0;

            transition:
                opacity 0.15s ease;
        }}

        .active-arrow:hover .arrow-default {{
            opacity: 0;
        }}

        .active-arrow:hover .arrow-hover {{
            opacity: 1;
        }}

        .progress-dots {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 27px;
        }}

        .progress-dot {{
            width: 22px;
            height: 22px;

            flex-shrink: 0;

            border-radius: 50%;
        }}

        .progress-dot.pending {{
            background:
                rgba(255, 255, 255, 0.58);
        }}

        .progress-dot.completed {{
            background: #ffffff;
        }}

        .progress-dot.current {{
            background: var(--accent-orange);
        }}

        /* ======================================
           반응형
        ====================================== */

        @media (max-width: 1300px) {{
            .question-stage {{
                top: 20vh;
                left: 5vw;

                width: 65vw;
            }}

            .role-grid {{
                margin-top: 50px;
            }}

            .role-card {{
                height: 310px;
                padding-top: 54px;
            }}

            .question-navigation {{
                margin-top: 70px;
            }}

            .question-character {{
                right: -10vw;
                width: 54vw;
            }}
        }}

        @media (max-width: 950px) {{
            .question-header {{
                left: 18px;
                right: 18px;

                min-height: 82px;

                padding:
                    0 15px
                    0 20px;

                border-radius: 18px;
            }}

            .question-brand {{
                gap: 14px;
            }}

            .question-brand-symbol {{
                width: 54px;
                height: 54px;
            }}

            .question-brand-title {{
                font-size: 22px;
            }}

            .student-badge {{
                min-width: auto;
                height: 58px;

                padding: 0 16px;

                font-size: 17px;

                border-radius: 13px;
            }}

            .question-stage {{
                top: 19vh;
                left: 5vw;

                width: 90vw;
            }}

            .question-character {{
                right: -26vw;
                width: 74vw;
                opacity: 0.45;
            }}

            .role-grid {{
                grid-template-columns:
                    repeat(2, minmax(0, 1fr));
            }}

            .role-card {{
                height: 255px;
                padding-top: 32px;
            }}

            .role-icon-circle {{
                width: 76px;
                height: 76px;
            }}

            .role-icon {{
                width: 42px;
                height: 42px;
            }}

            .role-card-title {{
                margin-top: 22px;
            }}

            .question-navigation {{
                margin-top: 48px;
            }}
        }}

        @media (max-width: 620px) {{
            .question-brand-title {{
                font-size: 16px;
            }}

            .student-badge {{
                max-width: 150px;

                font-size: 13px;
                text-align: center;
            }}

            .question-stage {{
                top: 17vh;
            }}

            .question-title {{
                font-size: 36px;
            }}

            .question-description {{
                margin-top: 22px;
                font-size: 20px;
            }}

            .role-grid {{
                margin-top: 30px;
                gap: 10px;
            }}

            .role-card {{
                height: 220px;
                padding:
                    24px 10px
                    20px;
            }}

            .role-icon-circle {{
                width: 64px;
                height: 64px;
            }}

            .role-icon {{
                width: 35px;
                height: 35px;
            }}

            .role-card-title {{
                font-size: 18px;
            }}

            .role-card-description {{
                margin-top: 12px;
                font-size: 12px;
            }}

            .question-navigation {{
                grid-template-columns:
                    56px
                    minmax(180px, 1fr)
                    56px;

                gap: 10px;
            }}

            .nav-arrow,
            .arrow-image {{
                width: 54px;
                height: 54px;
            }}

            .progress-dots {{
                gap: 11px;
            }}

            .progress-dot {{
                width: 14px;
                height: 14px;
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            .question-stage,
            .question-copy,
            .role-grid,
            .question-navigation,
            .role-card,
            .active-arrow {{
                opacity: 1 !important;
                animation: none !important;
                transform: none !important;
                filter: none !important;
                transition: none !important;
            }}
        }}
    </style>

    <main class="question-screen">
        <header class="question-header">
            <a
                class="question-brand"
                href="?page=home"
                target="_self"
                aria-label="홈으로 이동"
            >
                <img
                    class="question-brand-symbol"
                    src="{symbol_uri}"
                    alt="오버워치 로고"
                />

                <p class="question-brand-title">
                    Open Source Software
                </p>
            </a>

            <div class="student-badge">
                {STUDENT_INFO}
            </div>
        </header>

        <img
            class="question-character"
            src="{character_uri}"
            alt="오버워치 캐릭터"
        />

        <section
            class="question-stage {transition_class}"
        >
            <div class="question-copy">
                <h1 class="question-title">
                    <span class="question-number">
                        Q1.
                    </span>

                    <span>
                        선호 역할
                    </span>
                </h1>

                <p class="question-description">
                    어떤 역할로 팀에 기여하고 싶나요?
                </p>
            </div>

            <div class="role-grid">
                {cards_html}
            </div>

            <nav
                class="question-navigation"
                aria-label="질문 이동"
            >
                <div
                    class="nav-arrow disabled-arrow"
                    aria-label="첫 번째 질문입니다"
                >
                    <img
                        class="arrow-image"
                        src="{left_gray_uri}"
                        alt=""
                    />
                </div>

                <div class="progress-dots">
                    {progress_dots_html}
                </div>

                {next_arrow_html}
            </nav>
        </section>
    </main>
    """

    st.html(question_html)

# =========================================================
# 질문 2 화면
# =========================================================

def render_question_2_placeholder() -> None:
    """
    Q2 디자인을 구현하기 전 사용하는 임시 화면입니다.
    이전 화살표의 backward 전환값을 확인할 수 있습니다.
    """
    st.html(
        """
        <style>
            .question-two-placeholder {
                position: fixed;
                inset: 0;
                z-index: 9999;

                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 30px;

                width: 100vw;
                height: 100vh;

                background: #101b2a;
                color: white;

                font-family:
                    Arial,
                    "Noto Sans KR",
                    sans-serif;
            }

            .question-two-placeholder h1 {
                margin: 0;

                font-size: 52px;
            }

            .question-two-placeholder p {
                margin: 0;

                color: rgba(255, 255, 255, 0.72);

                font-size: 22px;
            }

            .question-two-placeholder a {
                padding: 20px 34px;

                background: #ef6c22;
                color: white;

                text-decoration: none;

                font-size: 21px;
                font-weight: 800;
            }
        </style>

        <main class="question-two-placeholder">
            <h1>Q2 화면 준비 중</h1>

            <p>
                이전 버튼으로 돌아가면 왼쪽에서 질문 화면이 들어옵니다.
            </p>

            <a
                href="?page=question_1&direction=backward"
                target="_self"
            >
                Q1으로 돌아가기
            </a>
        </main>
        """
    )

# =========================================================
# 화면 라우팅
# =========================================================

def main() -> None:
    hide_streamlit_interface()
    initialize_quiz_state()

    current_page = get_query_value(
        "page",
        "home",
    )

    if current_page == "welcome":
        render_welcome_page()
        return

    if current_page == "question_1":
        render_question_1_page()
        return

    if current_page == "question_2":
        render_question_2_placeholder()
        return

    render_home_page()

if __name__ == "__main__":
    main()
