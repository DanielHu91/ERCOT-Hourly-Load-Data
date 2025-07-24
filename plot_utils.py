import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "."

excel_files = sorted([f for f in os.listdir(file_path) if f.endswith('.xls') or f.endswith('.xlsx')],)

df_list = []

for file in excel_files:
    try:
        df = pd.read_excel(file)

        df.columns = df.columns.str.strip()
        df.rename(columns={df.columns[0]: 'hour_end'}, inplace=True)
        df['hour_end'] = pd.to_datetime(df['hour_end'], errors='coerce')

        if '2015' in file or '2016' in file:
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
        
        df_list.append(df)
        print(f"File {file} - Cleaned columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"Error processing file {file}: {e}")


combined_df = pd.concat(df_list, ignore_index=True)
combined_df.set_index('hour_end', inplace=True)

combined_df.columns = ['coast', 'east', 'far west', 'north', 'north central', 'south', 'south central', 'west', 'ercot']

plt.figure(figsize = (16,8))
for column in combined_df.columns:
    plt.plot(combined_df.index, combined_df[column], label = column)

plt.xlabel('Date')
plt.ylabel('Load')
plt.title('Load vs Date')
plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()