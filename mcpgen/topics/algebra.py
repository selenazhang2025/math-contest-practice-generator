from __future__ import annotations
import random
from math import gcd


def make_problem(rng: random.Random, difficulty: int) -> tuple[str, str, str]:
    # Linear / quadratic / rational equation depending on difficulty
    if difficulty <= 2:
        # Solve ax + b = c
        a = rng.randint(2, 9)
        x = rng.randint(-9, 9)
        b = rng.randint(-12, 12)
        c = a * x + b
        prompt = f"Solve for $x$: {a}x + ({b}) = {c}."
        answer = f"x = {x}"
        solution = (
            f"We have {a}x + ({b}) = {c}.\n\n"
            f"Subtract {b} from both sides: {a}x = {c - b}.\n\n"
            f"Divide by {a}: $x = \\frac{{{c - b}}}{{{a}}} = {x}$."
        )
        return prompt, answer, solution

    if difficulty == 3:
        # Factorable quadratic x^2 + px + q = 0
        r1 = rng.randint(-8, 8)
        r2 = rng.randint(-8, 8)
        while r1 == 0 and r2 == 0:
            r1, r2 = rng.randint(-8, 8), rng.randint(-8, 8)
        p = -(r1 + r2)
        q = r1 * r2
        prompt = f"Solve $x^2 + ({p})x + ({q}) = 0$."
        answer = f"x = {r1}, {r2}"
        solution = (
            "Factor the quadratic:\n\n"
            f"$x^2 + ({p})x + ({q}) = (x - ({r1}))(x - ({r2}))$.\n\n"
            "Set each factor to zero:\n\n"
            f"$x = {r1}$ or $x = {r2}$."
        )
        return prompt, answer, solution

    # difficulty 4–5: Solve a rational equation with simplification
    # (x-a)/(x-b) = k  (avoid b)
    a = rng.randint(-6, 6)
    b = rng.choice([i for i in range(-6, 7) if i != a])
    k_num = rng.randint(2, 7)
    k_den = rng.randint(2, 7)
    g = gcd(k_num, k_den)
    k_num //= g
    k_den //= g

    # Solve (x-a)/(x-b) = k_num/k_den
    # k_den(x-a) = k_num(x-b)
    # (k_den - k_num)x = k_den*a - k_num*b
    A = (k_den - k_num)
    B = (k_den * a - k_num * b)
    # Ensure A != 0
    if A == 0:
        k_num += 1
        A = (k_den - k_num)
        B = (k_den * a - k_num * b)

    # Make x integer by choosing B divisible by A if possible; else keep fraction
    if B % A == 0:
        x = B // A
        ans = f"x = {x} (with x ≠ {b})"
        x_str = str(x)
    else:
        # reduce fraction
        g2 = gcd(abs(B), abs(A))
        num, den = B // g2, A // g2
        ans = f"x = {num}/{den} (with x ≠ {b})"
        x_str = f"\\frac{{{num}}}{{{den}}}"

    prompt = f"Solve for $x$: $\\frac{{x-({a})}}{{x-({b})}} = \\frac{{{k_num}}}{{{k_den}}}$."
    solution = (
        "Cross-multiply (noting $x \\neq " + str(b) + "$):\n\n"
        f"${k_den}(x-({a})) = {k_num}(x-({b}))$.\n\n"
        f"Expand:\n\n"
        f"${k_den}x - {k_den}({a}) = {k_num}x - {k_num}({b})$.\n\n"
        f"Bring like terms together:\n\n"
        f"$({k_den}-{k_num})x = {k_den}({a}) - {k_num}({b})$.\n\n"
        f"So $x = {x_str}$, and ensure $x \\neq {b}$."
    )
    return prompt, ans, solution
