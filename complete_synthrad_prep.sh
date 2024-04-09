#!/bin/bash

python prep_for_strip.py

source general_data_prep/skull_strip_folder.sh

python general_data_prep/skullstrip_extract.py

echo "Data ready for compilation."