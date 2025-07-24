import pandas as pd
import glob
import os

from rename import rename_files

if __name__ == "__main__":
    folder_path = '.'

    excel_files = glob.glob(os.path.join(folder_path, "*.xls")) + \
        glob.glob(os.path.join(folder_path, "*.xlsx"))
    
    excel_files = sorted(excel_files, key = lambda f: int(os.path.basename(f)[:4]))

    folder = '.'
    rename_files(folder)

    print(f"Found {len(excel_files)} Excel files.\n")

    dataframes = []

    for file in excel_files:
        print(file)
    
    print()

    for data in excel_files:
        print(f"Reading {data}...")

        engine = 'openpyxl' if data.endswith('.xlsx') else None
        df = pd.read_excel(data, engine = engine)
        print(df.head())
        print()
        dataframes.append(df)

    print(f"Loaded {len(dataframes)} files.")