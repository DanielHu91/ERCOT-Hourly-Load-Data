# This module contains utility functions for plotting data and detrended data.

import pandas as pd
import matplotlib.pyplot as plt
from detrend import detrend_data

def plot_data(df, title = 'Load vs Date'):
    plt.figure(figsize = (16,8))
    # numeric_columns = df.select_dtypes(include='number').columns
    for column in df.columns:
        plt.plot(df.index, df[column], label = column)

    plt.xlabel('Date')
    plt.ylabel('Load')
    plt.title('Load vs Date')
    plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def plot_detrended_data(df, title = 'Detrended Load vs Data', window=24*30):
    detrended_df = detrend_data(df)
    numeric_columns = df.select_dtypes(include='number').columns
    plt.figure(figsize=(16, 8))
    for column in numeric_columns:
        plt.plot(detrended_df.index, detrended_df[column], label=column)

    plt.xlabel('Date')
    plt.ylabel('Detrended Load')
    plt.title('Detrended Load vs Date')
    plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(True)
    plt.show()