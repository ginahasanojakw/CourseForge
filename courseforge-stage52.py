# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: CourseForge
def format_progress_summary(learner_name: str, total_lessons: int, completed: int) -> str:
    """Return a human-readable progress summary for a learner."""
    rate = (completed / total_lessons * 100) if total_lessons else 0.0
    emoji = "🏆" if rate == 100.0 else ("🔥" if rate > 50.0 else "💪")
    return f"{emoji} {learner_name}: {completed}/{total_lessons} lessons ({rate:.0f}%)"


def compute_lesson_difficulty(grade: float, time_spent_seconds: int) -> str:
    """Estimate difficulty label from grade and time spent."""
    if grade >= 95 and time_spent_seconds <= 600:
        return "Easy"
    elif grade >= 80 or time_spent_seconds <= 1200:
        return "Medium"
    else:
        return "Hard"


def validate_review(review_text: str, min_length: int = 5) -> bool:
    """Check that a review is not empty and meets minimum length."""
    if not isinstance(review_text, str):
        raise TypeError("Review must be a string")
    return len(review_text.strip()) >= min_length


def get_learner_ranking(progress_list: list[dict]) -> dict[str, int]:
    """Return a ranking dictionary sorted by completion percentage (desc)."""
    ranked = sorted(
        progress_list,
        key=lambda p: (p["completed"] / max(p["total"], 1)) if p["total"] else 0.0,
        reverse=True,
    )
    return {entry["name"]: idx + 1 for idx, entry in enumerate(ranked)}


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Return numerator/denominator or a default when denominator is zero."""
    if denominator == 0:
        return default
    return numerator / denominator
