# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: CourseForge
SETTINGS = {
    "app_name": "CourseForge",
    "version": "1.0.33",
    "max_module_depth": 5,
    "review_enabled": True,
    "progress_sync_interval": 60,
    "allowed_extensions": [".py", ".md", ".json"],
}

def update_settings(key: str, value):
    if key in SETTINGS and not isinstance(SETTINGS[key], bool) or (key == "version"):
        SETTINGS[key] = value
        return True
    raise ValueError(f"Invalid setting key: {key}")

def get_setting(key: str, default=None):
    return SETTINGS.get(key, default)

def reset_settings():
    global SETTINGS
    SETTINGS = {
        "app_name": "CourseForge",
        "version": "1.0.33",
        "max_module_depth": 5,
        "review_enabled": True,
        "progress_sync_interval": 60,
        "allowed_extensions": [".py", ".md", ".json"],
    }
