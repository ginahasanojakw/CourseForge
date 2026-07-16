# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: CourseForge
class ScoringEngine:
    def __init__(self):
        self.weights = {
            'module': 1,
            'lesson': 2,
            'exercise': 3,
            'review': 4,
            'progress': 5,
        }

    def score(self, item_type, value):
        return self.weights.get(item_type, 0) * max(0, min(value / 100.0, 1.0))

    def recommend(self, items):
        scores = [self.score(it['type'], it.get('value', 0)) for it in items]
        return sorted(zip(scores, items), reverse=True)[:3]
