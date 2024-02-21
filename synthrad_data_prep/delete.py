import os

def delete_named_files(folder_path, filename):
  """
  This function deletes files with the specified name in the given folder
  and all its subfolders.

  Args:
    folder_path: The path to the folder where the search starts.
    filename: The name of the files to delete.
  """
  for root, directories, files in os.walk(folder_path):
    for file in files:
      if file == filename:
        file_path = os.path.join(root, file)
        print(f"Deleting file: {file_path}")
        os.remove(file_path)

# Replace these with your desired values
folder_path = r"C:\Users\mrdyl\Downloads\Synthrad data\Task1\Task1\brain"
filename = r"mr.nii.gz"  # Change this to the filename you want to delete

# This part prints the files to be deleted and asks for confirmation before deleting
print("The following files will be deleted:")
delete_named_files(folder_path, filename)

confirmation = input("Are you sure you want to delete these files? (y/n): ")
if confirmation.lower() == "y":
  delete_named_files(folder_path, filename)
  print("Files deleted successfully!")
else:
  print("Deletion cancelled.")

