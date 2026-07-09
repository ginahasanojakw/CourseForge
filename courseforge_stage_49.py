# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: CourseForge
import unittest
from src.models.exercise import Exercise, ExerciseStatus, Difficulty
from src.services.course_service import CourseService
from src.models.course import Course
from datetime import datetime


class TestExerciseUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.service = CourseService()
        course = Course(title="Test", description="", created_at=datetime.now())
        course.lessons = [Lesson(content="L1", duration=60, created_at=datetime.now())]
        lesson = course.lessons[0]
        exercise = Exercise(
            question="Q1?",
            options=["A", "B", "C"],
            correct_index=0,
            explanation="",
            difficulty=Difficulty.EASY,
            status=ExerciseStatus.DRAFT,
            created_at=datetime.now(),
        )
        lesson.exercises = [exercise]

    def test_update_exercise_status(self):
        exercise = self.service.update_exercise(
            course_id="c1",
            module_id="",
            lesson_id="l1",
            question_id="e1",
            status=ExerciseStatus.PUBLISHED,
            updated_at=datetime.now(),
        )
        self.assertEqual(exercise.status, ExerciseStatus.PUBLISHED)

    def test_update_exercise_content(self):
        exercise = self.service.update_exercise(
            course_id="c1",
            module_id="",
            lesson_id="l1",
            question_id="e1",
            content="Updated Q?",
            updated_at=datetime.now(),
        )
        self.assertEqual(exercise.question, "Updated Q?")

    def test_update_exercise_difficulty(self):
        exercise = self.service.update_exercise(
            course_id="c1",
            module_id="",
            lesson_id="l1",
            question_id="e1",
            difficulty=Difficulty.HARD,
            updated_at=datetime.now(),
        )
        self.assertEqual(exercise.difficulty, Difficulty.HARD)

    def test_delete_exercise(self):
        result = self.service.delete_exercise(
            course_id="c1",
            module_id="",
            lesson_id="l1",
            question_id="e1",
            deleted_by="instructor",
        )
        self.assertTrue(result)

    def test_delete_published_exercise(self):
        exercise = self.service.update_exercise(
            course_id="c1",
            module_id="",
            lesson_id="l1",
            question_id="e1",
            status=ExerciseStatus.PUBLISHED,
            updated_at=datetime.now(),
        )
        result = self.service.delete_exercise(
            course_id="c1",
            module_id="",
            lesson_id="l1",
            question_id="e1",
            deleted_by="instructor",
        )
        self.assertFalse(result)

    def test_update_nonexistent_question(self):
        with self.assertRaises(ValueError):
            self.service.update_exercise(
                course_id="c1",
                module_id="",
                lesson_id="l1",
                question_id="nonexistent",
                status=ExerciseStatus.DRAFT,
                updated_at=datetime.now(),
            )

    def test_delete_nonexistent_question(self):
        with self.assertRaises(ValueError):
            self.service.delete_exercise(
                course_id="c1",
                module_id="",
                lesson_id="l1",
                question_id="nonexistent",
                deleted_by="instructor",
            )


if __name__ == "__main__":
    unittest.main()
