import sys
import subprocess
import os
import shutil
import gzip

filepath = r"C:\Users\mrdyl\Downloads\Task1\Task1\brain"
destination = "test"
overview_folder = os.path.join(filepath, "overview")

if len(sys.argv) > 1:
    filepath = sys.argv[1]

if len(sys.argv) > 2:
    destination = sys.argv[2]

if os.path.exists(overview_folder):
    shutil.rmtree(overview_folder, ignore_errors=True)
    print(f"Folder '{overview_folder}' deleted.")

os.environ["DESTINATION"] = destination
os.environ["FILEPATH"] = filepath

# Get absolute paths for the scripts
gz_extract_script = r"C:\Users\mrdyl\OneDrive\Documents\DiffusionAgeingSynthesis\synthrad_data_prep\gz_extract.py"
delete_script = r"C:\Users\mrdyl\OneDrive\Documents\DiffusionAgeingSynthesis\synthrad_data_prep\delete.py"
name_to_folder_script = r"C:\Users\mrdyl\OneDrive\Documents\DiffusionAgeingSynthesis\synthrad_data_prep\name_to_folder.py"
move_script = r"C:\Users\mrdyl\OneDrive\Documents\DiffusionAgeingSynthesis\synthrad_data_prep\move_nii.py"

# Execute the scripts using absolute paths
subprocess.run(['python', gz_extract_script], check=True)
subprocess.run(['python', delete_script], check=True)
subprocess.run(['python', name_to_folder_script], check=True)
subprocess.run(['python', move_script], check=True)