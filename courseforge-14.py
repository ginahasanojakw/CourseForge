# === Stage 14: Add file load support with fallback demo data ===
# Project: CourseForge
def load_or_demo():
    try:
        with open("course_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "modules": [
                {"id": 1, "title": "Intro", "lessons": [{"id": 101, "content": "Welcome"}]},
                {"id": 2, "title": "Basics", "lessons": []}
            ],
            "learners": [],
            "reviews": []
        }
