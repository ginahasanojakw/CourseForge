# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: CourseForge
class SearchFilter:
    def __init__(self, data):
        self.data = data

    def search(self, query):
        if not query:
            return list(self.data)
        q = query.lower()
        results = []
        for item in self.data:
            text_fields = [item.get('title', ''), item.get('description', ''), item.get('content', '')]
            combined_text = ' '.join(text_fields).lower()
            if q in combined_text:
                results.append(item)
        return results
