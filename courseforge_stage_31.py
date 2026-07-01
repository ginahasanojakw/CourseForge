# === Stage 31: Add compact table rendering for long lists ===
# Project: CourseForge
def render_compact_table(data, columns=None):
    if not data: return ""
    if columns is None: columns = list(data[0].keys())
    header = "  ".join(f"{c[:12]:<12}" for c in columns) + "\n"
    rows = []
    for row in data:
        line = "  ".join(str(row.get(c, ""))[:12] for c in columns)
        if len(line) > 60:
            lines = [line[i:i+58] for i in range(0, len(line), 58)]
            rows.extend(lines)
        else:
            rows.append(line)
    return header + "\n".join(rows[:10]) if len(rows) > 10 else header + "\n".join(rows)
