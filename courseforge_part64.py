# === Stage 64: Add validation for relationship references ===
# Project: CourseForge
from ..models import Module, Lesson, Exercise, Review, LearnerProgress, CourseForgeError


def validate_relationship_references(db: "Database", course_id: int) -> None:
    """Validate that all relationship references in a course are valid."""
    # Check module references in lessons
    lessons = db.get_lessons(course_id=course_id)
    for lesson in lessons:
        if lesson.module_id and not db.get_module(lesson.module_id):
            raise CourseForgeError(f"Lesson {lesson.id} references non-existent module {lesson.module_id}")

    # Check exercise references in lessons
    exercises = db.get_exercises(course_id=course_id)
    for exercise in exercises:
        if exercise.lesson_id and not db.get_lesson(exercise.lesson_id):
            raise CourseForgeError(f"Exercise {exercise.id} references non-existent lesson {exercise.lesson_id}")

    # Check review references
    reviews = db.get_reviews(course_id=course_id)
    for review in reviews:
        if review.exercise_id and not db.get_exercise(review.exercise_id):
            raise CourseForgeError(f"Review {review.id} references non-existent exercise {review.exercise_id}")

    # Check learner progress references
    progress_records = db.get_learner_progress(course_id=course_id)
    for record in progress_records:
        if record.lesson_id and not db.get_lesson(record.lesson_id):
            raise CourseForgeError(f"LearnerProgress {record.id} references non-existent lesson {record.lesson_id}")
