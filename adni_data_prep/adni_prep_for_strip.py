import sys
import subprocess
import os
import shutil
import zipfile

filepath = r"adni_t1"
destination = "adni_t1/adni_skulls"

if len(sys.argv) > 1:
    filepath = sys.argv[1]

if len(sys.argv) > 2:
    destination = sys.argv[2]

os.environ["DESTINATION"] = destination
os.environ["FILEPATH"] = filepath

# Get absolute paths for the scripts
remove_identifiers_script = "adni_data_prep/remove_identifiers.py"

# Execute the scripts using absolute paths
subprocess.run(['python', remove_identifiers_script], check=True)