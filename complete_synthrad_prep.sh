#!/bin/bash

python synthrad_data_prep/synthrad_prep_for_strip.py

source general_data_prep/skull_strip_folder.sh

python general_data_prep/skullstrip_extract.py

python general_data_prep/normalise_position.py

python general_data_prep/deconstruct_nii.py

echo "Data ready for compilation."