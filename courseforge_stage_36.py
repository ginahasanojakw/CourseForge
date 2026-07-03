# === Stage 36: Add templates for quickly creating common records ===
# Project: CourseForge
class CourseForgeTemplates:
    @staticmethod
    def create_module(name, description=""):
        return {
            "id": f"mod_{name.lower().replace(' ', '_')}",
            "title": name,
            "description": description,
            "lessons": [],
            "created_at": datetime.now().isoformat()
        }

    @staticmethod
    def create_lesson(module_id, title, content=""):
        return {
            "id": f"les_{module_id}_{title.lower().replace(' ', '_')}",
            "moduleId": module_id,
            "title": title,
            "content": content,
            "exercises": [],
            "created_at": datetime.now().isoformat()
        }

    @staticmethod
    def create_exercise(lesson_id, type="code", prompt="", solution=None):
        return {
            "id": f"exe_{lesson_id}_{type}",
            "lessonId": lesson_id,
            "type": type,
            "prompt": prompt,
            "solution": solution or "",
            "tests": [],
            "created_at": datetime.now().isoformat()
        }

    @staticmethod
    def create_review(learner_id, record_id, score=0, comment=""):
        return {
            "id": f"rev_{record_id}_{learner_id}",
            "learnerId": learner_id,
            "recordId": record_id,
            "score": score,
            "comment": comment,
            "created_at": datetime.now().isoformat()
        }

    @staticmethod
    def create_progress(learner_id, module_id, lesson_id=None, completed=False):
        return {
            "id": f"prog_{module_id}_{lesson_id or 'none'}",
            "learnerId": learner_id,
            "moduleId": module_id,
            "lessonId": lesson_id,
            "completed": completed,
            "started_at": datetime.now().isoformat(),
            "finished_at": None if not completed else datetime.now().isoformat()
        }
