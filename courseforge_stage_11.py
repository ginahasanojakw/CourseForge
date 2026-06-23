# === Stage 11: Add JSON export for the current application state ===
# Project: CourseForge
def export_state_to_json(state: dict) -> str:
    import json
    from datetime import datetime
    timestamp = datetime.utcnow().isoformat() + "Z"
    compact_data = {
        "version": 1,
        "timestamp": timestamp,
        "modules": state.get("modules", []),
        "lessons": state.get("lessons", []),
        "exercises": state.get("exercises", []),
        "reviews": state.get("reviews", []),
        "learners": state.get("learners", [])
    }
    return json.dumps(compact_data, indent=2)
