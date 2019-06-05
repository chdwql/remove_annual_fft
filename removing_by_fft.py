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


def my_harmonic(df):
    T = 365
    c = []
    for i in range(T):
        c.append(cos(2 * pi * (i + 1) / T))
    c = pd.DataFrame(c)
    df['FITTING'] = df['OBSVALUE'] * c

    return df


def rolling_fft(df):
    df.rolling(window=365, on='OBSVALUE').apply(my_harmonic)


a = []
for i in range(365 * 10):
    a.append(10 * sin(2 * pi * i / 365) + 3*np.random.rand())

df_a = pd.DataFrame(a)
df_a.columns = ['OBSVALUE']
df_a.index = pd.date_range(start='2000-01-01', periods=10 * 365)
rolling_fft(df_a)
