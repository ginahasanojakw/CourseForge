# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: CourseForge
def update_record(record_id, updates):
    if record_id in records:
        for key, value in updates.items():
            if key in records[record_id]:
                records[record_id][key] = value
            else:
                raise ValueError(f"Field {key} does not exist for record {record_id}")
        return True
    else:
        raise KeyError(f"Record with id {record_id} not found")
