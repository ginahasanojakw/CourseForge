# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: CourseForge
from datetime import datetime, timedelta
import json
import os
ARCHIVE_DIR = "archive"
def archive_records(records):
    if not records: return
    cutoff = datetime.now() - timedelta(days=90)
    old = [r for r in records if r.get("completed_at", "") and datetime.fromisoformat(r["completed_at"]) < cutoff]
    new = [r for r in records if r not in old]
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(os.path.join(ARCHIVE_DIR, "old_records.json"), "w") as f: json.dump(old, f, indent=2)
    return new

def restore_records(records):
    archive_path = os.path.join(ARCHIVE_DIR, "old_records.json")
    if not os.path.exists(archive_path): return records
    with open(archive_path) as f: archived = json.load(f)
    return records + archived
