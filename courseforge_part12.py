# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: CourseForge
import json, os

def load_safe(path: str) -> dict | None:
    if not os.path.exists(path):
        return {"error": f"File {path} not found"}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "modules" in data:
            return data
        else:
            raise ValueError("Invalid structure: missing 'modules' key or not a dictionary.")
    except json.JSONDecodeError as e:
        return {"error": f"Malformed JSON in {path}: {e.msg}", "line": e.lineno}
    except Exception as e:
        return {"error": f"Unexpected error reading {path}: {str(e)}"}
