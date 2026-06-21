# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: CourseForge
class CourseFilter:
    def __init__(self, items):
        self.items = items

    def filter_by_status(self, status):
        return [item for item in self.items if getattr(item, 'status', None) == status]

    def filter_by_category(self, category):
        return [item for item in self.items if getattr(item, 'category', None) == category]

    def filter_by_owner(self, owner_name):
        return [item for item in self.items if getattr(item, 'owner', None).get('login') == owner_name]

    def filter_by_tag(self, tag):
        tags = getattr(item, 'tags', [])
        return [item for item in self.items if any(tag.lower() in t.lower() for t in tags)]

    def apply_filters(self, status=None, category=None, owner=None, tag=None):
        result = self.items
        if status:
            result = self.filter_by_status(status)
        if category:
            result = [item for item in result if getattr(item, 'category', None) == category]
        if owner:
            result = [item for item in result if getattr(item, 'owner', None).get('login') == owner]
        if tag:
            result = [item for item in result if any(tag.lower() in t.lower() for t in getattr(item, 'tags', []))]
        return result
