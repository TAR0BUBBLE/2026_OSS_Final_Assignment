import json
from functools import lru_cache
from pathlib import Path
from typing import Any


DATA_PATH = Path(__file__).resolve().parent / "data" / "heroes.json"


PRIORITY_TO_METRIC = {
    "damage": "damage",
    "survival": "durability",
    "protection": "protection",
    "healing": "healing",
    "control": "control",
    "easy": "beginner_friendly",
}


PRIORITY_LABELS = {
    "damage": "높은 공격력",
    "survival": "생존력",
    "protection": "아군 보호",
    "healing": "치유 능력",
    "control": "전장 제어",
    "easy": "쉬운 조작",
}


POSITION_LABELS = {
    "frontline": "최전방",
    "midline": "중간 전선",
    "backline": "후방",
    "flank": "측면·적 후방",
    "flexible": "유연한 위치",
}


EXPERIENCE_TO_COMPLEXITY = {
    "beginner": 1,
    "intermediate": 3,
    "advanced": 5,
}


@lru_cache
def load_heroes() -> list[dict[str, Any]]:
    """
    heroes.json을 한 번만 읽고 메모리에 저장합니다.
    """
    with DATA_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    heroes = data.get("heroes")

    if not isinstance(heroes, list):
        raise ValueError("heroes.json에 heroes 배열이 없습니다.")

    return heroes


def similarity(hero_value: int, user_value: int) -> float:
    """
    1~5 점수 두 개의 유사도를 0~1로 계산합니다.
    """
    difference = abs(hero_value - user_value)
    return max(0.0, 1.0 - difference / 4.0)


def calculate_score(
    hero: dict[str, Any],
    answers: dict[str, Any],
) -> float:
    """
    영웅과 사용자 답변의 적합도를 100점 만점으로 계산합니다.

    역할: 25점
    교전 거리: 12점
    조준 성향: 12점
    기동성: 10점
    공격성: 10점
    선호 위치: 10점
    중요 능력: 16점
    경험 수준: 5점
    """
    scores = hero["scores"]

    total_score = 25.0

    total_score += 12.0 * similarity(
        scores["range"],
        answers["range"],
    )

    total_score += 12.0 * similarity(
        scores["aim"],
        answers["aim"],
    )

    total_score += 10.0 * similarity(
        scores["mobility"],
        answers["mobility"],
    )

    total_score += 10.0 * similarity(
        scores["aggression"],
        answers["aggression"],
    )

    selected_position = answers["position"]

    if (
        selected_position == "flexible"
        or selected_position in hero["positions"]
    ):
        total_score += 10.0

    priority_metric = PRIORITY_TO_METRIC[answers["priority"]]

    total_score += 16.0 * (
        scores[priority_metric] / 5.0
    )

    target_complexity = EXPERIENCE_TO_COMPLEXITY[
        answers["experience"]
    ]

    total_score += 5.0 * similarity(
        scores["complexity"],
        target_complexity,
    )

    return round(total_score, 1)


def build_reasons(
    hero: dict[str, Any],
    answers: dict[str, Any],
) -> list[str]:
    """
    추천 화면에 표시할 추천 이유를 생성합니다.
    """
    scores = hero["scores"]
    reasons: list[str] = []

    if abs(scores["range"] - answers["range"]) <= 1:
        if answers["range"] <= 2:
            reasons.append(
                "가까운 거리에서 적극적으로 교전하는 성향과 잘 맞습니다."
            )
        elif answers["range"] >= 4:
            reasons.append(
                "멀리서 안정적으로 공격하는 성향과 잘 맞습니다."
            )
        else:
            reasons.append(
                "중거리에서 유연하게 교전하는 성향과 잘 맞습니다."
            )

    if (
        scores["mobility"] >= 4
        and answers["mobility"] >= 4
    ):
        reasons.append(
            "빠른 이동과 재배치를 선호하는 플레이에 적합합니다."
        )

    if (
        scores["aggression"] >= 4
        and answers["aggression"] >= 4
    ):
        reasons.append(
            "적극적으로 진입하고 교전을 시작하는 성향과 잘 맞습니다."
        )

    if answers["aim"] <= 2 and scores["aim"] <= 2:
        reasons.append(
            "정밀 조준에 대한 부담이 비교적 적은 영웅입니다."
        )

    if answers["aim"] >= 4 and scores["aim"] >= 4:
        reasons.append(
            "높은 조준 자신감을 효과적으로 활용할 수 있습니다."
        )

    selected_position = answers["position"]

    if (
        selected_position != "flexible"
        and selected_position in hero["positions"]
    ):
        reasons.append(
            f"선호한 {POSITION_LABELS[selected_position]} 위치에서 "
            "강점을 발휘할 수 있습니다."
        )

    priority = answers["priority"]
    priority_metric = PRIORITY_TO_METRIC[priority]

    reasons.append(
        f"중요하게 선택한 ‘{PRIORITY_LABELS[priority]}’ 특성이 "
        f"{scores[priority_metric]}/5점으로 높게 평가되었습니다."
    )

    return reasons[:3]


def recommend_heroes(
    answers: dict[str, Any],
    top_n: int = 3,
) -> list[dict[str, Any]]:
    """
    사용자 답변을 기준으로 상위 영웅을 반환합니다.
    """
    heroes = load_heroes()

    selected_role = answers["role"]

    if selected_role == "flex":
        candidates = heroes
    else:
        candidates = [
            hero
            for hero in heroes
            if hero["role"] == selected_role
        ]

    recommendations = []

    for hero in candidates:
        match_percentage = calculate_score(
            hero,
            answers,
        )

        recommendations.append(
            {
                "hero_id": hero["id"],
                "name_ko": hero["name_ko"],
                "name_en": hero["name_en"],
                "role": hero["role"],
                "match_percentage": match_percentage,
                "summary": hero["summary_ko"],
                "reasons": build_reasons(
                    hero,
                    answers,
                ),
                "tags": hero["tags"],
                "source_url": hero["source_url"],
            }
        )

    recommendations.sort(
        key=lambda hero: hero["match_percentage"],
        reverse=True,
    )

    return recommendations[:top_n]