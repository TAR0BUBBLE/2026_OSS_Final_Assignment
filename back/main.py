from fastapi import FastAPI

from back.recommender import recommend_heroes
from back.schemas import (
    RecommendRequest,
    RecommendResponse,
)


app = FastAPI(
    title="Overwatch Hero Recommendation API",
    description=(
        "사용자의 플레이 성향을 바탕으로 "
        "오버워치 영웅을 추천하는 API입니다."
    ),
    version="1.0.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Overwatch Hero Recommendation API"
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok"
    }


@app.post(
    "/recommend",
    response_model=RecommendResponse,
)
def recommend(
    request: RecommendRequest,
) -> RecommendResponse:
    answers = request.model_dump()

    recommendations = recommend_heroes(
        answers=answers,
        top_n=3,
    )

    return RecommendResponse(
        message="플레이 성향 분석이 완료되었습니다.",
        received_role=request.role,
        recommendations=recommendations,
    )
