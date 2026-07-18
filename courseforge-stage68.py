# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: CourseForge
def generate_changelog(activity_log, max_entries=30):
    """Generate a compact changelog from an activity log."""
    entries = []
    for action, user, details in activity_log:
        if len(entries) >= max_entries:
            break
        entry = f"  - [{user}] {action}: {details}"
        entries.append(entry)
    return "\n".join(entries)
