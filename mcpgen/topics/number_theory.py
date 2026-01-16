from __future__ import annotations
import random
from math import gcd


def make_problem(rng: random.Random, difficulty: int) -> tuple[str, str, str]:
    if difficulty <= 2:
        # gcd/lcm
        a = rng.randint(12, 80)
        b = rng.randint(12, 80)
        g = gcd(a, b)
        l = a * b // g
        prompt = f"Compute $\\gcd({a},{b})$ and $\\operatorname{{lcm}}({a},{b})$."
        answer = f"gcd = {g}, lcm = {l}"
        solution = (
            f"Use $ab = \\gcd(a,b)\\cdot\\mathrm{{lcm}}(a,b)$.\n\n"
            f"$\\gcd({a},{b}) = {g}$.\n\n"
            f"$\\mathrm{{lcm}}({a},{b}) = \\frac{{{a}\\cdot{b}}}{{{g}}} = {l}$."
        )
        return prompt, answer, solution

    if difficulty == 3:
        # modular inverse small
        m = rng.choice([7, 9, 11, 13, 17, 19])
        a = rng.choice([i for i in range(2, m) if gcd(i, m) == 1])
        # find inverse
        inv = next(x for x in range(1, m) if (a * x) % m == 1)
        prompt = f"Find the multiplicative inverse of {a} modulo {m}."
        answer = f"{inv}"
        solution = (
            f"We need $x$ such that ${a}x \\equiv 1 \\pmod{{{m}}}$.\n\n"
            f"Testing residues (or using the Euclidean algorithm), we find "
            f"${a}\\cdot{inv} = {a*inv} \\equiv 1 \\pmod{{{m}}}$.\n\n"
            f"So the inverse is {inv}."
        )
        return prompt, answer, solution

    # difficulty 4–5: divisibility / Diophantine counting
    # Count solutions to ax + by = n in nonnegative integers (small)
    a = rng.choice([3, 4, 5, 6, 7])
    b = rng.choice([4, 5, 6, 7, 8])
    n = rng.randint(25, 70)
    prompt = f"How many pairs of nonnegative integers $(x,y)$ satisfy ${a}x + {b}y = {n}$?"
    count = 0
    sols = []
    for y in range(0, n // b + 1):
        rem = n - b * y
        if rem % a == 0:
            x = rem // a
            if x >= 0:
                count += 1
                sols.append((x, y))
    answer = str(count)
    solution = (
        f"Scan $y$ from $0$ to $\\lfloor {n}/{b} \\rfloor$.\n\n"
        f"For each $y$, compute $n - {b}y$ and check divisibility by {a}.\n\n"
        f"Valid solutions: {', '.join([f'({x},{y})' for x,y in sols]) if sols else 'none'}.\n\n"
        f"Therefore there are {count} solution(s)."
    )
    return prompt, answer, solution
