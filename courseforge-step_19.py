# === Stage 19: Add undo support for the last simple mutation ===
# Project: CourseForge
class HistoryManager:
    def __init__(self):
        self._stack = []
    
    def push(self, state):
        self._stack.append(state)
    
    def undo(self):
        if self._stack:
            return self._stack.pop()
        return None
    
    def get_history_depth(self):
        return len(self._stack)

def apply_undo(history_manager, current_state):
    last_state = history_manager.undo()
    if last_state is not None:
        # Revert to previous state and notify listeners or update UI
        print(f"Undo applied. Restored state from {last_state.get('timestamp', 'unknown')}.")
        return True
    else:
        print("No more actions to undo.")
        return False

def main():
    history = HistoryManager()
    
    # Simulate a sequence of course modifications
    states = [
        {"module": "Intro", "lessons": 1},
        {"module": "Intro", "lessons": 2, "exercise": "Quiz"},
        {"module": "Advanced", "lessons": 3}
    ]
    
    for state in states:
        history.push(state)
        
        # Allow undo after each step (except the last one if we want to keep current)
        # In a real app, you might only allow undo if user explicitly requested it
        input("Press Enter to add next modification or Ctrl+C to stop.")

if __name__ == "__main__":
    main()
