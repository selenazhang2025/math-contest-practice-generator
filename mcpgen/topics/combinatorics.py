from __future__ import annotations
import random
import math


def nCk(n: int, k: int) -> int:
    return math.comb(n, k)


def make_problem(rng: random.Random, difficulty: int) -> tuple[str, str, str]:
    if difficulty <= 2:
        # basic counting
        n = rng.randint(5, 10)
        k = rng.randint(2, min(5, n))
        ans = nCk(n, k)
        prompt = f"How many ways are there to choose {k} students from {n} students?"
        answer = str(ans)
        solution = (
            f"This is a combination: $\\binom{{{n}}}{{{k}}} = {ans}$."
        )
        return prompt, answer, solution

    if difficulty == 3:
        # inclusion-exclusion: count integers in range divisible by a or b
        N = rng.randint(80, 150)
        a = rng.choice([3, 4, 5, 6])
        b = rng.choice([5, 6, 7, 8])
        l = abs(a*b) // math.gcd(a, b)
        ans = N // a + N // b - N // l
        prompt = f"How many integers from 1 to {N} are divisible by {a} or {b}?"
        answer = str(ans)
        solution = (
            f"Count multiples of {a}: $\\lfloor {N}/{a}\\rfloor = {N//a}$.\n\n"
            f"Count multiples of {b}: $\\lfloor {N}/{b}\\rfloor = {N//b}$.\n\n"
            f"Subtract multiples of lcm({a},{b})={l}: $\\lfloor {N}/{l}\\rfloor = {N//l}$.\n\n"
            f"Total = {N//a}+{N//b}-{N//l} = {ans}$."
        )
        return prompt, answer, solution

    # difficulty 4–5: stars and bars with constraint
    n = rng.randint(10, 25)
    k = rng.randint(3, 6)
    # number of nonnegative integer solutions to x1+...+xk = n
    ans = nCk(n + k - 1, k - 1)
    prompt = f"How many solutions in nonnegative integers are there to $x_1+\\cdots+x_{k}={n}$?"
    answer = str(ans)
    solution = (
        "Use stars and bars.\n\n"
        f"Number of nonnegative solutions to $x_1+\\cdots+x_{k}={n}$ is "
        f"$\\binom{{{n}+{k}-1}}{{{k}-1}} = \\binom{{{n+k-1}}}{{{k-1}}} = {ans}$."
    )
    return prompt, answer, solution
