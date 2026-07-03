# === Stage 34: Add support for multiple local user profiles ===
# Project: CourseForge
import json, os
from pathlib import Path
PROFILE_DIR = Path(__file__).parent / ".profiles"
def get_profiles():
    if not PROFILE_DIR.exists(): PROFILE_DIR.mkdir()
    data_file = PROFILE_DIR / "users.json"
    if not data_file.exists(): return []
    with open(data_file, encoding="utf-8") as f:
        users = json.load(f)
    return [User(**u) for u in users]
def save_profiles(users):
    with open(PROFILE_DIR / "users.json", "w", encoding="utf-8") as f:
        json.dump([{"id": u.id, "name": u.name} for u in users], f, ensure_ascii=False, indent=2)
class User:
    def __init__(self, name="", id=None):
        self._name = name or (f"User_{len(get_profiles())+1}" if not id else None)
        self.id = id or len(get_profiles()) + 1
    @property
    def name(self): return self._name
    def __repr__(self): return f"<User {self.name}>"
