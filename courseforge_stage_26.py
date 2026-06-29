# === Stage 26: Add weekly summary calculations ===
# Project: CourseForge
def calculate_weekly_summary(learner_data, week_start):
    """Aggregate progress and reviews for a specific week."""
    summary = {
        "week_start": week_start,
        "total_exercises_completed": 0,
        "average_review_score": 0.0,
        "lessons_mastered": set(),
        "active_days": set()
    }
    
    for entry in learner_data.get("activity_log", []):
        date = entry.get("date")
        if not date.startswith(week_start + "-"):
            continue
        
        summary["total_exercises_completed"] += entry.get("exercises_done", 0)
        
        review_score = entry.get("review_score")
        if review_score is not None:
            summary["average_review_score"] += review_score
        
        lesson_id = entry.get("lesson_id")
        if lesson_id and entry.get("status") == "mastered":
            summary["lessons_mastered"].add(lesson_id)
        
        day_part = date.split("-")[1]
        summary["active_days"].add(day_part)
    
    count = len([e for e in learner_data.get("activity_log", []) if e.get("date").startswith(week_start + "-")])
    if count > 0:
        summary["average_review_score"] /= count
    
    return summary
