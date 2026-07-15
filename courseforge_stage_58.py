# === Stage 58: Add bulk update behavior for selected records ===
# Project: CourseForge
def bulk_update_records(self, record_type: str, updates: dict) -> int:
    """Update multiple records of a given type with the same field/value mapping.
    
    Args:
        record_type (str): The type of record to update (e.g., 'module', 'lesson').
        updates (dict): A dictionary where keys are field names and values are the new values.
        
    Returns:
        int: Number of records successfully updated.
        
    Raises:
        ValueError: If updates is empty or if a required field is missing from the provided data.
        
    Example:
        >>> bulk_update_records('module', {'title': 'New Title'})
        3
    """
    if not updates:
        raise ValueError("Update dictionary must contain at least one key-value pair.")

    updated_count = 0
    for record in getattr(self, f'_store_{record_type}', []):
        try:
            for field, value in updates.items():
                setattr(record, field, value)
            updated_count += 1
        except Exception as e:
            raise ValueError(f"Failed to update {record_type}: {e}")

    return updated_count
