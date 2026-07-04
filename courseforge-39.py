# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: CourseForge
def repair_data_integrity(data):
    if isinstance(data, dict) and 'modules' in data:
        for module_id, module in data['modules'].items():
            if isinstance(module.get('lessons'), list):
                for lesson_idx, lesson in enumerate(module['lessons']):
                    if not isinstance(lesson.get('exercises', []), list):
                        lesson['exercises'] = []
                    for exercise_idx, ex in enumerate(lesson['exercises']):
                        if 'id' not in ex:
                            ex['id'] = f"{module_id}_{lesson_idx}_{exercise_idx}"
                        if 'status' not in ex:
                            ex['status'] = 'pending'
            elif isinstance(module.get('lessons'), dict):
                for lesson_key, lesson in module['lessons'].items():
                    if not isinstance(lesson.get('exercises', []), list):
                        lesson['exercises'] = []
                    for exercise_idx, ex in enumerate(lesson['exercises']):
                        if 'id' not in ex:
                            ex['id'] = f"{module_id}_{lesson_key}_{exercise_idx}"
                        if 'status' not in ex:
                            ex['status'] = 'pending'
    return data
