import os
import nibabel as nib
from PIL import Image
import numpy as np

def convert_nii_to_jpg(nii_folder, output_folder_base):
  #Iterates through the subfolders of the target directory and runs the convert_single_nii file on each file with the .nii ending
  for path, subdirs, files in os.walk(nii_folder):
    for filename in files:
        if filename.endswith(".nii"):
          file_name, _ = os.path.splitext(filename)
          output_folder = os.path.join(output_folder_base, file_name)
          os.makedirs(output_folder, exist_ok=True)
      
          nii_file = os.path.join(nii_folder, filename)
      
          try:
            convert_single_nii(nii_file, output_folder)
            #(Optionally) removes the original nii file after deconstruction
            #os.remove(nii_file)
            print(f"Converted {nii_file} to jpgs and deleted the original file.")
          except Exception as e:
            print(f"Error converting {nii_file}: {e}")

def convert_single_nii(nii_file, output_folder):
#Load the nii file using nibabel
  img = nib.load(nii_file)
  img_data = img.get_fdata()

#Convert the nii into an array of jpgs, and iterate through the array, saving each as a jpg file
  for slice_num in range(img_data.shape[2]):
    slice_data = img_data[:, :, slice_num]
    slice_data = slice_data.astype(np.uint8)  
    img = Image.fromarray(slice_data)
    output_filename = f"{output_folder}/slice_{slice_num}.jpg"
    img.save(output_filename)

def extract_middle_percentage_slices(nii_folder, percentage=0.3):
#Iterates through the subfolders of the target directory and runs the convert_single_nii file on each file with the .nii ending
  for path, subdirs, files in os.walk(nii_folder):
    for filename in files:
      if filename.endswith(".nii"):
        file_name, _ = os.path.splitext(filename)
        subdirectory = os.path.join(path, file_name)
        os.makedirs(subdirectory, exist_ok=True)

        nii_file = os.path.join(path, filename)

        try:
          extract_middle_percentage_slices_single(nii_file, subdirectory, percentage)
          print(f"Extracted middle {percentage*100:.0f}% slices from {nii_file} and saved to {subdirectory}")
        except Exception as e:
          print(f"Error processing {nii_file}: {e}")


def extract_middle_percentage_slices_single(nii_file, subdirectory, percentage=0.3):
  #Load the nii file using nibabel, taking the number of slices
  img = nib.load(nii_file)
  img_data = img.get_fdata()
  num_slices = img_data.shape[2]

#Calculate the number of slices to extract and where extraction should begin and end in the array of slices
  num_extract_slices = int(num_slices * percentage) // 2
  start_slice = (num_slices // 2) - num_extract_slices
  end_slice = (num_slices // 2) + num_extract_slices

#Get the filename minus the file extension
  nii_filename = os.path.splitext(os.path.basename(nii_file))[0]

#Convert the nii into an array of jpgs, and iterate through the array, saving each as a jpg file
  for slice_num in range(start_slice, end_slice):
    slice_data = img_data[:, :, slice_num]
    slice_data = slice_data.astype(np.uint8)
    img = Image.fromarray(slice_data)
    output_filename = f"{subdirectory}/{nii_filename}_slice_{slice_num}.jpg"
    img.save(output_filename)

#Define where to put the nii files and where to get them from
nii_folder = "adni_t1"
output_folder_base = nii_folder
extract_middle_percentage_slices(nii_folder,0.1)