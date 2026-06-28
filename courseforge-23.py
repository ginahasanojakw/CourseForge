# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: CourseForge
def manage_tags(tags, text):
    if tags is None: return text
    for tag in tags:
        pattern = f"\\b{tag}\\b"
        text = re.sub(pattern, r"\1", text)
    summary = " | ".join(f"[{t}]" for t in sorted(tags)) if tags else ""
    return f"{summary}: {text}"
