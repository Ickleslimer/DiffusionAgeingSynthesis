import os
import shutil
from pathlib import Path

# Define desktop path using pathlib (recommended)
desktop_path = Path.home() / "Desktop"  # Replace "Desktop" with your desired subfolder on Desktop if needed

# Construct the destination folder path (combine desktop path and folder name)
destination_folder = os.path.join(desktop_path, "Synthrad_MRI_NII")

os.makedirs(destination_folder, exist_ok=True)  # Handles existing folders

root_folder = r"C:\Users\mrdyl\Downloads\Synthrad data\Task1_val\Task1\brain"  

for path, subdirs, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith(".nii"):
            file_path = os.path.join(path, filename)
            destination = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination)

print("All .nii files have been moved to the folder Synthrad_MRI_NII on your Desktop!")

