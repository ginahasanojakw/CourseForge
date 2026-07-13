# === Stage 57: Add structured result objects for command handlers ===
# Project: CourseForge
class CommandResult:
    """Base class for structured responses from CourseForge command handlers."""

    def __init__(self, status: str = "ok", message: str = "") -> None:
        self.status = status
        self.message = message

    def to_dict(self) -> dict:
        return {"status": self.status, "message": self.message}


class ExerciseResult(CommandResult):
    """Response after completing an exercise."""

    def __init__(self, passed: bool, score: float, feedback: str = "") -> None:
        super().__init__()
        self.passed = passed
        self.score = score
        self.feedback = feedback

    def to_dict(self) -> dict:
        return {**super().to_dict(), "passed": self.passed, "score": self.score, "feedback": self.feedback}


class LessonResult(CommandResult):
    """Response after completing a lesson."""

    def __init__(self, topics_covered: list[str], time_spent_min: float) -> None:
        super().__init__()
        self.topics_covered = topics_covered
        self.time_spent_min = time_spent_min

    def to_dict(self) -> dict:
        return {**super().to_dict(), "topics_covered": self.topics_covered, "time_spent_min": self.time_spent_min}


class ModuleResult(CommandResult):
    """Response after completing a module."""

    def __init__(self, lessons_completed: int, exercises_passed: int) -> None:
        super().__init__()
        self.lessons_completed = lessons_completed
        self.exercises_passed = exercises_passed

    def to_dict(self) -> dict:
        return {**super().to_dict(), "lessons_completed": self.lessons_completed, "exercises_passed": self.exercises_passed}


class ReviewResult(CommandResult):
    """Response after a peer review."""

    def __init__(self, reviewer_id: str, feedback: list[str], grade: float) -> None:
        super().__init__()
        self.reviewer_id = reviewer_id
        self.feedback = feedback
        self.grade = grade

    def to_dict(self) -> dict:
        return {**super().to_dict(), "reviewer_id": self.reviewer_id, "feedback": self.feedback, "grade": self.grade}


class ProgressResult(CommandResult):
    """Response after updating learner progress."""

    def __init__(self, module_progress: float, course_progress: float) -> None:
        super().__init__()
        self.module_progress = module_progress
        self.course_progress = course_progress

    def to_dict(self) -> dict:
        return {**super().to_dict(), "module_progress": self.module_progress, "course_progress": self.course_progress}


class ErrorResult(CommandResult):
    """Response when a command fails."""

    def __init__(self, error_code: str, details: str = "") -> None:
        super().__init__(status="error", message=details)
        self.error_code = error_code

    def to_dict(self) -> dict:
        return {**super().to_dict(), "error_code": self.error_code}
