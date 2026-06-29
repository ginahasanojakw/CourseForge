# === Stage 25: Add daily summary calculations ===
# Project: CourseForge
def calculate_daily_summary(learner_progress):
    from collections import defaultdict, Counter
    daily_stats = defaultdict(lambda: {'completed_lessons': 0, 'reviewed_exercises': 0, 'total_time_minutes': 0})
    for entry in learner_progress:
        date_str = entry.get('date', '')
        if not date_str: continue
        completed = entry.get('lesson_completed') or entry.get('exercise_solved')
        if completed: daily_stats[date_str]['completed_lessons'] += 1
        reviewed = entry.get('reviewed_exercises_count', 0)
        if reviewed > 0: daily_stats[date_str]['reviewed_exercises'] += reviewed
        duration = entry.get('duration_minutes', 0)
        if duration > 0: daily_stats[date_str]['total_time_minutes'] += duration

    summary_list = []
    for date in sorted(daily_stats.keys()):
        stats = daily_stats[date]
        avg_duration = stats['total_time_minutes'] / max(stats['completed_lessons'], 1)
        summary_list.append({
            'date': date,
            'tasks_completed': stats['completed_lessons'] + stats['reviewed_exercises'],
            'avg_session_minutes': round(avg_duration, 1),
            'total_time_minutes': stats['total_time_minutes']
        })

    return summary_list
