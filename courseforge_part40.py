# === Stage 40: Add plain text report export ===
# Project: CourseForge
def export_report_to_text(course_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=== CourseForge Report ===\n")
        for module in course_data.get('modules', []):
            f.write(f"\n[Module: {module['title']}]\n")
            for lesson in module.get('lessons', []):
                f.write(f"  - Lesson: {lesson['title']}\n")
                for exercise in lesson.get('exercises', []):
                    status = "Completed" if exercise.get('completed') else "Pending"
                    review = exercise.get('review', 'No review yet.')
                    f.write(f"    * Exercise: {exercise['name']} | Status: {status}\n")
                    if review:
                        f.write(f"      Review: {review}\n")
        total_progress = sum(1 for m in course_data.get('modules', []) 
                            for l in m.get('lessons', []) 
                            for e in l.get('exercises', []) if e.get('completed'))
        total_exercises = sum(len(m['lessons'][0].get('exercises', [])) 
                             for m in course_data.get('modules', []))
        f.write(f"\n=== Summary ===\n")
        f.write(f"Total Exercises Completed: {total_progress}\n")
        if total_exercises > 0:
            percentage = (total_progress / total_exercises) * 100
            f.write(f"Completion Rate: {percentage:.1f}%\n")
