from __future__ import annotations
import random
import math


def make_problem(rng: random.Random, difficulty: int) -> tuple[str, str, str]:
    if difficulty <= 2:
        # triangle area with base/height
        b = rng.randint(6, 20)
        h = rng.randint(4, 18)
        area = b * h / 2
        prompt = f"A triangle has base {b} and height {h}. Find its area."
        answer = str(area).rstrip("0").rstrip(".")
        solution = f"Area = $\\frac12 bh = \\frac12\\cdot {b}\\cdot {h} = {area}$."
        return prompt, answer, solution

    if difficulty == 3:
        # circle arc length
        r = rng.randint(3, 12)
        deg = rng.choice([30, 45, 60, 90, 120, 150])
        arc = (deg / 360) * 2 * math.pi * r
        prompt = f"A circle has radius {r}. Find the arc length subtended by a central angle of {deg}° (in terms of $\\pi$)."
        # express as fraction*pi
        frac_num = deg * r
        frac_den = 180
        g = math.gcd(frac_num, frac_den)
        frac_num //= g
        frac_den //= g
        answer = f"{frac_num}π/{frac_den}" if frac_den != 1 else f"{frac_num}π"
        solution = (
            f"Arc length = $\\frac{{{deg}}}{{360}}\\cdot 2\\pi r$.\n\n"
            f"= $\\frac{{{deg}}}{{360}}\\cdot 2\\pi\\cdot {r}"
            f"= \\frac{{{deg}\\cdot{r}}}{{180}}\\pi"
            f"= \\frac{{{frac_num}}}{{{frac_den}}}\\pi$."
        )
        return prompt, answer, solution

    # difficulty 4–5: coordinate geometry distance to line
    # distance from point to line ax+by+c=0
    a = rng.randint(1, 6)
    b = rng.randint(1, 6)
    c = rng.randint(-12, 12)
    x0 = rng.randint(-5, 5)
    y0 = rng.randint(-5, 5)

    num = abs(a * x0 + b * y0 + c)
    den = math.sqrt(a * a + b * b)

    prompt = f"Find the distance from the point $({x0},{y0})$ to the line ${a}x+{b}y+({c})=0$."
    answer = f"{num}/√{a*a + b*b}"
    solution = (
        "Use the point-to-line distance formula:\n\n"
        r"$d=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$" "\n\n"
        f"Here $a={a}, b={b}, c={c}, (x_0,y_0)=({x0},{y0})$.\n\n"
        f"Numerator: $|{a}({x0})+{b}({y0})+({c})| = |{a*x0 + b*y0 + c}| = {num}$.\n\n"
        f"Denominator: $\\sqrt{{{a}^2+{b}^2}} = \\sqrt{{{a*a + b*b}}}$.\n\n"
        f"So $d = \\frac{{{num}}}{{\\sqrt{{{a*a + b*b}}}}}$."
    )
    return prompt, answer, solution
