import os

def delete_named_files(root_folder):
    #Checks all subdirectories of the target folder for files with the specified file ending and removes them 
    for root, directories, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".Identifier"):
                file_path = os.path.join(root, file)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)

#Sets the folder to check, overwrites with environment variable if set
root_folder = r"adni_t1"
environpath = os.environ.get("FILEPATH")
if environpath is not None:
    root_folder = environpath

delete_named_files(root_folder)