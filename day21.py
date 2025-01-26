# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:17:08 2025

@author: Triddles lamar
"""

import os
import shutil

def organize_files(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension[1:]  # Remove the dot from the extension

        # Create a folder for the extension if it doesn't exist
        extension_folder = os.path.join(folder_path, f"{file_extension.capitalize()}Files")
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        # Move the file to the corresponding folder
        shutil.move(file_path, os.path.join(extension_folder, filename))

if __name__ == "__main__":
    # Specify the folder to organize
    folder_to_organize = r"C:\Users\Triddles Lamar\3D Objects"
    organize_files(folder_to_organize)
    print("Files organized successfully!")