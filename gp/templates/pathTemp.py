from pathlib import Path

# Folders
ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / 'config'
CORE_DIR = ROOT / 'core'
LOG_DIR = ROOT / 'log'

# Files
LOG_FILE = LOG_DIR / 'log.txt'

# Function to create folder if don't exists  
def dirCheck():
    for path in [CONFIG_DIR, CORE_DIR, LOG_DIR]:
        path.mkdir(parents=True, exist_ok=True)