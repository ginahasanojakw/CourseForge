# === Stage 51: Add unit tests for search and filter behavior ===
# Project: CourseForge
import unittest
from courseforge.models import Course, Module, Lesson, Exercise, Review, LearnerProgress


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.course = Course("Intro to Python", "Introduction to Python programming")
        m1 = Module("Basics", [Lesson("Variables", ["Explain variables", "Create a variable"]), Lesson("Types", [])])
        m2 = Module("Advanced", [Lesson("Functions", []), Lesson("Classes", [])])
        self.course.add_module(m1)
        self.course.add_module(m2)

    def test_search_by_keyword_in_lesson_title(self):
        results = CourseForge.search(self.course, keyword="variables")
        self.assertTrue(any("Variables" in l.title for r, l in results))

    def test_filter_modules_by_status(self):
        m1.status = "completed"
        m2.status = "in_progress"
        filtered = CourseForge.filter_modules(self.course.modules, status="completed")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Basics")

    def test_search_empty_keyword_returns_all_lessons(self):
        results = CourseForge.search(self.course, keyword="")
        all_lessons = [l for m in self.course.modules for l in m.lessons]
        self.assertEqual(len(results), len(all_lessons))


if __name__ == "__main__":
    unittest.main()
