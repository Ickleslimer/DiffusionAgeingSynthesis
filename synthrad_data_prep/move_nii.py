import os
import shutil

#Sets folders to move file to/from, overwriting with environment variables if set
root_folder = "adni_t1/ADNI_T1_57"
destination_folder = root_folder
environdestination = os.environ.get("DESTINATION")
if environdestination is not None:
  destination_folder = environdestination
environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

#Creates destination folder if it does not exist
os.makedirs(destination_folder, exist_ok=True)
def rename_files(root_folder):
#Iterates through all subfolders of target folder and moves any file ending in .nii to the destination folder
  for path, subdirs, files in os.walk(root_folder):
      for filename in files:
          if filename.endswith(".nii"):
              file_path = os.path.join(path, filename)
              destination = os.path.join(destination_folder, filename)
              shutil.move(file_path, destination)

print("All .nii files have been moved to the folder " + destination_folder + "!")

