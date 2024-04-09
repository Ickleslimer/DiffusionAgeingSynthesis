import sys
import subprocess
import os
import shutil
import zipfile

filepath = r"synthrad_data/Task1/Task1/brain"
destination = "synthrad_data/synthrad_skulls"
overview_folder = os.path.join(filepath, "overview")
pelvis_folder = "synthrad_data/Task1/Task1/pelvis"

if len(sys.argv) > 1:
    filepath = sys.argv[1]

if len(sys.argv) > 2:
    destination = sys.argv[2]

os.environ["DESTINATION"] = destination
os.environ["FILEPATH"] = filepath

Synthrad_data_file = "synthrad_data/Task1.zip"

if os.path.exists(Synthrad_data_file):
    with zipfile.ZipFile(Synthrad_data_file, 'r') as zip_ref:
        zip_ref.extractall('synthrad_data/Task1')
else:
    print(f"Error: File '{Synthrad_data_file}' does not exist.")

    
if os.path.exists(overview_folder):
    shutil.rmtree(overview_folder, ignore_errors=True)
    print(f"Folder '{overview_folder}' deleted.")

# Get absolute paths for the scripts
gz_extract_script = "synthrad_data_prep/gz_extract.py"
delete_script = "synthrad_data_prep/delete.py"
name_to_folder_script = r"synthrad_data_prep/name_to_folder.py"
move_script = "synthrad_data_prep/move_nii.py"

# Execute the scripts using absolute paths
subprocess.run(['python', gz_extract_script], check=True)
subprocess.run(['python', delete_script], check=True)
subprocess.run(['python', name_to_folder_script], check=True)
subprocess.run(['python', move_script], check=True)

if os.path.exists("synthrad_data/Task1"):
    shutil.rmtree("synthrad_data/Task1", ignore_errors=True)
    print(f"Synthrad folder deleted.")