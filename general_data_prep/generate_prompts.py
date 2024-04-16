import os
import re

def create_text_prompts(root_folder):
  #Iterates through all subfolders of the target folder and finds jpg files, extracting the age and slice number using a regular expression
  for path, subdirs, files in os.walk(root_folder):
    for filename in files:
      if filename.endswith(".jpg"):
        match = re.search(r"_slice_(\d+)", filename)
        if match:
          slice_number = int(match.group(1))
          age_pattern = r"\d+" 
          age_match = re.search(age_pattern, filename)
          if age_match:
            age = int(age_match.group())

            #Uses the extracted slice number and age to generate a prompt in the format seen below, and writes it to a text file matching the filename of each jpg
            prompt = f"Slice {slice_number} of a {age} year old brain."
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_file_path = os.path.join(path, txt_filename)
            with open(txt_file_path, "w") as f:
              f.write(prompt)
            print(f"Created text prompt for {filename} as {txt_file_path}")
          else:
            print(f"Could not find age in filename: {filename}")
        else:
          print(f"Could not find slice number in filename: {filename}")

create_text_prompts("adni_t1")