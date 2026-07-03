# === Stage 35: Add active user switching and user-specific records ===
# Project: CourseForge
from typing import Optional, Dict, Any
import json
from pathlib import Path

class UserContext:
    def __init__(self):
        self.active_user_id: Optional[str] = None
        self.user_records: Dict[str, Dict[str, Any]] = {}
    
    def set_active(self, user_id: str) -> None:
        if not self.active_user_id and self.user_records:
            raise RuntimeError("No records initialized")
        self.active_user_id = user_id
    
    def get_record(self, key: str) -> Optional[Any]:
        if not self.active_user_id or self.active_user_id not in self.user_records:
            return None
        record = self.user_records[self.active_user_id].get(key)
        return record if record is not None else None
    
    def set_record(self, key: str, value: Any) -> None:
        if not self.active_user_id or self.active_user_id not in self.user_records:
            raise RuntimeError("No active user")
        self.user_records[self.active_user_id][key] = value
    
    def save_state(self, path: Path) -> None:
        state = {
            "active_user": self.active_user_id,
            "records": self.user_records
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    def load_state(self, path: Path) -> None:
        if not path.exists():
            return
        with open(path, 'r', encoding='utf-8') as f:
            state = json.load(f)
        self.active_user_id = state.get("active_user")
        self.user_records = state.get("records", {})

# Usage example within CourseForge context
if __name__ == "__main__":
    ctx = UserContext()
    # Simulate loading existing state if any
    # ctx.load_state(Path("courseforge_state.json"))
    
    # Switch to a specific learner
    ctx.set_active("learner_01")
    ctx.set_record("progress", {"module_1": 85, "module_2": 40})
    ctx.set_record("reviews", [{"topic": "Python Basics", "score": 9.5}])
    
    # Retrieve current progress for active user
    print(f"Current Progress: {ctx.get_record('progress')}")
