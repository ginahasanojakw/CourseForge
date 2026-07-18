# === Stage 67: Add a function that returns key project metrics ===
# Project: CourseForge
def get_project_metrics():
    """Return key CourseForge metrics."""
    try:
        with open("README.md", "r") as f:
            readme = f.read()
    except FileNotFoundError:
        readme = ""
    
    total_lines = sum(1 for _ in open(__file__)) - 1
    
    try:
        import subprocess
        result = subprocess.run(["git", "log", "--oneline"], capture_output=True, text=True)
        commits = len(result.stdout.strip().split("\n")) if result.stdout.strip() else 0
    except Exception:
        commits = 0

    metrics = {
        "total_lines": total_lines,
        "commits": commits,
        "readme_length": len(readme),
        "project_name": "CourseForge",
        "feature_count": 67
    }
    
    return metrics
