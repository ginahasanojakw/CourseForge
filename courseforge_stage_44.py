# === Stage 44: Add backup creation for the data file ===
# Project: CourseForge
import os, shutil, datetime

def create_backup(data_file: str, backup_dir: str = "backups") -> bool:
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    src = data_file
    dst = os.path.join(backup_dir, f"{os.path.basename(src)}_{datetime.datetime.now():%Y%m%d_%H%M%S}.bak")
    try:
        shutil.copy2(src, dst)
        return True
    except (OSError, FileNotFoundError):
        return False
