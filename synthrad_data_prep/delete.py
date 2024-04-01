import os
import sys

def delete_named_files(folder_path, filenames):
    """
    This function deletes files with the specified names in the given folder
    and all its subfolders.

    Args:
      folder_path: The path to the folder where the search starts.
      filenames: A list of filenames to delete.
    """
    for root, directories, files in os.walk(folder_path):
        for file in files:
            if file in filenames:
                file_path = os.path.join(root, file)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)

# Replace these with your desired values
folder_path = r"C:\Users\mrdyl\Downloads\Synthrad data\Task1\Task1\brain"

environpath = os.environ.get("FILEPATH")
if environpath is not None:
    folder_path = environpath

filenames = ["mr.nii.gz", "ct.nii.gz", "mask.nii.gz"]  # List of filenames to delete

# This part prints the files to be deleted and asks for confirmation before deleting
print("The following files will be deleted:")
delete_named_files(folder_path, filenames)