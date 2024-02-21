import os
from nilearn import image

# Define the path to the folder containing the .nii files
input_folder = "path/to/your/input_folder"

# Loop through each .nii file in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".nii"):
        input_path = os.path.join(input_folder, filename)

        # Extract the base filename without extension
        base_filename = os.path.splitext(filename)[0]

        # Define output paths for the brain mask and brain image
        output_mask_path = os.path.join(input_folder, base_filename + "_brain_mask.nii")
        output_image_path = os.path.join(input_folder, base_filename + "_brain_image.nii")

        # Load the image
        input_img = image.load_img(input_path)

        # Perform BET
        brain_mask, brain_img = image.bet(input_img, return_mask=True)

        # Save the extracted brain mask and brain image
        image.save_img(brain_mask, output_mask_path)
        image.save_img(brain_img, output_image_path)

        print(f"BET completed for {filename}! Results saved at: {output_mask_path}, {output_image_path}")

print("Finished processing all .nii files in the folder!")
