from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).resolve().parent / "data" / "heroes.json"

ROLE_VALUES = {"tank", "damage", "support", "flex"}
POSITION_VALUES = {"frontline", "midline", "backline", "flank", "flexible"}
PRIORITY_TO_METRIC = {
    "damage": "damage",
    "survival": "durability",
    "protection": "protection",
    "healing": "healing",
    "control": "control",
    "easy": "beginner_friendly",
}
EXPERIENCE_TARGETS = {
    "beginner": {
        "complexity": 1,
        "beginner_friendly": 5,
    },
    "intermediate": {
        "complexity": 3,
        "beginner_friendly": 3,
    },
    "advanced": {
        "complexity": 5,
        "beginner_friendly": 1,
    },
}

METRIC_LABELS = {
    "damage": "높은 공격력",
    "durability": "튼튼한 생존력",
    "protection": "아군 보호와 구조",
    "healing": "강력한 치유",
    "control": "적 방해와 전장 제어",
    "beginner_friendly": "쉬운 조작과 입문 난이도",
}
POSITION_LABELS = {
    "frontline": "최전방",
    "midline": "중간 전선",
    "backline": "후방",
    "flank": "측면·적 후방",
    "flexible": "유연한 위치",
}
RANGE_LABELS = {
    1: "근거리",
    2: "근중거리",
    3: "중거리",
    4: "중장거리",
    5: "장거리",
}
ROLE_LABELS = {
    "tank": "돌격",
    "damage": "공격",
    "support": "지원",
    "flex": "전체 역할",
}

# 총점 100점
WEIGHTS = {
    "role": 25.0,
    "range": 12.0,
    "aim": 12.0,
    "mobility": 10.0,
    "aggression": 10.0,
    "position": 10.0,
    "priority": 16.0,
    "experience_complexity": 3.0,
    "experience_beginner_friendly": 2.0,
}


@lru_cache(maxsize=1)
def load_heroes(path: Path = DATA_PATH) -> list[dict[str, Any]]:
    """heroes.json에서 영웅 목록을 한 번만 읽어 캐시합니다."""
    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    heroes = payload.get("heroes")
    if not isinstance(heroes, list):
        raise ValueError("heroes.json의 heroes 항목이 올바른 목록이 아닙니다.")

    return heroes


def similarity(hero_value: int | float, user_value: int | float) -> float:
    """1~5 값 두 개의 유사도를 0~1 범위로 계산합니다."""
    return max(0.0, 1.0 - abs(float(hero_value) - float(user_value)) / 4.0)


def validate_answers(answers: dict[str, Any]) -> None:
    """추천 계산에 필요한 8개 응답과 값 범위를 검증합니다."""
    required = {
        "role",
        "range",
        "aim",
        "mobility",
        "aggression",
        "position",
        "priority",
        "experience",
    }
    missing = required - answers.keys()
    if missing:
        raise ValueError(f"누락된 응답 항목: {sorted(missing)}")

    if answers["role"] not in ROLE_VALUES:
        raise ValueError("role 값이 올바르지 않습니다.")
    if answers["position"] not in POSITION_VALUES:
        raise ValueError("position 값이 올바르지 않습니다.")
    if answers["priority"] not in PRIORITY_TO_METRIC:
        raise ValueError("priority 값이 올바르지 않습니다.")
    if answers["experience"] not in EXPERIENCE_TARGETS:
        raise ValueError("experience 값이 올바르지 않습니다.")

    for key in ("range", "aim", "mobility", "aggression"):
        value = answers[key]
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError(f"{key} 값은 1~5 정수여야 합니다.")


def calculate_score_breakdown(
    hero: dict[str, Any],
    answers: dict[str, Any],
) -> dict[str, float]:
    """항목별 점수를 계산합니다. 모든 항목의 합은 최대 100점입니다."""
    scores = hero["scores"]
    priority_metric = PRIORITY_TO_METRIC[answers["priority"]]
    experience_targets = EXPERIENCE_TARGETS[answers["experience"]]

    role_score = (
        WEIGHTS["role"]
        if answers["role"] == "flex" or hero["role"] == answers["role"]
        else 0.0
    )

    if answers["position"] == "flexible":
        position_score = WEIGHTS["position"]
    elif answers["position"] in hero["positions"]:
        position_score = WEIGHTS["position"]
    else:
        position_score = 0.0

    breakdown = {
        "role": role_score,
        "range": WEIGHTS["range"] * similarity(scores["range"], answers["range"]),
        "aim": WEIGHTS["aim"] * similarity(scores["aim"], answers["aim"]),
        "mobility": WEIGHTS["mobility"]
        * similarity(scores["mobility"], answers["mobility"]),
        "aggression": WEIGHTS["aggression"]
        * similarity(scores["aggression"], answers["aggression"]),
        "position": position_score,
        "priority": WEIGHTS["priority"] * (scores[priority_metric] / 5.0),
        # Q8 경험 수준은 complexity와 beginner_friendly를 모두 반영합니다.
        "experience_complexity": WEIGHTS["experience_complexity"]
        * similarity(scores["complexity"], experience_targets["complexity"]),
        "experience_beginner_friendly": WEIGHTS["experience_beginner_friendly"]
        * similarity(
            scores["beginner_friendly"],
            experience_targets["beginner_friendly"],
        ),
    }

    return {key: round(value, 2) for key, value in breakdown.items()}


def calculate_score(hero: dict[str, Any], answers: dict[str, Any]) -> float:
    """항목별 점수를 합산하여 0~100점의 최종 적합도를 반환합니다."""
    return round(sum(calculate_score_breakdown(hero, answers).values()), 2)


def build_reasons(hero: dict[str, Any], answers: dict[str, Any]) -> list[str]:
    """결과 화면에 표시할 추천 이유를 최대 4개 생성합니다."""
    scores = hero["scores"]
    reasons: list[str] = []

    if abs(scores["range"] - answers["range"]) <= 1:
        reasons.append(
            f"선호한 교전 거리와 잘 맞는 {RANGE_LABELS[scores['range']]} 중심 영웅입니다."
        )

    if abs(scores["mobility"] - answers["mobility"]) <= 1:
        if answers["mobility"] >= 4:
            reasons.append("빠른 이동과 재배치를 선호하는 성향에 잘 맞습니다.")
        elif answers["mobility"] <= 2:
            reasons.append("한 위치를 안정적으로 유지하는 플레이와 잘 맞습니다.")

    if abs(scores["aggression"] - answers["aggression"]) <= 1:
        if answers["aggression"] >= 4:
            reasons.append("적극적으로 교전을 시작하는 플레이 성향과 잘 맞습니다.")
        elif answers["aggression"] <= 2:
            reasons.append("신중하게 기회를 보는 플레이 성향과 잘 맞습니다.")

    if abs(scores["aim"] - answers["aim"]) <= 1:
        if answers["aim"] <= 2:
            reasons.append("정밀 조준 부담이 비교적 적은 편입니다.")
        elif answers["aim"] >= 4:
            reasons.append("높은 조준 자신감을 살릴 수 있는 영웅입니다.")

    metric = PRIORITY_TO_METRIC[answers["priority"]]
    reasons.append(
        f"가장 중요하게 선택한 ‘{METRIC_LABELS[metric]}’ 특성이 "
        f"{scores[metric]}/5점입니다."
    )

    if answers["position"] != "flexible" and answers["position"] in hero["positions"]:
        reasons.append(
            f"선호한 {POSITION_LABELS[answers['position']]} 운영에 적합합니다."
        )

    if answers["experience"] == "beginner" and scores["beginner_friendly"] >= 4:
        reasons.append("입문자가 비교적 쉽게 익힐 수 있는 영웅입니다.")
    elif answers["experience"] == "advanced" and scores["complexity"] >= 4:
        reasons.append("숙련도가 높을수록 잠재력을 크게 발휘할 수 있습니다.")

    # 중복을 제거하면서 생성 순서를 유지합니다.
    unique_reasons = list(dict.fromkeys(reasons))
    return unique_reasons[:4]


def recommend_heroes(
    answers: dict[str, Any],
    top_n: int = 3,
    heroes: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """사용자 응답에 가장 잘 맞는 영웅을 점수순으로 반환합니다."""
    validate_answers(answers)

    if top_n < 1:
        raise ValueError("top_n은 1 이상의 정수여야 합니다.")

    candidates = list(heroes) if heroes is not None else list(load_heroes())

    # 역할을 고른 경우 해당 역할만 비교하고, flex는 전체 영웅을 비교합니다.
    if answers["role"] != "flex":
        candidates = [
            hero for hero in candidates if hero["role"] == answers["role"]
        ]

    if not candidates:
        raise ValueError("조건에 맞는 추천 후보 영웅이 없습니다.")

    priority_metric = PRIORITY_TO_METRIC[answers["priority"]]
    ranked: list[dict[str, Any]] = []

    for hero in candidates:
        breakdown = calculate_score_breakdown(hero, answers)
        match_score = round(sum(breakdown.values()), 2)

        ranked.append(
            {
                "hero_id": hero["id"],
                "name_ko": hero["name_ko"],
                "name_en": hero["name_en"],
                "role": hero["role"],
                "match_percentage": match_score,
                "summary": hero["summary_ko"],
                "reasons": build_reasons(hero, answers),
                "tags": hero["tags"],
                "source_url": hero["source_url"],
                "score_breakdown": breakdown,
                "hero_scores": hero["scores"],
                "priority_metric": priority_metric,
            }
        )

    ranked.sort(
        key=lambda item: (
            item["match_percentage"],
            item["hero_scores"][priority_metric],
            item["hero_scores"]["beginner_friendly"],
            item["name_en"],
        ),
        reverse=True,
    )

    return ranked[: min(top_n, len(ranked))]


if __name__ == "__main__":
    sample_answers = {
        "role": "damage",
        "range": 1,
        "aim": 2,
        "mobility": 5,
        "aggression": 5,
        "position": "flank",
        "priority": "easy",
        "experience": "beginner",
    }

    print(
        json.dumps(
            recommend_heroes(sample_answers, top_n=3),
            ensure_ascii=False,
            indent=2,
        )
    )
