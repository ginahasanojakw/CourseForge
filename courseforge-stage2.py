# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: CourseForge
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Module:
    id: int
    title: str
    description: str = ""
    lessons: List['Lesson'] = field(default_factory=list)

@dataclass
class Lesson:
    id: int
    module_id: int
    title: str
    content: str = ""
    exercises: List['Exercise'] = field(default_factory=list)

@dataclass
class Exercise:
    id: int
    lesson_id: int
    question: str
    options: Optional[List[str]] = None
    correct_answer_idx: Optional[int] = None
    user_attempts: List[dict] = field(default_factory=list)  # {'user': str, 'answer': str, 'is_correct': bool}

@dataclass
class Review:
    id: int
    lesson_id: int
    learner_name: str
    rating: float
    comment: str = ""
    date: date = field(default_factory=date)

@dataclass
class LearnerProgress:
    module_id: int
    completed_lessons: List[int] = field(default_factory=list)
    last_accessed: Optional[date] = None
