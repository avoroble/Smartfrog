import os
import tarfile
import time

def ensure_tmp_folder():
    """Ensure that the 'tmp' folder exists."""
    if not os.path.exists("tmp"):
        os.mkdir("tmp")

def count_files_in_tmp():
    """Count the number of files in the 'tmp' folder."""
    return len([f for f in os.listdir("tmp") if os.path.isfile(os.path.join("tmp", f))])

def create_archive_and_clean():
    """Create a 'files.tar.gz' archive and clean up the 'tmp' folder."""
    with tarfile.open("files.tar.gz", "w:gz") as archive:
        for filename in os.listdir("tmp"):
            file_path = os.path.join("tmp", filename)
            if os.path.isfile(file_path):
                archive.add(file_path, arcname=filename)
    # Clean the folder
    for filename in os.listdir("tmp"):
        file_path = os.path.join("tmp", filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("files collected")

def main():
    ensure_tmp_folder()
    while True:
        file_count = count_files_in_tmp()
        if file_count == 10:
            create_archive_and_clean()
            break
        time.sleep(1)  # Wait a moment before checking again

if __name__ == "__main__":
    main()