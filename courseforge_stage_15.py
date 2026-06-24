# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: CourseForge
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, command_line):
        parts = command_line.strip().split(maxsplit=1)
        if not parts: return None
        cmd_name, *args = parts
        handler = self.handlers.get(cmd_name)
        if handler:
            try:
                return handler(*args)
            except Exception as e:
                print(f"Error executing '{cmd_name}': {e}")
                return None
        print(f"Unknown command: {command_line}")
        return None

    def register(self, cmd, func):
        self.handlers[cmd.lower()] = func
