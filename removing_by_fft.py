import pandas as pd
from numpy import pi, sin, cos
import numpy as np


def harmonic_analysis(df, order):
    df.fillna(method='bfill', inplace=True)
    n = df.shape[0]
    df['IND'] = range(1, n + 1)
    df['FITTING'] = df['OBSVALUE'].mean()
    for i in range(1, order):
        ak = sum(df['OBSVALUE'] * cos(2.0 * pi * df['IND'] / n * i)) / n * 2.0
        bk = sum(df['OBSVALUE'] * sin(2.0 * pi * df['IND'] / n * i)) / n * 2.0
        df['FITTING'] = df['FITTING'] \
                        + ak * cos(2.0 * pi * df['IND'] * i / n) \
                        + bk * sin(2.0 * pi * df['IND'] * i / n)
    return df


def my_harmonic(s):
    T = 365
    c = []
    for i in range(T):
        c.append(cos(2 * pi * (i + 1) / T))
    np.array(c)
    s = s * c
    f = s.sum() / T * 2.0
    return f


def rolling_fft(df):
    df['FITTING'] = pd.Series.rolling(df['OBSVALUE'], window=365).apply(my_harmonic, raw=True)
    return df
