# === Stage 41: Add plain text import for a simple line-based format ===
# Project: CourseForge
class TextLoader:
    def __init__(self, path):
        self.path = path
        self.lines = []
        
    def load(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                for line in f:
                    self.lines.append(line.rstrip('\n'))
            return True
        except FileNotFoundError:
            print(f"Error: File {self.path} not found.")
            return False
            
    def get_lines(self):
        return self.lines
        
    def save(self, content_list):
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                for line in content_list:
                    f.write(line + '\n')
            print(f"Saved {len(content_list)} lines to {self.path}")
            return True
        except IOError as e:
            print(f"Error saving file: {e}")
            return False

def parse_exercise_data(text_block):
    """Parses a simple text block into structured exercise data."""
    if not text_block or '\n' not in text_block:
        return None
        
    lines = text_block.strip().split('\n')
    exercises = []
    
    current_exercise = {}
    for line in lines:
        if not line.startswith('#'):
            continue
            
        parts = line.split('=', 1)
        if len(parts) != 2:
            continue
            
        key, value = parts
        
        if key == 'title':
            current_exercise['title'] = value.strip()
        elif key == 'description':
            current_exercise['description'] = value.strip()
        elif key == 'type' and 'question_type' not in current_exercise:
            current_exercise['question_type'] = value.strip()
            
    if current_exercise.get('title'):
        exercises.append(current_exercise)
        
    return exercises
