import os
import sys

def delete_named_files(root_folder, filenames):
    #Iterates through all subfolders of the target folder, checking files found against the list of filenames to remove and removing a match
    for root, directories, files in os.walk(root_folder):
        for file in files:
            if file in filenames:
                file_path = os.path.join(root, file)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)

#Sets folder to check, overwriting with environment variable if set
root_folder = r"synthrad_data\Task1\Task1\brain"
environpath = os.environ.get("FILEPATH")
if environpath is not None:
    root_folder = environpath

#Define filenames to remove
filenames = ["mr.nii.gz", "ct.nii.gz", "mask.nii.gz"]

delete_named_files(root_folder, filenames)