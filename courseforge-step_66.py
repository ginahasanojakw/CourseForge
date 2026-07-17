# === Stage 66: Add export of a short status dashboard ===
# Project: CourseForge
import os
from pathlib import Path


def render_dashboard(courses, stats):
    """Render a compact status dashboard."""
    lines = [f"=== CourseForge Dashboard ===\n"]
    for course in courses:
        name = course["name"]
        progress = stats.get(name, 0)
        bar_len = int(20 * progress / max(stats.values())) if stats else 0
        bar = "#" * bar_len + "." * (20 - bar_len)
        lines.append(f"  {name}: [{bar}] {progress:.0%}")
    total = sum(c["total_lessons"] for c in courses)
    completed = sum(c.get("completed", {}).get("count", 0) for c in courses.values())
    lines.append(f"\nTotal lessons: {total} | Completed: {completed}")
    return "\n".join(lines)


def export_dashboard(output_dir="dashboard"):
    os.makedirs(output_dir, exist_ok=True)
    path = Path(output_dir) / "status.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_dashboard(courses(), stats()))
    return str(path.resolve())


if __name__ == "__main__":
    print(export_dashboard())
