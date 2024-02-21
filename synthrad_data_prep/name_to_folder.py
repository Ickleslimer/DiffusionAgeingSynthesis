import os

def rename_files(folder_path):
  """
  This function renames all files in subfolders of a folder to their immediate parent folder name.

  Args:
    folder_path: The path to the folder where the renaming starts.
  """
  for root, directories, files in os.walk(folder_path):
    parent_folder = os.path.basename(root)
    for file in files:
      old_file_path = os.path.join(root, file)
      new_file_path = os.path.join(root, parent_folder)
      new_file_path = new_file_path + ".nii"
      print(f"Renaming {old_file_path} to {new_file_path}")
      os.rename(old_file_path, new_file_path)

# Replace with your desired folder path
folder_path = r"C:\Users\mrdyl\Downloads\Synthrad data\Task1\Task1\brain"

# This part prints the files to be renamed and asks for confirmation before renaming
print("The following files will be renamed:")
rename_files(folder_path)

confirmation = input("Are you sure you want to rename these files? (y/n): ")
if confirmation.lower() == "y":
  rename_files(folder_path)
  print("Files renamed successfully!")
else:
  print("Renaming cancelled.")

