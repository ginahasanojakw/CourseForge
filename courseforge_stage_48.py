# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: CourseForge
from courseforge.models import Module, Lesson, Exercise
from courseforge.helpers import create_module_with_lessons, validate_course_structure


def test_create_module_with_single_lesson():
    module = create_module_with_lessons("Intro", topics=["Basics"])
    assert isinstance(module, dict)
    assert "name" in module and module["name"] == "Intro"
    assert len(module.get("lessons", [])) >= 1


def test_create_module_with_mixed_content():
    lesson = Lesson(title="Getting Started", exercises=[Exercise(title="Quiz 1")])
    module = create_module_with_lessons("Chapter 1", topics=["Overview"], lessons=[lesson])
    assert "Getting Started" in [l["title"] for l in module.get("lessons", [])]


def test_validate_empty_structure():
    structure = {"modules": []}
    result = validate_course_structure(structure)
    assert result is False


def test_validate_single_module_structure():
    structure = {
        "modules": [
            {
                "name": "Python 101",
                "topics": ["Syntax"],
                "lessons": [{"title": "Hello World"}],
            }
        ]
    }
    result = validate_course_structure(structure)
    assert result is True


def test_validate_missing_modules():
    structure = {"modules": None}
    result = validate_course_structure(structure)
    assert result is False
