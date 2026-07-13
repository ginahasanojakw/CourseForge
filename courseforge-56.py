# === Stage 56: Add compact error classes for domain failures ===
# Project: CourseForge
class CourseForgeError(Exception):
    """Base class for all CourseForge domain errors."""


class ModuleNotFoundError(CourseForgeError):
    pass


class LessonNotFoundError(CourseForgeError):
    pass


class ExerciseNotFoundError(CourseForgeError):
    pass


class ReviewConflictError(CourseForgeError):
    pass


class ProgressUpdateError(CourseForgeError):
    pass


class LearnerNotEnrolledError(CourseForgeError):
    pass


class InvalidLessonOrderError(CourseForgeError):
    pass


class ContentValidationError(CourseForgeError):
    pass


class CollaborationConflictError(CourseForgeError):
    pass


class ResourceExhaustionError(CourseForgeError):
    pass
