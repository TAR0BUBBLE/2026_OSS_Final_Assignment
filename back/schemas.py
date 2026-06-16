from typing import Literal

from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    role: Literal[
        "tank",
        "damage",
        "support",
        "flex",
    ]

    range: int = Field(
        ge=1,
        le=5,
    )

    aim: int = Field(
        ge=1,
        le=5,
    )

    mobility: int = Field(
        ge=1,
        le=5,
    )

    aggression: int = Field(
        ge=1,
        le=5,
    )

    position: Literal[
        "frontline",
        "midline",
        "backline",
        "flank",
        "flexible",
    ]

    priority: Literal[
        "damage",
        "survival",
        "protection",
        "healing",
        "control",
        "easy",
    ]

    experience: Literal[
        "beginner",
        "intermediate",
        "advanced",
    ]


class HeroRecommendation(BaseModel):
    hero_id: str
    name_ko: str
    name_en: str
    role: str
    match_percentage: float
    summary: str
    reasons: list[str]
    tags: list[str]
    source_url: str


class RecommendResponse(BaseModel):
    message: str
    received_role: str
    recommendations: list[HeroRecommendation]