import ants
import os


root_folder = "adni_t1"
environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

def register_nii_files(root_folder):
    first_nii_path = None
    #Checks all subdirectories of the target folder for files with the specified file ending and removes them 
    for path, subdirs, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(".nii"):
                file_path = os.path.join(path, filename)

                #Defines the fixed image as the first image found
                if first_nii_path is None:
                    first_nii_path = file_path
                    template_img = ants.image_read(first_nii_path)
                    os.rename(first_nii_path,f"registered_{filename}")
                    print(f"Registered image {filename} as template")
                #Performs registration on all but the first image found
                else:
                    transformation = ants.registration(
                    fixed=ants.image_read("adni_data_prep/ADNI_T1_62/registered_MRI_1_skullstripped.nii"),
                    moving=ants.image_read(file_path),
                    type_of_transform='SyN',
                    verbose=True)
                    
                    #Saves registered image to file
                    registered_img = transformation['warpedmovout']
                    registered_img.to_file(os.path.join(path, f"registered_{filename}"))
                    print(f"Registered image {filename}")

register_nii_files(root_folder)
print("Finished registration process")