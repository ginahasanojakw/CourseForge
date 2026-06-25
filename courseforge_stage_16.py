# === Stage 16: Add argparse support for the most common commands ===
# Project: CourseForge
import argparse

def main():
    parser = argparse.ArgumentParser(description="CourseForge CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create course
    create_parser = subparsers.add_parser('create', help='Create a new course')
    create_parser.add_argument('--name', required=True, help='Course name')
    create_parser.add_argument('--author', default='anonymous', help='Author name')

    # Add module
    add_module_parser = subparsers.add_parser('add-module', help='Add a module to a course')
    add_module_parser.add_argument('--course', required=True, help='Course ID')
    add_module_parser.add_argument('--title', required=True, help='Module title')

    # List courses
    list_parser = subparsers.add_parser('list', help='List all courses')
    list_parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Placeholder logic for command execution
    print(f"Executing command: {args.command}")
    if hasattr(args, 'name'):
        print(f"Course name: {args.name}")
    if hasattr(args, 'course'):
        print(f"Target course: {args.course}")
    return 0

if __name__ == "__main__":
    exit(main())
