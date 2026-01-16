from __future__ import annotations
import random


def make_problem(rng: random.Random, difficulty: int) -> tuple[str, str, str]:
    if difficulty <= 2:
        # evaluate composition
        a = rng.randint(1, 5)
        b = rng.randint(-6, 6)
        x = rng.randint(-4, 6)
        # f(t)=at+b, g(t)=t^2
        fx = a * (x * x) + b
        prompt = f"Let $g(x)=x^2$ and $f(x)={a}x+({b})$. Compute $f(g({x}))$."
        answer = str(fx)
        solution = (
            f"First compute $g({x})={x}^2={x*x}$.\n\n"
            f"Then $f(g({x}))=f({x*x})={a}({x*x})+({b})={fx}$."
        )
        return prompt, answer, solution

    if difficulty == 3:
        # find parameter for inverse linear
        m = rng.randint(2, 9)
        b = rng.randint(-10, 10)
        prompt = f"Given $f(x)={m}x+({b})$, find $f^{{-1}}(x)$."
        answer = f"(x-({b}))/{m}"
        solution = (
            "Let $y=f(x)$.\n\n"
            f"$y={m}x+({b})$.\n\n"
            f"Swap $x$ and $y$: $x={m}y+({b})$.\n\n"
            f"Solve for $y$: $x-({b})={m}y \\Rightarrow y=\\frac{{x-({b})}}{{{m}}}$.\n\n"
            f"So $f^{{-1}}(x)=\\frac{{x-({b})}}{{{m}}}$."
        )
        return prompt, answer, solution

    # difficulty 4–5: piecewise continuity / parameter
    a = rng.randint(-6, 6)
    b = rng.randint(-6, 6)
    # choose c so it can be continuous at 0: left= ax+b at 0 is b, right= c*0^2 + a = a
    # So require a=b to be continuous; ask to find condition.
    prompt = (
        "For what values of the parameters is the function continuous at $x=0$?\n\n"
        r"$f(x)=\begin{cases}"
        f"{a}x+({b}), & x<0\\\\"
        f"x^2+({a}), & x\\ge 0"
        r"\end{cases}$"
    )
    answer = "a = b"
    solution = (
        "Continuity at 0 requires left-hand limit = value at 0.\n\n"
        f"Left-hand limit: $\\lim_{{x\\to 0^-}}({a}x+({b})) = {b}$.\n\n"
        f"Value at 0 from the right piece: $f(0)=0^2+({a}) = {a}$.\n\n"
        f"Set equal: {b} = {a} ⇒ $a=b$."
    )
    return prompt, answer, solution
