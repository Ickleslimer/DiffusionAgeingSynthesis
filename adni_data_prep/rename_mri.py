import os

def rename_nii_files(folder_path):
  """
  This function iterates through a folder and renames all .nii files with a sequential numbering scheme.

  Args:
      folder_path (str): Path to the folder containing .nii files.
  """
  counter = 1
  for filename in os.listdir(folder_path):
    if filename.endswith(".nii"):
      new_filename = f"MRI_{counter}"
      old_filepath = os.path.join(folder_path, filename)
      new_filepath = os.path.join(folder_path, new_filename + ".nii")
      os.rename(old_filepath, new_filepath)
      print(f"Renamed {filename} to {new_filename}")
      counter += 1
      
# Example usage
folder_path = "adni_t1/ADNI_T1_69"
rename_nii_files(folder_path)
