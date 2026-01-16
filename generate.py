from __future__ import annotations

import argparse
from pathlib import Path

from mcpgen.core import GeneratorConfig, generate_set
from mcpgen.render import render_markdown


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Math Contest Practice Generator")
    p.add_argument("--n", type=int, default=10, help="Number of problems")
    p.add_argument("--difficulty", type=int, default=3, choices=range(1, 6),
                   help="Difficulty 1 (easy) to 5 (hard)")
    p.add_argument("--topics", type=str, default="all",
                   help="Comma-separated topics or 'all' "
                        "(algebra,number_theory,combinatorics,geometry,functions)")
    p.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    p.add_argument("--out", type=str, default="practice.md", help="Markdown output path")
    p.add_argument("--no-solutions", action="store_true",
                   help="If set, omit solutions section in markdown")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    topics = args.topics.strip()
    topic_list = None if topics.lower() == "all" else [t.strip() for t in topics.split(",") if t.strip()]

    cfg = GeneratorConfig(
        n=args.n,
        difficulty=args.difficulty,
        topics=topic_list,
        seed=args.seed,
    )

    problem_set = generate_set(cfg)
    md = render_markdown(problem_set, include_solutions=(not args.no_solutions))

    out_path = Path(args.out)
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote markdown: {out_path.resolve()}")


if __name__ == "__main__":
    main()
