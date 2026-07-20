# === Stage 72: Add Markdown report export ===
# Project: CourseForge
def export_report(course: Course, output_path: str):
    """Export a course summary as an HTML report."""
    lines = ["<html><head><title>CourseForge Report</title>",
             "<style>body{font-family:sans-serif;margin:20px}h1{color:#333}",
             "table{border-collapse:collapse;width:80%}td,th{padding:6px;border:1px solid #ccc}</style></head><body>"]
    lines.append(f"<h1>Report for {course.title}</h1>")
    lines.append(f"<p>Total modules: {len(course.modules)}</p>")
    lines.append("<table><tr><th>Module</th><th>Lessons</th><th>Exercises</th></tr>")
    for mod in course.modules:
        lines.append(f"<tr><td>{mod.title}</td><td>{len(mod.lessons)}</td><td>{sum(len(l.exercises) for l in mod.lessons)}</td></tr>")
    lines.append("</table>")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
