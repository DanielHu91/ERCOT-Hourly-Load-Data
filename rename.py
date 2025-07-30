# This module renames the Excel files to just the year of the data.
# It is used to ensure that the files are named consistently for further processing.

import os

def rename_files(folder_path, dry_run = True):
    for filename in os.listdir(folder_path):
        if not (filename.endswith('.xls') or filename.endswith('.xlsx')):
            continue

        ext = filename[-5:] if filename.endswith('xlsx') else filename[-4:]
        year = filename[:4]
        new_name = year + ext

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)    

        if filename != new_name:
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(old_path, new_path)
