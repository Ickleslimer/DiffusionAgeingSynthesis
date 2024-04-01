import sys
import subprocess
import os

filepath = r"C:\Users\mrdyl\Downloads\Synthrad data\Task1\Task1\brain"
destination = "test"

if len(sys.argv) > 1:
    filepath = sys.argv[1]

if len(sys.argv) > 2:
    destination = sys.argv[2]

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