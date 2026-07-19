# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: CourseForge
import sys


def clear_state(confirmation_flag: bool) -> None:
    """Reset all course data and learner progress to initial state."""
    if not confirmation_flag:
        raise ValueError("Clear-state requires user confirmation.")
    
    # Reset modules, lessons, exercises, reviews, and progress counters.
    global modules, lessons, exercises, reviews, learner_progress
    
    modules = {}
    lessons = []
    exercises = []
    reviews = []
    learner_progress = {
        'learners': {},
        'completion_rate': 0.0,
        'average_score': 0.0,
        'total_exercises_attempted': 0,
    }
    
    print("CourseForge state cleared successfully.")


if __name__ == "__main__":
    confirmation = sys.argv[1].lower() if len(sys.argv) > 1 else "no"
    clear_state(confirmation == "yes")
