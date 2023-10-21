#!/usr/bin/python3

import os
import shutil
from datetime import datetime

# Define the source directory where you want to rename files.
source_dir = os.getcwd()  # You can change this to your desired source directory.

def map_name (path, current_directory):
        # Remove the current working directory (current_directory) from the beginning of the path.
    relative_path = os.path.relpath(path, current_directory)

    # Create a new file name by joining the directory and file name parts.
    directory, filename = os.path.split(relative_path)
    directory = directory.replace("/", "-").lower()
    # print(directory, filename)
    # Convert the filename to lowercase and replace spaces with hyphens.
    new_filename =  directory + "-" + filename.lower()
    new_filename =  new_filename.replace(" ", "")
    
    #print(new_filename)
    
    return new_filename


# Function to rename a file using its creation date.
def rename_file_by_creation_date(file_path):
    try:
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.utcfromtimestamp(creation_time).strftime('%Y-%m-%d')
        # file_name = os.path.basename(file_path)
        file_name = map_name(file_path, source_dir)
        new_file_name = f"{creation_date}-{file_name}"
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        print(file_path, new_file_path)
        os.rename(file_path, new_file_path)
        return new_file_path
    except Exception as e:
        print(f"Error renaming {file_path}: {e}")
        return None

# Recursively traverse the source directory.
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = rename_file_by_creation_date(file_path)
        #if new_file_path:
        #    print(f"Renamed: {file_path} -> {new_file_path}")

print("File renaming completed.")
