# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: CourseForge
import json, pathlib, sys

DATA_FILE = pathlib.Path(__file__).parent / "data" / "demo.json"


def reset_demo_data():
    """Reset all demo data to initial state for manual testing."""
    if DATA_FILE.exists():
        DATA_FILE.unlink()
    print("✓ Demo data removed.")
