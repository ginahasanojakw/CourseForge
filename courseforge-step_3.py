# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: CourseForge
def validate_identifier(value):
    if not value:
        raise ValueError("Identifier cannot be empty")
    return re.sub(r'[^a-zA-Z0-9_-]', '', str(value)).lower()[:50]

def validate_short_text(text, max_length=100):
    if text is None or len(str(text)) > max_length:
        raise ValueError(f"Text exceeds {max_length} characters")
    return str(text).strip()

def validate_required_field(field_name, value):
    if not value:
        raise ValueError(f"{field_name} is required")
    return value
