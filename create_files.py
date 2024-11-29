import os

def create_tmp_folder():
    """Ensure the 'tmp' folder exists, create it if it doesn't."""
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
        print("Created 'tmp' folder")

def create_files_in_tmp():
    """Create 10 text files in the 'tmp' folder."""
    for i in range(1, 11):
        file_path = f"tmp/file_{i}.txt"
        with open(file_path, 'w') as file:
            file.write(f"This is file number {i}")
        print(f"Created: {file_path}")

def main():
    create_tmp_folder()  # Ensure 'tmp' folder exists
    create_files_in_tmp()  # Create 10 files in 'tmp' folder

if __name__ == "__main__":
    main()