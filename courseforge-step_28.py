# === Stage 28: Add overdue item detection based on due dates ===
# Project: CourseForge
from datetime import date, timedelta
def check_overdue_items(course_data):
    today = date.today()
    overdue_list = []
    for module in course_data.get('modules', []):
        if 'lessons' in module:
            for lesson in module['lessons']:
                due_date_str = lesson.get('due_date')
                if due_date_str and not lesson.get('completed'):
                    try:
                        due_date = date.fromisoformat(due_date_str)
                        days_overdue = (today - due_date).days
                        if days_overdue > 0:
                            overdue_list.append({
                                'module': module['name'],
                                'lesson': lesson.get('title'),
                                'overdue_days': days_overdue,
                                'status': 'OVERDUE'
                            })
                    except ValueError:
                        continue
    return overdue_list
