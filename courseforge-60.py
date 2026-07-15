# === Stage 60: Add saved views for frequently used filters ===
# Project: CourseForge
class SavedFilter:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters

    @staticmethod
    def from_dict(data):
        return SavedFilter(data["name"], data["filters"])

    def to_dict(self):
        return {"name": self.name, "filters": self.filters}


class FilterManager:
    def __init__(self):
        self._saved = {}

    def save_filter(self, name, filters):
        if not name or not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Filter name must be a non-empty string")
        self._saved[name] = SavedFilter.from_dict({"name": name, "filters": filters})

    def delete_filter(self, name):
        if name not in self._saved:
            raise KeyError(f"Saved filter '{name}' does not exist")
        del self._saved[name]

    def get_filters(self):
        return list(self._saved.values())
