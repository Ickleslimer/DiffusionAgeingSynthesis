import os
import gzip

def extract_and_delete_gz_files(folder_path):
    """
    This function extracts all .gz files in the given folder
    and all its subfolders, and then deletes the original .gz files.

    Args:
        folder_path: The path to the folder where the search starts.
    """
    for root, directories, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".gz"):
                file_path = os.path.join(root, file)
                extracted_filename = os.path.splitext(file_path)[0]  # Remove .gz extension
                with gzip.open(file_path, 'rb') as gz_file:
                    with open(extracted_filename, 'wb') as extracted_file:
                        extracted_file.write(gz_file.read())
                print(f"Extracted file: {file_path} to {extracted_filename}")
                # Delete the original .gz file
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

# Replace this with your desired folder path
folder_path = r"C:\Users\mrdyl\Desktop\Stripped_Synthrad_MRI_NII"

# This part prints the files to be extracted and deleted and asks for confirmation before performing the actions
print("The following files will be extracted and deleted:")
extract_and_delete_gz_files(folder_path)
