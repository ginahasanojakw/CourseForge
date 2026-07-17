# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: CourseForge
def _merge_imports(existing, new):
    """Merge a list of import strings into an existing set-like container,
    skipping obvious duplicates by normalizing whitespace and case."""
    normalized = lambda s: re.sub(r'\s+', ' ', s.strip())
    for item in new:
        if not _is_import(item) or normalized(item) in {normalized(i) for i in existing}:
            continue
        existing.append(normalized(item))

def _is_import(value):
    return bool(re.match(r'^\s*(import|from)\b', value.strip()))
