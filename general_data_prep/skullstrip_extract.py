import os
import gzip

def extract_and_delete_gz_files(root_folder):
#Checks all subdirectories of the target folder for files ending in .gz, extracts them using gzip and deletes the .gz file. 
    for root, directories, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".gz"):
                file_path = os.path.join(root, file)
                extracted_filename = os.path.splitext(file_path)[0] 
                with gzip.open(file_path, 'rb') as gz_file:
                    with open(extracted_filename, 'wb') as extracted_file:
                        extracted_file.write(gz_file.read())
                print(f"Extracted file: {file_path} to {extracted_filename}")
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

#Sets the new destination folder for scripts (as the new folder is where the .nii files are kept)
root_folder = "adni_t1"
os.environ["DESTINATION"] = root_folder
if os.path.exists(root_folder) == False:
    print(f"Error: Folder '{root_folder}' does not exist.")
extract_and_delete_gz_files(root_folder)
