import os
import nrrd

def convert_nhdr_to_nrrd(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True) 

    for filename in os.listdir(input_folder):
        if filename.endswith(".nhdr"):  
            file_path = os.path.join(input_folder, filename)
            output_filename = os.path.join(output_folder, filename.replace(".nhdr", ".nrrd"))

            try:
                # Read NHDR file
                nrrd_data, nrrd_header = nrrd.read(file_path)

                # Write to NRRD format
                nrrd_header['custom_field_map'] = nrrd_header.get('custom_field_map', {})  # Ensure custom fields
                nrrd.write(output_filename, nrrd_data, header=nrrd_header, detached_header=False)

                print(f"Converted: {file_path} → {output_filename}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Example usage
input_folder = r"C:\WAIKnotCT\InstancePhysicsInformed\tree8"   # Replace with actual path 
output_folder = r"C:\WAIKnotCT\InstancePhysicsInformed\tree8nrrd" # Replace with actual path
os.makedirs(output_folder, exist_ok=True)

convert_nhdr_to_nrrd(input_folder, output_folder)