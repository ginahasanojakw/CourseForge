# === Stage 18: Add an activity log with timestamps and action names ===
# Project: CourseForge
from datetime import datetime, timezone
import logging

logger = logging.getLogger("courseforge")


class ActivityLog:
    """Records user actions with timestamps for audit trails."""

    def __init__(self):
        self._entries = []

    def log(self, action_name: str, details: dict | None = None) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action_name,
            "details": details or {}
        }
        self._entries.append(entry)
        logger.info(f"[{entry['timestamp']}] Action: {entry['action']}")

    def get_recent(self, count: int = 10) -> list[dict]:
        return self._entries[-count:] if len(self._entries) >= count else self._entries.copy()


activity_log = ActivityLog()
