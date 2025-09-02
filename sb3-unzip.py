import sys
import os
import zipfile
import shutil

def unpack_sb3(sb3_path, output_dir):
    """
    Unpacks a .sb3 Scratch project file into a specified directory.
    If the directory exists, it will be cleared first.
    """
    # 1. Validate that the input file exists
    if not os.path.exists(sb3_path):
        print(f"Error: The file '{sb3_path}' was not found.")
        return False

    # 2. Handle the output directory
    if os.path.exists(output_dir):
        print(f"Output directory '{output_dir}' already exists. Clearing it for a fresh unpack.")
        try:
            shutil.rmtree(output_dir)
        except OSError as e:
            print(f"Error: Could not clear the output directory. {e}")
            return False
    
    try:
        os.makedirs(output_dir)
    except OSError as e:
        print(f"Error: Could not create the output directory. {e}")
        return False

    # 3. Unzip the .sb3 file
    print(f"Unpacking '{sb3_path}' into '{output_dir}'...")
    try:
        with zipfile.ZipFile(sb3_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print("Unpacking complete!")
        print("You can now commit the contents of the 'src' folder to Git.")
        return True
    except zipfile.BadZipFile:
        print(f"Error: '{sb3_path}' is not a valid .sb3 file or is corrupted.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during extraction: {e}")
        return False

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("--- Scratch Project Unpacker ---")
        print("Usage: python unpacker.py <path_to_your_project.sb3> <output_source_folder>")
        print('Example: python unpacker.py "Silent Void.sb3" "src"')
        sys.exit(1)

    # Get the file paths from the command line arguments
    project_file = sys.argv[1]
    source_folder = sys.argv[2]
    
    unpack_sb3(project_file, source_folder)
