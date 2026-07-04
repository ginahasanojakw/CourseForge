# === Stage 38: Add data integrity checks for broken references ===
# Project: CourseForge
def validate_course_integrity(course: dict) -> list[str]:
    errors = []
    for module in course.get("modules", []):
        if "lessons" not in module: continue
        for lesson in module["lessons"]:
            ref_id = lesson.get("exerciseId")
            exercise_list = [m.get("exercises", []) for m in course.get("modules", [])]
            flat_exercises = [e for mod in exercise_list for e in mod]
            if ref_id and not any(e.get("id") == str(ref_id) for e in flat_exercises):
                errors.append(f"Lesson {lesson['title']} references non-existent exercise: {ref_id}")
        review_ids = lesson.get("reviewIds", [])
        if isinstance(review_ids, list):
            for rid in review_ids:
                reviews = [m.get("reviews", []) for m in course.get("modules", [])]
                flat_reviews = [r for mod in reviews for r in mod]
                if not any(r.get("id") == str(rid) for r in flat_reviews):
                    errors.append(f"Lesson {lesson['title']} references non-existent review: {rid}")
    return errors
