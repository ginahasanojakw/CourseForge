# === Stage 27: Add monthly summary calculations ===
# Project: CourseForge
def calculate_monthly_summary(course_data):
    from collections import defaultdict
    monthly_stats = defaultdict(lambda: {'lessons': 0, 'exercises_completed': 0, 'reviews_submitted': 0})
    for learner in course_data.get('learners', []):
        progress = learner.get('progress', {})
        history = progress.get('history', [])
        for event in history:
            date_str = event.get('timestamp', '')
            if not date_str: continue
            try:
                month_key = date_str[:7]  # YYYY-MM
            except Exception:
                continue
            action = event.get('action', '')
            if action == 'lesson_completed':
                monthly_stats[month_key]['lessons'] += 1
            elif action == 'exercise_submitted':
                monthly_stats[month_key]['exercises_completed'] += 1
            elif action == 'review_posted':
                monthly_stats[month_key]['reviews_submitted'] += 1
    summary = []
    for month in sorted(monthly_stats.keys()):
        stats = monthly_stats[month]
        total_activities = sum(stats.values())
        if total_activities > 0:
            avg_per_learner = total_activities / len(course_data.get('learners', [1]))
            entry = {
                'month': month,
                'lessons': stats['lessons'],
                'exercises_completed': stats['exercises_completed'],
                'reviews_submitted': stats['reviews_submitted'],
                'total_activities': total_activities,
                'avg_per_learner': round(avg_per_learner, 2)
            }
            summary.append(entry)
    return sorted(summary, key=lambda x: x['month'])
