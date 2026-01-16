from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Difficulty = Literal[1, 2, 3, 4, 5]


@dataclass(frozen=True)
class Problem:
    id: int
    topic: str
    difficulty: int
    prompt: str
    answer: str
    solution: str


@dataclass(frozen=True)
class ProblemSet:
    title: str
    seed: int | None
    problems: list[Problem]
