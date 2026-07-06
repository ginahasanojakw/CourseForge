# === Stage 42: Add CSV export without external dependencies ===
# Project: CourseForge
import csv, os, json

def export_to_csv(data, filename='export.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    return filename
