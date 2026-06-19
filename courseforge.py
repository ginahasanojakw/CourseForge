# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: CourseForge
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import uuid

@dataclass
class Exercise:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    solution: Optional[str] = None

@dataclass
class Lesson:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    content: str = ""
    exercises: List[Exercise] = field(default_factory=list)

@dataclass
class Module:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    lessons: Dict[str, Lesson] = field(default_factory=dict)

@dataclass
class Course:
    name: str = ""
    modules: List[Module] = field(default_factory=list)
    learners_progress: Dict[str, Dict[str, int]] = field(default_factory=dict)  # learner_id -> {module_id -> completed_lessons}

def init_demo_course() -> Course:
    course = Course(name="Python Basics")
    
    module1 = Module(title="Introduction", lessons={})
    lesson1 = Lesson(title="Hello World", content="print('Hello, World!')")
    exercise1 = Exercise(title="Run Code", description="Execute the provided code snippet.")
    lesson1.exercises.append(exercise1)
    module1.lessons["intro"] = lesson1
    course.modules.append(module1)
    
    module2 = Module(title="Data Structures", lessons={})
    lesson2 = Lesson(title="Lists", content="my_list = [1, 2, 3]")
    exercise2 = Exercise(title="Create List", description="Initialize a list with three items.")
    lesson2.exercises.append(exercise2)
    module2.lessons["lists"] = lesson2
    course.modules.append(module2)
    
    return course

demo_course = init_demo_course()
