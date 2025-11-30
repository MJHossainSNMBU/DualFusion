import os
import nrrd
import numpy as np

def binarise_mask_classes(input_folder: str, output_folder: str) -> None:
    """
    Convert labels 1-100 to 1 and everything else to 0 in every NRRD mask
    found inside *input_folder*. Results are written to *output_folder*,
    preserving the original filenames.
    """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(".nrrd"):
            continue

        in_path  = os.path.join(input_folder, filename)
        out_path = os.path.join(output_folder, filename)

        try:
            data, header = nrrd.read(in_path)

            # Binary remapping: 1-100 ➜ 1, everything else ➜ 0
            binary_data = np.where((data >= 1) & (data <= 100), 1, 0).astype(data.dtype)

            nrrd.write(out_path, binary_data, header)
            print(f"✓ processed {filename}")
        except Exception as exc:
            print(f"✗ error processing {filename}: {exc}")

# ── Example usage ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    input_folder  = r"C:\WAIKnotCT\InstanceSegmentation\crop10\FolderCreate\WetMask"
    output_folder = r"C:\WAIKnotCT\InstanceSegmentation\crop10\FolderCreate\WetMask2Class"
    binarise_mask_classes(input_folder, output_folder)