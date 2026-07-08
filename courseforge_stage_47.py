# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: CourseForge
# Demo scenario for CourseForge: exercises the main workflow end-to-end.
import sys, os, json, random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from courseforge import (CourseForge, Module, Lesson, Exercise, Reviewer)

demo = CourseForge("DemoCourse")
demo.add_module(Module("Python 101"))
demo.add_lesson(Lesson("Intro to Variables", demo["Python 101"]))

exercises = [
    Exercise("Print Hello", "print('Hello')"),
    Exercise("Add numbers", "a, b = 2, 3\nprint(a + b)"),
]
for ex in exercises:
    demo.add_exercise(ex, lesson=demo["Intro to Variables"])

random.seed(0)
reviews = [Reviewer("Alice", score=4), Reviewer("Bob", score=5)]
for r in reviews:
    demo.add_review(r, exercise=random.choice(exercises))

progress = {"total_lessons": 1, "completed_exercises": random.randint(1, len(exercises))}
demo.set_progress(progress)

print(f"CourseForge Demo – {len(demo.modules)} module(s), {len(demo.lessons)} lesson(s)")
for m in demo.modules:
    print(f"  Module: {m.name}")
for l in demo.lessons:
    print(f"  Lesson: {l.title} → exercises={sum(1 for e in demo.exercises if e.lesson == l)}")
