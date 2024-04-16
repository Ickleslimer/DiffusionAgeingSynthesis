import os
import sys

def rename_files(root_folder):
#Checks all subfolders of target folder and renames files (in this case MRIs) based on their target directory in order to ensure unique filenames
  for root, directories, files in os.walk(root_folder):
    parent_folder = os.path.basename(root)
    for file in files:
      old_file_path = os.path.join(root, file)
      new_file_path = os.path.join(root, parent_folder)
      new_file_path = new_file_path + ".nii"
      print(f"Renaming {old_file_path} to {new_file_path}")
      os.rename(old_file_path, new_file_path)

#Sets folder to check, overwriting with environment variable if set
root_folder = "synthrad_data\Task1\Task1\brain"
environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

rename_files(root_folder)

