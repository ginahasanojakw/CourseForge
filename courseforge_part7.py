# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: CourseForge
def format_module(module):
    return f"📦 {module['name']}: {len(module.get('lessons', []))} lessons, {len(module.get('exercises', []))} exercises\n   Status: {'✅ Complete' if module.get('completed') else '⏳ In Progress'}\n   Reviews: {sum(1 for l in module.get('lessons', []) for r in l.get('reviews', []) if r)}"

def format_lesson(lesson):
    return f"📄 {lesson['name']}: {len(lesson.get('exercises', []))} exercises\n   Progress: {lesson.get('progress', 0)}/100%\n   Last Review: {lesson.get('last_review') or 'Never'}"

def format_exercise(ex):
    return f"💻 {ex['name']}: {'✅ Solved' if ex.get('solved') else '⏳ Pending'}\n   Code:\n{format_code_block(ex.get('code', ''))}"

def format_review(review):
    return f"⭐ Review by {review['author']}: \"{review['text']}\" ({review['rating']}/5 stars)"

def format_code_block(code, language="python"):
    if not code:
        return "No code provided."
    lines = code.splitlines()
    formatted_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        indent = len(line) - len(stripped)
        prefix = f"{' ' * indent}>" if stripped else ""
        formatted_lines.append(f"{prefix}{line}")
    return "\n".join(formatted_lines)

def format_progress_report(course):
    print("=" * 60)
    print("COURSE FORGE PROGRESS REPORT")
    print("=" * 60)
    
    for module in course.get('modules', []):
        print(format_module(module))
        
        for lesson in module.get('lessons', []):
            if not lesson.get('completed'):
                print("-" * 40)
                print(format_lesson(lesson))
                
                for ex in lesson.get('exercises', []):
                    if not ex.get('solved'):
                        print("  " + "-" * 36)
                        print(format_exercise(ex))
    
    reviews = course.get('reviews', [])
    if reviews:
        print("-" * 40)
        print("RECENT REVIEWS:")
        for r in reviews[-5:]:
            print(f"  {format_review(r)}")
    
    print("=" * 60)
