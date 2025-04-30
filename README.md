# gp – Python Project Generator

`gp` is a lightweight Python command-line tool to scaffold a new project structure with built-in logging, config handling, and optional package support.

---

## Features

- Creates a base project folder with:
  - `logs/` – for log storage
  - `config/` – for configuration files
  - `core/` – for core application logic
- Adds helpful boilerplate:
  - `main.py` or `__main__.py`
  - `config/path.py` with auto-directory creation logic
  - `log.txt` for error tracking
  - Optional `__init__.py` for packaging
- Includes basic error logging setup using `traceback` and `datetime`
- Generates an empty `README.md`

---
## Setps to setup this package
### 1. Clone the Repository
First, clone the repository to your system:
```bash
git clone https://github.com/UditSax3na/gppackage.git
cd gppackage
```

### 2. Install the Package
Run the following command to install the package using pip:

```bash
pip install .
```
Or for development use (recommended if you plan to modify the code):
```bash
pip install -e .
```
This will make the gp command available globally in your terminal.

### 3. Add to System PATH (if needed)
If the gp command doesn't work globally, make sure your Python Scripts/ or bin/ directory is added to your system PATH.

On Windows
Find where gp.exe or gp is installed:

```bash
where gp
```
>Copy that path and add it to your System Environment Variables > PATH.

On Linux/macOS
Use:
```bash
which gp
```
>Add the containing folder to your .bashrc, .zshrc, or equivalent:

```bash
export PATH="$PATH:/path/to/folder"
```
---

## Usage
```bash
gp <project_name> [--path <target_directory>] [--package | -p]
```
#### Arguments
| Argument        | Description                                |
|-----------------|--------------------------------------------|
| `project_name`  | Name of the project folder to create       |
| `--path`        | Base directory where the project goes (default: current directory) |
| `--package`, `-p` | Creates `__init__.py` and uses `__main__.py` as entry point |

---

## Example Commands
```bash
# Create a project called 'myapp' in the current directory
gp myapp 

# Create a package called 'myapp' in the current directory
gp myapp -p

# Create a packaged project inside /c/Users/you/projects
gp myapp --path /c/Users/you/projects --package
```

---

## Generated Structure
Example (with --package flag):
```
myapp/
├── logs/
│   └── log.txt
├── config/
│   └── path.py
├── core/
│   └── zero.py
├── __init__.py
├── __main__.py
└── README.md
```

---

## Logging & Error Handling
The generated main file includes basic error tracking:
- Catches exceptions
- Logs error message, traceback, and file path
- Appends them to logs/log.txt  

---

## Requirements
- Python 3.7+
- pathlib (included in Python 3.4+)

---

## Author
Made By [UditSax3na](github.com/UditSax3na)