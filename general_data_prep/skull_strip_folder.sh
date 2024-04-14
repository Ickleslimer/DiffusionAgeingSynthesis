#!/bin/bash

# Define the folder containing your .nii files
input_folder="synthrad_data/synthrad_skulls"

# Check if the input folder is provided as an argument
if [ -z "$input_folder" ]; then
  echo "Error: Please provide the path to the folder containing .nii files as an argument."
  exit 1
fi

# Define the output folder on the desktop
output_folder="synthrad_data/stripped_synthrad"

# Create the output folder if it doesn't exist
if [ ! -d "$output_folder" ]; then
  mkdir -p "$output_folder"
  echo "Output folder created: $output_folder"
fi

# Loop through each file in the folder
for filename in $input_folder/*.nii; do
  echo "filename = $filename"
  # Extract the filename without extension
  base_filename=$(basename "$filename" .nii)

  # Define the output filename with _skullstripped suffix
  output_filename="$output_folder/${base_filename}_skullstripped.nii"

  # Run bet on the current file
  bet "$filename" "$output_filename"

  # Print a message for each processed file (optional)
  echo "Skull-stripped: $filename -> $output_filename"
done

echo "Skull-stripping process completed!"
rm -rf "$input_folder"
echo "Input folder deleted: $input_folder"