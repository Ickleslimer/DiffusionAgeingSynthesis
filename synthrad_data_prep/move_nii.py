import os
import shutil

root_folder = "adni_t1/ADNI T1 69"
destination_folder = root_folder

environdestination = os.environ.get("DESTINATION")
if environdestination is not None:
  destination_folder = environdestination

os.makedirs(destination_folder, exist_ok=True)  # Handles existing folders


environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

for path, subdirs, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith(".nii"):
            file_path = os.path.join(path, filename)
            destination = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination)

for subdir in subdirs:
  shutil.rmtree(os.path.join(path, subdir), ignore_errors=True)

print("All .nii files have been moved to the folder " + destination_folder + "!")

