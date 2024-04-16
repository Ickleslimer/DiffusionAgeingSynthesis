import sys
import subprocess
import os
import shutil
import zipfile

#Set environment variables for use in other scripts
filepath = r"synthrad_data/Task1/Task1/brain"
destination = "synthrad_data/synthrad_skulls"
os.environ["DESTINATION"] = destination
os.environ["FILEPATH"] = filepath

#Unzips the synthrad task1 base zip file
Synthrad_data_file = "synthrad_data/Task1.zip"
if os.path.exists(Synthrad_data_file):
    with zipfile.ZipFile(Synthrad_data_file, 'r') as zip_ref:
        zip_ref.extractall('synthrad_data/Task1')
else:
    print(f"Error: File '{Synthrad_data_file}' does not exist.")

#Removes 'overview' folder from synthrad library to prevent it causing errors in other scripts
overview_folder = os.path.join(filepath, "overview")
if os.path.exists(overview_folder):
    shutil.rmtree(overview_folder, ignore_errors=True)
    print(f"Folder '{overview_folder}' deleted.")

#Runs the necessary scripts to pre-process for skullstripping in sequence
gz_extract_script = "synthrad_data_prep/gz_extract.py"
delete_script = "synthrad_data_prep/delete.py"
name_to_folder_script = r"synthrad_data_prep/name_to_folder.py"
move_script = "synthrad_data_prep/move_nii.py"

subprocess.run(['python', gz_extract_script], check=True)
subprocess.run(['python', delete_script], check=True)
subprocess.run(['python', name_to_folder_script], check=True)
subprocess.run(['python', move_script], check=True)

#Removes the extracted task 1 folder for space when done, as it is now redundant
if os.path.exists("synthrad_data/Task1"):
    shutil.rmtree("synthrad_data/Task1", ignore_errors=True)
    print(f"Synthrad folder deleted.")