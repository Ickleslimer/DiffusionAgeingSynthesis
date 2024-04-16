import sys
import subprocess
import os
import shutil
import zipfile

#Define folder containing MRIs and output folder for prepared NII files
filepath = r"adni_t1"
destination = "adni_t1/adni_skulls"

#Set environment variables for use in other scripts
os.environ["DESTINATION"] = destination
os.environ["FILEPATH"] = filepath

#Run the script to remove all .identifier files from the copying of data
remove_identifiers_script = "adni_data_prep/remove_identifiers.py"
subprocess.run(['python', remove_identifiers_script], check=True)