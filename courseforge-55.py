# === Stage 55: Add a setting to disable colorized output ===
# Project: CourseForge
import sys

class ColorizedOutput:
    """Manages whether output is colorized based on terminal support and user preference."""
    
    def __init__(self):
        self._enabled = None
    
    @property
    def enabled(self) -> bool:
        if self._enabled is None:
            return sys.stdout.isatty()
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
    
    def reset(self) -> None:
        """Reset to auto-detect terminal support."""
        self._enabled = None
    
    def print_progress(self, message: str) -> None:
        """Print progress indicator with optional colorization."""
        if self.enabled:
            sys.stdout.write(f"\033[1;36m{message}\033[0m\n")
        else:
            print(message)
    
    def print_section(self, title: str = "") -> None:
        """Print a section header with optional colorization."""
        if self.enabled and title:
            sys.stdout.write(f"\n\033[1;34m{'='*len(title)} {title} {'='*len(title)}\033[0m\n")
        else:
            print(f"\n{'=' * (len(title) + 2)} {title} {'=' * (len(title) + 2)}")
    
    def print_result(self, value) -> None:
        """Print a result with optional colorization."""
        if self.enabled and isinstance(value, str):
            sys.stdout.write(f"\033[1;32m{value}\033[0m\n")
        else:
            print(str(value))
