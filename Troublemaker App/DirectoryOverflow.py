import os
import random
import string
from Intensity import Intensity

def generate_random_file(filepath, size_kb=1):
    """Generate a file with random content of approximately size_kb kilobytes."""
    try:
        with open(filepath, 'w') as f:
            content = ''.join(random.choices(string.ascii_letters + string.digits, k=size_kb * 1024))
            f.write(content)
    except Exception as e:
        print(f"Error writing file {filepath}: {e}")

def simulate_directory_overflow(directory, intensity=Intensity.Low):
    """Simulate directory overflow by creating many files in the given directory based on intensity."""
    # Set parameters based on intensity level
    if intensity == Intensity.Low:
        num_files = 100
        file_size_kb = 1
    elif intensity == Intensity.Medium:
        num_files = 500
        file_size_kb = 2
    elif intensity == Intensity.High:
        num_files = 1000
        file_size_kb = 5
    else:
        # Default values if unknown intensity is passed
        num_files = 100
        file_size_kb = 1

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory {directory} already exists.")

    created_files = 0
    for i in range(num_files):
        filename = os.path.join(directory, f"overflow_file_{i}.txt")
        try:
            generate_random_file(filename, file_size_kb)
            created_files += 1
            print(f"Created file {filename}")
        except Exception as e:
            print(f"Exception occurred after creating {created_files} files: {e}")
            break

    print(f"Simulation complete: {created_files} files created in {directory}.")

def cleanup_directory(directory):
    """Delete all files in the given directory and remove the directory itself."""
    if os.path.exists(directory):
        # Remove files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
        # Remove the directory after all files have been deleted
        try:
            os.rmdir(directory)
            print(f"Deleted directory {directory}")
        except Exception as e:
            print(f"Error deleting directory {directory}: {e}")
    else:
        print(f"Directory {directory} does not exist. No cleanup necessary.")

if __name__ == "__main__":
    target_directory = "./overflow_test_dir"  # Target directory for file creation
    
    # Set the desired intensity level: Intensity.Low, Intensity.Medium, or Intensity.High
    selected_intensity = Intensity.High
    
    # Generate all files based on the selected intensity.
    simulate_directory_overflow(target_directory, intensity=selected_intensity)
    
    # After all files are created, clean up by deleting them and removing the directory.
    cleanup_directory(target_directory)
