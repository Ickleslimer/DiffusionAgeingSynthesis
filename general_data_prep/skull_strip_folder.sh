#!/bin/bash

# Define the folder containing your .nii files
input_folder="adni_t1"

# Check if the input folder is provided as an argument
if [ -z "$input_folder" ]; then
  echo "Error: Please provide the path to the folder containing .nii files as an argument."
  exit 1
fi

# Create the output folder if it doesn't exist
if [ ! -d "$output_folder" ]; then
  mkdir -p "$output_folder"
  echo "Output folder created: $output_folder"
fi

# Loop through each file in the folder and its subdirectories recursively
for filename in $(find "$input_folder" -type f -name "*.nii"); do
  echo "filename = $filename"
  # Extract the directory path from the filename
  file_directory=$(dirname "$filename")

  # Construct the output filename with _skullstripped suffix within the original directory
  output_filename="$file_directory/$(basename "$filename" .nii)_skullstripped.nii"

  # Run bet on the current file
  bet "$filename" "$output_filename"

  # Print a message for each processed file (optional)
  echo "Skull-stripped: $filename -> $output_filename"
done

echo "Skull-stripping process completed!"
#rm -rf "$input_folder"
#echo "Input folder deleted: $input_folder"