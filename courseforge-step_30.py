# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: CourseForge
from datetime import datetime, date
import re

def parse_date(date_str: str) -> date | None:
    """Parse common date formats and return a date object or None if invalid."""
    patterns = [
        (r'(\d{4})-(\d{2})-(\d{2})', '%Y-%m-%d'),
        (r'(\d{1,2})/(\d{1,2})/(\d{2,4})', lambda m: ('%m/%d/%y' if len(m.group(3)) == 2 else '%m/%d/%Y')),
        (r'(\w+),\s*(\d{1,2}),?\s*(\d{4})', None), # Requires month mapping
    ]
    for pattern, fmt in patterns:
        match = re.match(pattern, date_str.strip())
        if match:
            try:
                return datetime.strptime(date_str.strip(), fmt).date() if isinstance(fmt, str) else \
                       datetime.strptime(f"{match.group(1)}/{match.group(2)}/{match.group(3)}", '%m/%d/%Y').date()
            except ValueError:
                continue
    raise ValueError(f"Unable to parse date string: {date_str}")

def normalize_date(date_obj: date | str, default: date = None) -> date:
    """Normalize input to a standard date object using current day if missing."""
    if isinstance(date_obj, str):
        try:
            return parse_date(date_obj)
        except ValueError as e:
            raise RuntimeError(f"Invalid date format provided: {date_obj}. Error: {e}") from e
    elif isinstance(date_obj, datetime):
        return date_obj.date()
    elif default is not None:
        return default
    else:
        return date.today()
