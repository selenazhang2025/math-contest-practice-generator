from __future__ import annotations

from pathlib import Path

from mcpgen.models import ProblemSet


def render_markdown(pset: ProblemSet, include_solutions: bool = True) -> str:
    lines: list[str] = []
    lines.append(f"# {pset.title}")
    if pset.seed is not None:
        lines.append(f"**Seed:** `{pset.seed}`")
    lines.append("")
    lines.append("## Problems")
    lines.append("")
    for p in pset.problems:
        lines.append(f"**{p.id}. ({p.topic.replace('_',' ').title()})** {p.prompt}")
        lines.append("")
    lines.append("## Answer Key")
    lines.append("")
    for p in pset.problems:
        lines.append(f"- **{p.id}**: {p.answer}")
    lines.append("")
    if include_solutions:
        lines.append("## Solutions")
        lines.append("")
        for p in pset.problems:
            lines.append(f"### {p.id}. ({p.topic.replace('_',' ').title()})")
            lines.append("")
            lines.append(p.solution.strip())
            lines.append("")
    return "\n".join(lines)


def render_pdf(pset: ProblemSet, pdf_path: Path) -> None:
    # Optional dependency: reportlab
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    width, height = letter

    margin = 50
    y = height - margin

    def draw_line(text: str, dy: int = 14) -> None:
        nonlocal y
        if y < margin:
            c.showPage()
            y = height - margin
        c.drawString(margin, y, text)
        y -= dy

    draw_line(pset.title, dy=22)
    if pset.seed is not None:
        draw_line(f"Seed: {pset.seed}", dy=18)
    draw_line("Problems", dy=18)

    for p in pset.problems:
        draw_line(f"{p.id}. ({p.topic}) {p.prompt}")
        draw_line("")

    c.showPage()
    y = height - margin
    draw_line("Answer Key", dy=18)
    for p in pset.problems:
        draw_line(f"{p.id}. {p.answer}")

    c.showPage()
    y = height - margin
    draw_line("Solutions", dy=18)
    for p in pset.problems:
        draw_line(f"{p.id}. ({p.topic})", dy=16)
        for line in p.solution.strip().splitlines():
            draw_line(line)
        draw_line("")

    c.save()
