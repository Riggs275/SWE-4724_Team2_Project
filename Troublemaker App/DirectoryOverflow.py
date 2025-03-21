import os
import random
import string

def generate_random_file(filepath, size_kb=1):
    """Generate a file with random content of approximately size_kb kilobytes."""
    try:
        with open(filepath, 'w') as f:
            # Generate random content: approximately size_kb * 1024 characters.
            content = ''.join(random.choices(string.ascii_letters + string.digits, k=size_kb * 1024))
            f.write(content)
    except Exception as e:
        print(f"Error writing file {filepath}: {e}")

def simulate_directory_overflow(directory, num_files=1000, size_kb=1):
    """Simulate directory overflow by creating many files in the given directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory {directory} already exists.")

    created_files = 0
    for i in range(num_files):
        filename = os.path.join(directory, f"overflow_file_{i}.txt")
        try:
            generate_random_file(filename, size_kb)
            created_files += 1
            print(f"Created file {filename}")
        except Exception as e:
            print(f"Exception occurred after creating {created_files} files: {e}")
            break

    print(f"Simulation complete: {created_files} files created in {directory}.")

if __name__ == "__main__":
    target_directory = "./overflow_test_dir"  # Target directory for file creation
    num_files = 1000  # Adjust the number of files to simulate overflow
    file_size_kb = 1  # Size of each file in kilobytes

    simulate_directory_overflow(target_directory, num_files, file_size_kb)
