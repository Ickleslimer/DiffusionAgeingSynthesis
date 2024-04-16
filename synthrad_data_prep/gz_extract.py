import os
import gzip
import sys

def extract_named_files(root_folder, filename):
#Iterates through all subfolders of the target folder, checking files found against the set filename and extracting matches
  for root, directories, files in os.walk(root_folder):
    for file in files:
      if file.endswith(".gz") and file[:-3] == filename:
        file_path = os.path.join(root, file)
        with gzip.open(file_path, 'rb') as gz_file:
          extracted_filename = os.path.join(root, filename)
          with open(extracted_filename, 'wb') as extracted_file:
            extracted_file.write(gz_file.read())
        print(f"Extracted file: {file_path} to {extracted_filename}")

#Sets folder to check, overwriting with environment variable if set
root_folder = r"synthrad_data\Task1\Task1\brain"
environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

filename = r"mr.nii"

extract_named_files(root_folder, filename)

