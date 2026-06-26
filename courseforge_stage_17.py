# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: CourseForge
def dry_run_mode():
    import sys, os
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("DRY RUN MODE: No changes will be made to the file system.")
        return True
    return False

def safe_write(path, content):
    if dry_run_mode():
        print(f"[DRY-RUN] Would write {path}:")
        for line in content.splitlines():
            print(f"  -> {line}")
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def safe_append(path, content):
    if dry_run_mode():
        print(f"[DRY-RUN] Would append to {path}:")
        for line in content.splitlines():
            print(f"  + {line}")
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    return True

def safe_remove(path):
    if dry_run_mode():
        print(f"[DRY-RUN] Would remove file: {path}")
        return False
    os.remove(path)
    return True
