reference_folder="synthrad_data/stripped_synthrad/middle_slices/registered_1BA001_skullstripped"

results_folder="synthrad_data/stripped_synthrad/middle_slices/registered_1BA012_skullstripped"

#Checks reference folder against results folder to generate Frechet Inception Distance (FID) score.
python -m pytorch_fid $reference_folder $results_folder