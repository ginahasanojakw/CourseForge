# === Stage 45: Add restore from backup with validation ===
# Project: CourseForge
def restore_course(course_data, backup_file):
    """Restore a course from a JSON backup with validation."""
    import json, os

    if not backup_file.endswith(".json"):
        raise ValueError("Backup must be a .json file")

    try:
        with open(backup_file) as f:
            data = json.load(f)
    except Exception as e:
        raise IOError(f"Failed to read backup: {e}") from e

    required_keys = {"name", "modules"}
    for key in required_keys:
        if key not in data or not isinstance(data[key], str):
            raise ValueError(f"Missing or invalid '{key}' in course backup")

    modules_data = data.get("modules", [])
    if not isinstance(modules_data, list) or len(modules_data) == 0:
        raise ValueError("Backup must contain at least one module")

    for i, mod in enumerate(modules_data):
        if not isinstance(mod, dict):
            raise ValueError(f"Module {i} is not a dictionary")
        if "id" not in mod or "title" not in mod:
            raise ValueError(f"Module {i} missing 'id' or 'title'")

    course = {
        "name": data["name"],
        "modules": modules_data,
        "version": 1.0,
        "_source": backup_file,
    }

    output_path = os.path.join(os.path.dirname(backup_file), f"{data['name']}_restored.json")
    with open(output_path, "w") as out:
        json.dump(course, out, indent=2)

    print(f"Course restored to {output_path}")
    return course
