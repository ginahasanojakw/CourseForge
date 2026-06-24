# === Stage 13: Add file save support using a configurable path ===
# Project: CourseForge
import os
from pathlib import Path

class ConfigurableStorage:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path) if base_path else Path.cwd() / "data"
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save(self, data, filename):
        file_path = self.base_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return str(file_path.relative_to(self.base_path.parent))

    def load(self, filename):
        file_path = self.base_path / filename
        if not file_path.exists():
            raise FileNotFoundError(f"File {filename} not found in storage.")
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_files(self):
        return [f.name for f in self.base_path.iterdir() if f.is_file()]
