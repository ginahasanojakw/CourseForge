# === Stage 43: Add CSV import for the primary record type ===
# Project: CourseForge
def import_courses_from_csv(csv_path):
    """Import courses from a CSV file with columns: name, description, level."""
    import csv
    with open(csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            course = Course(
                name=row['name'],
                description=row.get('description', ''),
                level=int(row.get('level', 1))
            )
            courses.append(course)
    return courses
