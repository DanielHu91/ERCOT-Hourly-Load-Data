# This module detrends the data in a DataFrame by using SciyPy detrending methods.

import pandas as pd
from scipy.signal import detrend
import numpy as np

def detrend_data(df, window = 24 * 30):
    detrend_df = pd.DataFrame(index=df.index)

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            trend = df[column].rolling(window=window, min_periods = 1, center=True).mean()
            detrend_df[column] = df[column] - trend

    return detrend_df

