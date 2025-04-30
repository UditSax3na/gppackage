import traceback
import datetime
from .config.path import *
from .core.zero import func

try:
    func()


except Exception as e:
    with open(LOG_FILE, 'a') as myfile:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_trace = traceback.format_exc()
        myfile.write(f"[{timestamp}] Error: {str(e)}\n")
        myfile.write(f"[{timestamp}] Traceback:\n{error_trace}\n")
        myfile.write(f"[{timestamp}] File Location: {__file__}\n")
        myfile.write("-" * 60 + "\n")