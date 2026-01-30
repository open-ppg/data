import json
import sys
from pathlib import Path

# --- 1. File Path Configuration ---
SRC_DIR = Path(__file__).resolve().parent        # data/src
BASE_DIR = SRC_DIR.parent                        # data

DATA_FILE_PATH = SRC_DIR / 'datasets_info.json'
TEMPLATE_FILE_PATH = SRC_DIR / 'template_webpage.html'
OUTPUT_FILE_PATH = BASE_DIR / 'docs' / 'index.html'

# Ensure output directory exists
OUTPUT_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

# --- 2. File I/O Functions ---

def load_datasets(filepath: Path) -> list:
    """Reads dataset information from the external JSON file."""
    if not filepath.exists():
        print(f"Error: Data file not found at {filepath}", file=sys.stderr)
        return []
    try:
        with filepath.open('r', encoding='utf-8') as f:
            print(f" - Reading dataset info from {filepath}...")
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}", file=sys.stderr)
        return []

def load_template(filepath: Path) -> str:
    """Reads the HTML template from a separate file."""
    if not filepath.exists():
        print(f"Error: Template file not found at {filepath}", file=sys.stderr)
        return ""
    try:
        with filepath.open('r', encoding='utf-8') as f:
            print(f" - Reading template html webpage from {filepath}...")
            return f.read()
    except IOError as e:
        print(f"Error reading template file: {e}", file=sys.stderr)
        return ""

def generate_html_content(datasets: list, template: str) -> str:
    """Generates the final HTML content by injecting the serialized JSON data."""
    if not datasets or not template:
        # Return a simple error page if loading failed
        return "<html><body><h1>Error</h1><p>Failed to load data or template.</p></body></html>"

    # Serialize the datasets list into a JSON string for safe injection into the JavaScript
    datasets_json_string = json.dumps(datasets, indent=4)

    # Inject the JSON string into the template placeholder
    final_html = template.replace('{DATASETS_PLACEHOLDER}', datasets_json_string)
    return final_html

def save_html_file(filepath: Path, content: str):
    """Saves the final HTML content to the specified file path."""
    print(f" - Writing final HTML content to {filepath}...")
    try:
        with filepath.open('w', encoding='utf-8') as f:
            f.write(content)
        print(f"   - Successfully wrote HTML content to {filepath}")
    except IOError as e:
        print(f"   - Error writing HTML file: {e}", file=sys.stderr)

# --- 3. Main Execution Block ---

def main():
    # 1. Load Data from JSON
    datasets_db = load_datasets(DATA_FILE_PATH)

    # 1.1. Order datasets by number of subjects (descending)
    datasets_db.sort(key=lambda x: x.get('subjects', 0), reverse=True)

    # 2. Load Template from HTML file
    html_template = load_template(TEMPLATE_FILE_PATH)

    # 3. Generate HTML
    final_html = generate_html_content(datasets_db, html_template)

    # 4. Save HTML to file
    save_html_file(OUTPUT_FILE_PATH, final_html)

if __name__ == "__main__":
    main()
