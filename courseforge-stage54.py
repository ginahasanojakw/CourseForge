# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: CourseForge
def colorize(text, fg=None, bg=None):
    """Return ANSI-colored string for terminal output."""
    codes = []
    if fg:
        if isinstance(fg, int):
            codes.append(f"\033[38;5;{fg}m")
        elif isinstance(fg, str):
            color_map = {
                'red': 196, 'green': 46, 'yellow': 226, 'blue': 33,
                'purple': 127, 'cyan': 58, 'white': 15, 'black': 0,
            }
            codes.append(f"\033[38;5;{color_map.get(fg.lower(), 15)}m")
    if bg:
        if isinstance(bg, int):
            codes.append(f"\033[48;5;{bg}m")
        elif isinstance(bg, str):
            color_map = {
                'red': 204, 'green': 149, 'yellow': 226, 'blue': 37,
                'purple': 127, 'cyan': 58, 'white': 15, 'black': 0,
            }
            codes.append(f"\033[48;5;{color_map.get(bg.lower(), 15)}m")
    if not codes:
        return text
    end = "\033[0m"
    return "".join(codes) + end + text

def print_progress(lesson, color='green'):
    """Print a colored progress bar for course lessons."""
    total = len(lesson.exercises)
    done = sum(1 for e in lesson.exercises if e.status == 'completed')
    pct = (done / total * 100) if total else 0
    filled = int(pct / 2)
    bar = "█" * filled + "░" * (20 - filled)
    print(colorize(f"[{bar}] {pct:.0f}% — {lesson.title}", fg=color))
