import os
import gzip
import sys

def extract_named_files(folder_path, filename):
  """
  This function extracts files with the specified name from gz format
  in the given folder and all its subfolders.

  Args:
    folder_path: The path to the folder where the search starts.
    filename: The base name of the files to extract (without the .gz extension).
  """
  for root, directories, files in os.walk(folder_path):
    for file in files:
      if file.endswith(".gz") and file[:-3] == filename:
        file_path = os.path.join(root, file)
        with gzip.open(file_path, 'rb') as gz_file:
          extracted_filename = os.path.join(root, filename)
          with open(extracted_filename, 'wb') as extracted_file:
            extracted_file.write(gz_file.read())
        print(f"Extracted file: {file_path} to {extracted_filename}")

# Replace these with your desired values
folder_path = r"C:\Users\mrdyl\Downloads\Task1\Task1\brain"

environpath = os.environ.get("FILEPATH")
if environpath is not None:
  folder_path = environpath

filename = r"mr.nii"  # Change this to the filename (without .gz)

# This part prints the files to be extracted and asks for confirmation before extracting
print("The following files will be extracted:")
extract_named_files(folder_path, filename)

