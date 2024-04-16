import os

def rename_nii_files(root_folder):
  #Names NII files with a sequential naming scheme as opposed to the complicated default name
  counter = 1
  for filename in os.listdir(root_folder):
    if filename.endswith(".nii"):
      new_filename = f"MRI_{counter}"
      old_filepath = os.path.join(root_folder, filename)
      new_filepath = os.path.join(root_folder, new_filename + ".nii")
      os.rename(old_filepath, new_filepath)
      print(f"Renamed {filename} to {new_filename}")
      counter += 1
      
      import os

def append_age_to_mri(root_folder):
  #Adds the age from the target folder to the jpg files from decomposed NII files
  for subdir, _, files in os.walk(root_folder):
    folder_number = subdir.split("_")[-1]
    for filename in files:
      if filename.startswith("registered_MRI_"):
        new_filename = f"registered_{folder_number}_MRI_{filename[16:]}"
        os.rename(os.path.join(subdir, filename), os.path.join(subdir, new_filename))

root_folder = "adni_t1"
append_age_to_mri(root_folder)
