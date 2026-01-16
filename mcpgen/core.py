from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Callable

from mcpgen.models import Problem, ProblemSet
from mcpgen.topics import algebra, number_theory, combinatorics, geometry, functions

TopicFn = Callable[[random.Random, int], tuple[str, str, str]]  # (prompt, answer, solution)


TOPIC_BANK: dict[str, TopicFn] = {
    "algebra": algebra.make_problem,
    "number_theory": number_theory.make_problem,
    "combinatorics": combinatorics.make_problem,
    "geometry": geometry.make_problem,
    "functions": functions.make_problem,
}


@dataclass(frozen=True)
class GeneratorConfig:
    n: int
    difficulty: int  # 1..5
    topics: list[str] | None  # None = all
    seed: int | None = None
    title: str = "Math Contest Practice Set"


def _pick_topics(cfg: GeneratorConfig) -> list[str]:
    if cfg.topics is None:
        return list(TOPIC_BANK.keys())
    chosen = []
    for t in cfg.topics:
        if t not in TOPIC_BANK:
            raise ValueError(f"Unknown topic '{t}'. Valid: {', '.join(TOPIC_BANK.keys())}")
        chosen.append(t)
    return chosen


def generate_set(cfg: GeneratorConfig) -> ProblemSet:
    if cfg.n <= 0:
        raise ValueError("n must be positive")
    if not (1 <= cfg.difficulty <= 5):
        raise ValueError("difficulty must be between 1 and 5")

    rng = random.Random(cfg.seed)
    topics = _pick_topics(cfg)

    problems: list[Problem] = []
    for i in range(1, cfg.n + 1):
        topic = rng.choice(topics)
        prompt, answer, solution = TOPIC_BANK[topic](rng, cfg.difficulty)
        problems.append(
            Problem(
                id=i,
                topic=topic,
                difficulty=cfg.difficulty,
                prompt=prompt,
                answer=answer,
                solution=solution,
            )
        )

    return ProblemSet(title=cfg.title, seed=cfg.seed, problems=problems)
