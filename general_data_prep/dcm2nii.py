from dicom2nifti import dicom_series_to_nifti

# Define paths
dcm_directory = "path/to/your/dicom_directory"
output_nifti_path = "path/to/output.nii"

# Convert the entire series
dicom_series_to_nifti(dcm_directory, output_nifti_path)

# Specify other parameters (optional)
dicom_series_to_nifti(dcm_directory, output_nifti_path, reorient=True, scaling=False)
