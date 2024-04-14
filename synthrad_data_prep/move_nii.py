import os
import shutil
from pathlib import Path
import sys

# Define desktop path using pathlib (recommended)
desktop_path = Path.home() / "Desktop"  # Replace "Desktop" with your desired subfolder on Desktop if needed

destination_name = "untitled"

environdestination = os.environ.get("DESTINATION")
if environdestination is not None:
  destination_folder = environdestination
# Construct the destination folder path (combine desktop path and folder name)

os.makedirs(destination_folder, exist_ok=True)  # Handles existing folders

root_folder = "synthrad_data\Task1\Task1\brain"

environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

for path, subdirs, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith(".nii"):
            file_path = os.path.join(path, filename)
            destination = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination)

print("All .nii files have been moved to the folder " + destination_folder + "!")

