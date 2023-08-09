import argparse
import os
import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from scanner import scan_file

def display_version():
    print("1.0.0")

def display_help():
    print("Usage:")
    print("  python3 cli.py xxx.php           - Perform a single PHP file check")
    print("  python3 cli.py -h / --help       - Show help")
    print("  python3 cli.py -v / --version    - Show version 1.0.0")
    print("  python3 cli.py -f <dir>          - Check all PHP files in the directory")

def scan_directory(directory_path):
    results = []
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.php'):
                file_path = os.path.join(root, file_name)
                file_results = scan_file(file_path)
                if file_results:
                    results.extend(file_results)
    return results


def main():
    parser = argparse.ArgumentParser(add_help=False, description='PHP Code Auditing Tool')
    parser.add_argument('file', type=str, nargs='?', help='PHP file to scan')
    parser.add_argument('-f', '--folder', type=str, help='Directory to scan')
    parser.add_argument('-v', '--version', action='store_true', help='Show version')
    parser.add_argument('-h', '--help', action='store_true', help='Show help')
    args = parser.parse_args()

    if args.help:
        display_help()
        return

    if args.version:
        display_version()
        return

    console = Console()

    if args.file:
        result = scan_file(args.file)
        if result:
            table = Table("Filename", "Line Number", "Warning", "Reason", show_lines=True) 
            for item in result:
                filename, line_number, warning, reason = item
                warning_text = Text(warning)
                if "SQL Injection Warning" in warning:
                    warning_text.stylize("red", 0, len(warning))
                elif "XSS Warning" in warning:
                    warning_text.stylize("yellow", 0, len(warning))
                table.add_row(filename, line_number, warning_text, reason)
            console.print(table)
        return
    

    if args.folder:
        directory_path = args.folder
        if not os.path.exists(directory_path):
            print(f"Invalid directory path: {directory_path}")
            return

        results = scan_directory(directory_path)
        if results:
            table = Table("Filename", "Line Number", "Warning", "Reason", show_lines=True)
            for item in results:
                filename, line_number, warning, reason = item
                warning_text = Text(warning)
                if "SQL Injection Warning" in warning:
                    warning_text.stylize("red", 0, len(warning))
                elif "XSS Warning" in warning:
                    warning_text.stylize("yellow", 0, len(warning))
                table.add_row(filename, line_number, warning_text, reason)
            console.print(table)
        else:
            print("No warnings found.")
        return


if __name__ == "__main__":
    main()
