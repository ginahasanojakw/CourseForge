# === Stage 32: Add pagination helpers for long console output ===
# Project: CourseForge
def paginate_output(text, max_lines=15):
    """Yields chunks of text limited by line count for console readability."""
    lines = text.splitlines()
    if len(lines) <= max_lines:
        yield text
        return
    chunk_size = (len(lines) + max_lines - 1) // max_lines
    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i+chunk_size])
        if i == 0:
            yield f"[Page {i//chunk_size + 1}/{len(lines)//chunk_size + (1 if len(lines)%chunk_size else 0)}]\n{chunk}"
        else:
            yield chunk

def format_large_output(text, max_lines=15):
    """Returns a single formatted string with pagination headers."""
    lines = text.splitlines()
    total_pages = (len(lines) + max_lines - 1) // max_lines if len(lines) > max_lines else 1
    result = f"[Page 1/{total_pages}]\n{text[:max_lines*80].replace(chr(10), chr(10)+chr(97))}" # Simplified visual break logic for demo
    return text
