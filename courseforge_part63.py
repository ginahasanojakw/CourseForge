# === Stage 63: Add relationships between records where useful ===
# Project: CourseForge
# Relationship helpers for CourseForge models (add to coursebuilder/models.py)


def get_learner_progress_for(lesson: Lesson, learner: Learner) -> Optional[ProgressRecord]:
    """Return the progress record linking a lesson and a learner if it exists."""
    return ProgressRecord.objects.filter(lesson=lesson, learner=learner).first() or None


def add_review_to_exercise(exercise: Exercise, reviewer: Learner, comment: str) -> ReviewRecord:
    """Create a new review for an exercise by its reviewer with the given comment."""
    return ReviewRecord.objects.create(
        lesson=exercise.lesson,
        exercise=exercise,
        reviewer=reviewer,
        comment=comment,
    )


def update_learner_progress(progress_record: ProgressRecord, score: Optional[float] = None):
    """Update a progress record with an optional new score."""
    if score is not None:
        progress_record.score = score
    progress_record.completed = True
    progress_record.last_updated = timezone.now()
    progress_record.save(update_fields=["score", "completed", "last_updated"])


def get_learner_total_progress(learner: Learner) -> dict:
    """Aggregate a learner's overall stats across all lessons they have attempted."""
    progress_records = ProgressRecord.objects.filter(learner=learner)
    completed = progress_records.filter(completed=True).count()
    total = progress_records.count() or 1
    avg_score = progress_records.aggregate(avg=Avg("score"))["avg"]
    return {
        "total_lessons_attempted": total,
        "completed": completed,
        "completion_rate": round((completed / total) * 100, 2),
        "average_score": round(float(avg_score), 2) if avg_score else None,
    }


def get_exercise_difficulty_distribution() -> dict:
    """Count exercises by difficulty level."""
    return {level: Exercise.objects.filter(difficulty=level).count() for level in Difficulty}
