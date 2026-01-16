# Math Contest Practice Generator (Python)

Generate reproducible, contest-style math practice sets with **full solutions** across core competition topics.

This project produces high-quality, intermediate-level problems suitable for Euclid / AMC 10–12 style practice, with a clean CLI and modular design.

This project was built to generate realistic math contest practice for my own competition prep, and to explore clean, reproducible problem generation in Python.

---

## Features

* **Contest-style problems** (algebra, number theory, combinatorics, geometry, functions)
* **Reproducible output** via random seed
* **Difficulty control** (1–5)
* **Modular topic system** (easy to extend)
* **Markdown output** with problems, answer key, and solutions
* **Basic tests** to verify determinism and topic filtering

---

## Project Structure

```
math-contest-practice-generator/
├── generate.py              # CLI entry point
├── mcpgen/
│   ├── core.py              # Generation logic
│   ├── models.py            # Data models
│   ├── render.py            # Markdown rendering
│   └── topics/              # Topic-specific generators
│       ├── algebra.py
│       ├── number_theory.py
│       ├── combinatorics.py
│       ├── geometry.py
│       └── functions.py
├── tests/
│   └── test_generation.py   # Reproducibility & topic tests
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Quick Start

### Requirements

* Python 3.9+

### Generate a practice set

```bash
python3 generate.py --n 10 --difficulty 3 --topics all --seed 42
```

This creates:

```
practice.md
```

containing:

* Problems
* Answer key
* Step-by-step solutions

---

## CLI Options

| Flag             | Description                     |
| ---------------- | ------------------------------- |
| `--n`            | Number of problems              |
| `--difficulty`   | Difficulty level (1–5)          |
| `--topics`       | `all` or comma-separated list   |
| `--seed`         | Random seed for reproducibility |
| `--out`          | Output markdown file            |
| `--no-solutions` | Omit solutions section          |

### Example: topic-focused drill

```bash
python3 generate.py --n 8 --difficulty 3 --topics algebra,geometry --seed 7 --out geometry_drill.md
```

---

## Tests

Run tests with:

```bash
python3 -m pytest
```

Tests verify:

* Identical output with the same seed
* Correct topic filtering

---

## Design Choices (Why I Built It This Way)

* **Deterministic generation** ensures fairness and repeatability
* **Topic generators** are isolated for clarity and extensibility
* **Pure Python** with no heavy dependencies
* **Interview-friendly architecture** with clear separation of concerns

---
## Limitations & Future Work
- Difficulty scaling is uniform across topics; future versions could tune difficulty per topic.
- Problems are text-based only; diagrams could improve geometry questions.

---

## Possible Extensions

* Hint-only mode
* Difficulty scaling per topic
* PDF export
* Web interface
* Topic weighting

---

## License

MIT License

---

## Author

Built as a personal project to explore problem generation, clean Python architecture, and reproducible tooling for competitive mathematics practice.
