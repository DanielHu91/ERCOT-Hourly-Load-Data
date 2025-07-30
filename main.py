# This script processes multiple Excel data containing load data. It renames the files to just the year,
# renames columns, combines them into a single DataFrame, and saves it as a CSV
# If the combined CSV already exists, it skips the processing.

import pandas as pd
import glob
import os

from rename import rename_files

combined_file = "combined_data.csv"

if __name__ == "__main__":

    if os.path.exists(combined_file):
        print(f"Combined data '{combined_file}' already exists. Skipping Excel file processing.")
    else:
        folder_path = '.'

        excel_files = glob.glob(os.path.join(folder_path, "*.xls")) + \
            glob.glob(os.path.join(folder_path, "*.xlsx"))
    
        excel_files = sorted(excel_files, key = lambda f: int(os.path.basename(f)[:4]))

        folder = '.'
        rename_files(folder)

        print(f"Found {len(excel_files)} Excel files.\n")

        dataframes = []

        for data in excel_files:
            print(f"Reading {data}...")

            engine = 'openpyxl' if data.endswith('.xlsx') else None
            df = pd.read_excel(data, engine = engine)
            df.columns = df.columns.str.strip()

            original_col = df.columns[0]
            df.rename(columns={original_col: 'hour_end'}, inplace=True)
            df['hour_end'] = df['hour_end'].astype(str).str.replace("24:00", "00:00")

            df['hour_end'] = pd.to_datetime(df['hour_end'], errors='coerce')
            df['hour_end'] = df['hour_end'].dt.round('h')
            if df['hour_end'].isna().any():
                print(f"Warning: Some 'hour_end' values in {data} could not be converted to datetime.")
                df = df.dropna(subset=['hour_end'])

            cols = ['hour_end'] + [col for col in df.columns if col != 'hour_end']
            df = df[cols]
        
            if '2015' in data or '2016' in data:
                df.rename(columns={
                'FAR_WEST': 'fwest',
                'NORTH_C': 'ncent',
                'SOUTH_C': 'scent',
                'SOUTHERN': 'south',
                'COAST': 'coast',
                'EAST': 'east',
                'WEST': 'west',
                'ERCOT': 'ercot',
                'NORTH': 'north'
            }, inplace=True)
            else:
                df.rename(columns={
                'COAST': 'coast',
                'EAST': 'east',
                'FWEST': 'fwest',
                'NORTH': 'north',
                'NCENT': 'ncent',
                'SCENT': 'scent',
                'SOUTH': 'south',
                'WEST': 'west',
                'ERCOT': 'ercot'
            }, inplace=True)

            dataframes.append(df)
    
        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df.set_index('hour_end', inplace=True)
        combined_df.columns = ['Coast', 'East', 'Far West', 'North', 'North Central', 'South', 'South Central', 'West', 'ERCOT']

        print()
        print(f"Loaded {len(dataframes)} files.")
        print()

        combined_df.sort_index(inplace=True)
        combined_df.to_csv(combined_file, index = True, index_label='hour_end')
        print("Combined data saved to 'combined_data.csv'.")