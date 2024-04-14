import ants
import nibabel as nib
import os


root_folder = "synthrad_data/stripped_synthrad"

environpath = os.environ.get("FILEPATH")
if environpath is not None:
  root_folder = environpath

def register_nii_files(root_folder):
    first_nii_path = None

    for path, subdirs, files in os.walk(root_folder):
        for filename in files:
            if filename.endswith(".nii"):
                file_path = os.path.join(path, filename)

                if first_nii_path is None:
                    first_nii_path = file_path
                    template_img = ants.image_read(first_nii_path)
                    print(f"Registered image {filename} as template")
                else:

                    transformation = ants.registration(
                    fixed=template_img,
                    moving=ants.image_read(file_path),
                    type_of_transform='SyN',
                    verbose=True)
                    
                    registered_img = transformation['warpedmovout']
                    registered_img.to_file(os.path.join(root_folder, f"registered_{filename}"))
                    print(f"Registered image {filename}")

register_nii_files(root_folder)
print("Finished registration process")