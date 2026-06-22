# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: CourseForge
class CourseForgeSorter:
    def __init__(self, items): self.items = items
    def sort_by_title(self): return sorted(self.items, key=lambda x: (x.get('title', '').lower(), x.get('_id')))
    def sort_by_date(self): return sorted(self.items, key=lambda x: x.get('created_at'), reverse=True)
    def sort_by_priority(self): return sorted(self.items, key=lambda x: x.get('priority', 0), reverse=True)
    def sort_by_last_update(self): return sorted(self.items, key=lambda x: x.get('updated_at'), reverse=True)
    def apply_sort(self, field='title'):
        if field == 'title': return self.sort_by_title()
        elif field == 'date': return self.sort_by_date()
        elif field == 'priority': return self.sort_by_priority()
        elif field == 'last_update': return self.sort_by_last_update()
        else: raise ValueError(f"Unknown sort field: {field}")
