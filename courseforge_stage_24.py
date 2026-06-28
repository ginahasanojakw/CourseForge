# === Stage 24: Add grouped summaries by category or status ===
# Project: CourseForge
class SummaryGrouping:
    def __init__(self, items):
        self.items = items

    def group_by_status(self):
        groups = {}
        for item in self.items:
            status = getattr(item, 'status', 'unknown')
            if status not in groups:
                groups[status] = []
            groups[status].append(item)
        return {k: len(v) for k, v in groups.items()}

    def group_by_category(self):
        groups = {}
        for item in self.items:
            cat = getattr(item, 'category', 'uncategorized')
            if cat not in groups:
                groups[cat] = []
            groups[cat].append(item)
        return {k: len(v) for k, v in groups.items()}

    def get_summary(self):
        status_counts = self.group_by_status()
        category_counts = self.group_by_category()
        total = sum(status_counts.values())
        return f"Total items: {total}\nBy Status: {status_counts}\nBy Category: {category_counts}"
