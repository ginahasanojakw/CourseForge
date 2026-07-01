# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: CourseForge
from datetime import datetime, timedelta
def get_upcoming_items(items: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).timestamp()
    return [item for item in items if item.get('due_date', '') and float(item['due_date']) <= cutoff]

def format_upcoming_summary(items: list[dict]) -> str:
    now = datetime.now().strftime('%d.%m')
    lines = ['Upcoming reminders:', '']
    for i, item in enumerate(sorted(items, key=lambda x: x.get('due_date', '')), 1):
        date_str = item['due_date'].split('T')[0] if isinstance(item['due_date'], str) else datetime.fromtimestamp(float(item['due_date'])).strftime('%d.%m')
        lines.append(f'{i}. {item["title"]} ({date_str}) - {item.get("description", "")[:50]}...')
    return '\n'.join(lines)

def filter_by_category(items: list[dict], category: str = None) -> list[dict]:
    if not category:
        return items
    return [item for item in items if item.get('category', '').lower() == category.lower()]
