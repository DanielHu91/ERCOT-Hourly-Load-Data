import pandas as pd
from plot_utils import plot_data, plot_detrended_data

df = pd.read_csv("combined_data.csv")
df['hour_end'] = pd.to_datetime(df['hour_end'], errors='coerce')
df.dropna(subset = ["hour_end"], inplace=True)
df.set_index('hour_end', inplace=True)
df.sort_index(inplace=True)

plot_data(df, title = "ERCOT Load Data")
plot_detrended_data(df, title = "Detrended ERCOT Load Data")