import os
from datetime import datetime

# Get absolute path to the current script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Define the target file name
filename = "example.txt"
file_path = os.path.join(script_dir, filename)

# Check if file exists
if os.path.exists(file_path):
    # Get modification time
    mod_timestamp = os.path.getmtime(file_path)
    mod_datetime = datetime.fromtimestamp(mod_timestamp)
    
    print(f"File '{filename}' was last modified at: {mod_datetime}")
else:
    print(f"File '{filename}' does not exist.")
