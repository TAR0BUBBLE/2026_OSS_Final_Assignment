import re
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from back.recommender import recommend_heroes
from back.schemas import RecommendRequest, RecommendResponse

PROJECT_ROOT = Path(__file__).resolve().parents[1]
HERO_IMAGE_DIR = PROJECT_ROOT / "front" / "assets" / "heroes"
HERO_ID_PATTERN = re.compile(r"^[a-z0-9_-]+$")

app = FastAPI(
    title="Overwatch Hero Recommendation API",
    description="사용자의 플레이 성향을 바탕으로 오버워치 영웅을 추천하는 API입니다.",
    version="1.2.0",
)

# Streamlit 화면(8501 또는 EC2의 공개 포트)에서 브라우저가
# FastAPI(8000)로 직접 요청할 수 있도록 허용합니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Overwatch Hero Recommendation API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/hero-images/{hero_id}.png", response_class=FileResponse)
def get_hero_image(hero_id: str) -> FileResponse:
    """프론트엔드 결과 카드에 사용할 로컬 영웅 이미지를 반환합니다."""
    if not HERO_ID_PATTERN.fullmatch(hero_id):
        raise HTTPException(status_code=400, detail="올바르지 않은 영웅 ID입니다.")

    image_path = HERO_IMAGE_DIR / f"{hero_id}.png"

    if not image_path.is_file():
        raise HTTPException(status_code=404, detail="영웅 이미지를 찾을 수 없습니다.")

    return FileResponse(
        path=image_path,
        media_type="image/png",
        headers={"Cache-Control": "public, max-age=3600"},
    )


@app.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest) -> RecommendResponse:
    answers = request.model_dump()

    try:
        recommendations = recommend_heroes(
            answers=answers,
            top_n=3,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return RecommendResponse(
        message="플레이 성향 분석이 완료되었습니다.",
        received_answers=answers,
        recommendations=recommendations,
    )
