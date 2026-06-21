# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: CourseForge
def delete_item(item_id, confirm=False):
    if not confirm:
        raise ValueError("Deletion requires explicit confirmation flag set to True.")
    
    # Simulate fetching the item from a global registry or database
    try:
        existing_items = get_all_items()  # Assume this function exists in your context
        items_to_remove = [item for item in existing_items if item['id'] == item_id]
        
        if not items_to_remove:
            print(f"No item found with ID {item_id}.")
            return False
        
        removed_count = len(items_to_remove)
        new_registry = [item for item in existing_items if item['id'] != item_id]
        
        # Update the global registry (or database connection here)
        set_all_items(new_registry)
        
        print(f"Successfully deleted {removed_count} item(s) with ID {item_id}.")
        return True
        
    except Exception as e:
        print(f"Error during deletion of item {item_id}: {e}")
        return False
