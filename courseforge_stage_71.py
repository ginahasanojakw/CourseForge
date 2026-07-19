# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: CourseForge
def seed_demo_data(store):
    """Populate store with deterministic sample data for CourseForge."""
    store['modules'] = [
        {'id': 'm1', 'title': 'Module 1: Introduction'},
        {'id': 'm2', 'title': 'Module 2: Deep Dive'},
        {'id': 'm3', 'title': 'Module 3: Advanced Topics'},
    ]
    store['lessons'] = [
        {'id': 'l1', 'module_id': 'm1', 'title': 'Lesson 1.1: Welcome'},
        {'id': 'l2', 'module_id': 'm1', 'title': 'Lesson 1.2: Setup'},
        {'id': 'l3', 'module_id': 'm2', 'title': 'Lesson 2.1: Core Concepts'},
    ]
    store['exercises'] = [
        {'id': 'e1', 'lesson_id': 'l1', 'type': 'quiz', 'question': 'What is CourseForge?', 'correct_answer': 'A collaborative course builder', 'options': ['A quiz app', 'A collaborative course builder', 'An e-book reader', 'A video editor']},
        {'id': 'e2', 'lesson_id': 'l3', 'type': 'code', 'prompt': 'Write a hello world function'},
    ]
    store['reviews'] = [
        {'id': 'r1', 'module_id': 'm1', 'rating': 4, 'comment': 'Great intro module!'},
        {'id': 'r2', 'module_id': 'm3', 'rating': 5, 'comment': 'Very advanced and challenging.'},
    ]
    store['learners'] = [
        {'name': 'Alice', 'progress': 0.75},
        {'name': 'Bob', 'progress': 0.42},
    ]
