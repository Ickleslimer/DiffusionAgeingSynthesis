import os
import nibabel as nib
from PIL import Image
import numpy as np

def convert_nii_to_jpg(nii_folder, output_folder_base):
  """
  This function takes a folder path containing .nii files and a base path for output folders 
  as input. It iterates through each .nii file, converts all slices into jpgs, 
  and deletes the original .nii file.

  Args:
      nii_folder (str): Path to the folder containing .nii files.
      output_folder_base (str): Base path to create/home/ickleslimer/Documents/DiffusionAgeingSynthesis/synthrad_data/stripped_synthrad/1BA105_skullstripped separate output folders for each nii file.
  """
  for path, subdirs, files in os.walk(nii_folder):
    for filename in files:
        if filename.endswith(".nii"):
      # Extract file name without extension
        file_name, _ = os.path.splitext(filename)
      # Create output folder with filename as name
        output_folder = os.path.join(output_folder_base, file_name)
        os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
      
      # Full path to the nii file
        nii_file = os.path.join(nii_folder, filename)
      
        try:
          convert_single_nii(nii_file, output_folder)
        # Delete nii file after successful conversion
        #os.remove(nii_file)
          print(f"Converted {nii_file} to jpgs and deleted the original file.")
        except Exception as e:
          print(f"Error converting {nii_file}: {e}")
      
def convert_single_nii(nii_file, output_folder):
  """
  Helper function to convert a single nii file to jpgs in a specified folder.

  Args:
      nii_file (str): Path to the nii file.
      output_folder (str): Path to the folder where jpgs will be saved.
  """
  # Load the .nii file
  img = nib.load(nii_file)
  img_data = img.get_fdata()

  # Loop through each slice and save as jpg
  for slice_num in range(img_data.shape[2]):
    slice_data = img_data[:, :, slice_num]
    # Convert data type (assuming data is in range 0-255)
    slice_data = slice_data.astype(np.uint8)  
    img = Image.fromarray(slice_data)
    # Specify filename with slice number
    output_filename = f"{output_folder}/slice_{slice_num}.jpg"
    img.save(output_filename)

def extract_middle_slices(nii_folder, output_folder):
  """
  This function takes a folder path containing .nii files and an output folder path as input.
  It iterates through each .nii file, extracts the middle slice, and saves it as a jpg in the output folder.

  Args:
      nii_folder (str): Path to the folder containing .nii files.
      output_folder (str): Path to the output folder where middle slices will be saved.
  """
  os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist
  for path, subdirs, files in os.walk(nii_folder):
    for filename in files:
      if filename.endswith(".nii"):
      # Extract file name without extension
        file_name, _ = os.path.splitext(filename)
      
      # Full path to the nii file
        nii_file = os.path.join(nii_folder, filename)
      
        try:
        # Load the .nii file
          img = nib.load(nii_file)
          img_data = img.get_fdata()
        
        # Calculate the middle slice index (integer division for floor)
          middle_slice = img_data.shape[2] // 2
        
        # Extract the middle slice
          middle_slice_data = img_data[:, :, middle_slice]
        
        # Convert data type (assuming data is in range 0-255)
          middle_slice_data = middle_slice_data.astype(np.uint8)  
          img = Image.fromarray(middle_slice_data)
        
        # Specify filename with original name and "_middle" suffix
          output_filename = f"{output_folder}/{file_name}_middle.jpg"
          img.save(output_filename)
          print(f"Extracted middle slice from {nii_file} and saved to {output_filename}")
        except Exception as e:
          print(f"Error processing {nii_file}: {e}")

def extract_middle_percentage_slices(nii_folder, output_folder_base, percentage=0.3):
  """
  This function iterates through all .nii files in a folder, extracts a specified percentage of slices around the middle of each, and saves them as jpgs.

  Args:
      nii_folder (str): Path to the folder containing nii files.
      output_folder_base (str): Base path to create separate output folders for each nii file.
      percentage (float, optional): Percentage of slices to extract around the middle (defaults to 0.3).
  """
  for path, subdirs, files in os.walk(nii_folder):
    for filename in files:
      if filename.endswith(".nii"):
      # Extract file name without extension
        file_name, _ = os.path.splitext(filename)
      # Create output folder with filename as name
        output_folder = os.path.join(output_folder_base, file_name)
        os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

      # Full path to the nii file
        nii_file = os.path.join(nii_folder, filename)

        try:
        # Extract and save middle percentage slices
          extract_middle_percentage_slices_single(nii_file, output_folder, percentage)
          print(f"Extracted middle {percentage*100:.0f}% slices from {nii_file} and saved to {output_folder}")
        except Exception as e:
          print(f"Error processing {nii_file}: {e}")

def extract_middle_percentage_slices_single(nii_file, output_folder, percentage=0.3):
  """
  This function extracts a specified percentage of slices around the middle of a nii file and saves them as jpgs.

  Args:
      nii_file (str): Path to the nii file.
      output_folder (str): Path to the folder where jpgs will be saved.
      percentage (float, optional): Percentage of slices to extract around the middle (defaults to 0.3).
  """
  # Load the .nii file
  img = nib.load(nii_file)
  img_data = img.get_fdata()
  num_slices = img_data.shape[2]

  # Calculate the number of slices to extract based on percentage
  num_extract_slices = int(num_slices * percentage) // 2

  # Starting and ending slice indexes (rounded down for floor division)
  start_slice = (num_slices // 2) - num_extract_slices
  end_slice = (num_slices // 2) + num_extract_slices

  # Loop through the slices to extract and save
  for slice_num in range(start_slice, end_slice):
    slice_data = img_data[:, :, slice_num]
    slice_data = slice_data.astype(np.uint8)  # Assuming data is in range 0-255
    img = Image.fromarray(slice_data)
    output_filename = f"{output_folder}/slice_{slice_num}.jpg"
    img.save(output_filename)



# Example usage
nii_folder = "adni_t1"
output_folder_base = nii_folder
extract_middle_percentage_slices(nii_folder,output_folder_base,0.1)