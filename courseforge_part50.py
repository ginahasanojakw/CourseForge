# === Stage 50: Add unit tests for import and export behavior ===
# Project: CourseForge
import unittest
from courseforge.models.Course import Course
from courseforge.models.Lesson import Lesson
from courseforge.models.Module import Module
from courseforge.models.Exercise import Exercise, ExerciseType


class TestCourseImportExport(unittest.TestCase):
    def test_export_import_roundtrip(self):
        course = Course(
            name="Intro to Python",
            description="Learn basics of Python programming.",
            modules=[
                Module(name="Getting Started", lessons=[
                    Lesson(name="Setup", exercises=[Exercise("Install Python", ExerciseType.INSTALL)]),
                    Lesson(name="First Program", exercises=[Exercise("Hello World", ExerciseType.CODING)]),
                ]),
                Module(name="Advanced Topics", lessons=[]),
            ],
        )

        data = course.export()
        self.assertIn("name", data)
        self.assertEqual(data["modules"][0]["name"], "Getting Started")

        reimported = Course.import_from_json(data)
        self.assertEqual(reimported.name, "Intro to Python")
        self.assertEqual(len(reimported.modules), 2)
        self.assertEqual(len(reimported.modules[0].lessons), 2)


if __name__ == "__main__":
    unittest.main()
