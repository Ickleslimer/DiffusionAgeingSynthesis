import os
from nilearn import plotting
import subprocess

os.environ['FSLOUTPUTTYPE'] = 'NIFTI'

# Specify the path to the input folder containing MRI images
input_folder = r'C:\Users\mrdyl\Desktop\Synthrad_MRI_NII'

# Specify the path to the output folder for the skull-stripped images
output_folder = r'C:\Users\mrdyl\Desktop\Stripped_Synthrad_MRI_NII'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all .nii files in the input folder
input_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.nii')]

# Iterate over each input file and perform skull-stripping
for input_file in input_files:
  # Assuming FSL bin directory is at \\wsl.localhost\Ubuntu\home\ickleslimer\fsl\bin
    command = ['\\wsl.localhost\\Ubuntu\\home\\ickleslimer\\fsl\\bin\\bet', 
              '-i', input_folder, '-o', output_folder]

  # Use the subprocess module to call the external command (bet)
    subprocess.run(command)
    
    # Set input and output file paths for skull-stripped image
    output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.nii', '_skullstripped.nii.gz'))

    # Load the original and skull-stripped images using Nilearn for visualization
    original_img = input_file
    skull_stripped_img = output_file

    plotting.plot_roi(skull_stripped_img, bg_img=original_img, title='Skull-stripped Image')