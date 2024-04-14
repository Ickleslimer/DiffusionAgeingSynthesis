import os

def delete_named_files(folder_path):
    """
    This function deletes files with the specified names in the given folder
    and all its subfolders.

    Args:
      folder_path: The path to the folder where the search starts.
      filenames: A list of filenames to delete.
    """
    for root, directories, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".nii"):
                file_path = os.path.join(root, file)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)

# Replace these with your desired values
folder_path = r"adni_t1"

environpath = os.environ.get("FILEPATH")
if environpath is not None:
    folder_path = environpath
# This part prints the files to be deleted and asks for confirmation before deleting
delete_named_files(folder_path)