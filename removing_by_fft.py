import pandas as pd
from numpy import pi, sin, cos, ceil
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
    df.fillna(method='bfill', inplace=True)
    df['FITTING'] = pd.Series.rolling(df['OBSVALUE'], window=365, center=False).apply(my_harmonic, raw=True)
    df['FITTING'] = df['FITTING'] + df['OBSVALUE'].mean()
    return df


df = pd.read_hdf('mls-res.h5', 'table')
ns = df[df['ITEMID'] == '3211'].resample('D').median()
ew = df[df['ITEMID'] == '3212'].resample('D').median()

# 频率1 / t = k / N / T
# T为采样周期，这里T=1天
# N为采样长度，N = df.shape[0]
# k为阶数，t = 365
t = 365
N = ns.shape[0]
k = N / t
ew = harmonic_analysis(ew, int(ceil(k)))
ew.drop('IND', axis=1, inplace=True)
ew.plot()
