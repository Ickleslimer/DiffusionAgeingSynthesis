#!/bin/bash

input_folder="adni_t1/ADNI_T1_57"

if [ -z "$input_folder" ]; then
  echo "Error: Please provide the path to the folder containing .nii files as an argument."
  exit 1
fi

#Creates the output folder if it does not exist
if [ ! -d "$output_folder" ]; then
  mkdir -p "$output_folder"
  echo "Output folder created: $output_folder"
fi

#Iterates through all .nii files in the input folder and performs BET on them, outputting their file name with "_skullstripped" appended.
for filename in $(find "$input_folder" -type f -name "*.nii"); do
  file_directory=$(dirname "$filename")
  output_filename="$file_directory/$(basename "$filename" .nii)_skullstripped.nii"
  bet "$filename" "$output_filename"
  echo "Skull-stripped: $filename -> $output_filename"
done

echo "Skull-stripping process completed!"
#(Optionally) removes pre-skullstrip nii after completion of skull stripping
#rm -rf "$input_folder"
#echo "Input folder deleted: $input_folder"