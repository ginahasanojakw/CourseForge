# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: CourseForge
def confirm_bulk_delete(self, items):
    """Return True only if every item is marked for deletion."""
    return all(item.get("deleted", False) for item in items)
