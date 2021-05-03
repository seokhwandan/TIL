import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# 시계열 데이터 시각화 함수
plt.style.use('default')
plt.rcParams['figure.figsize'] = (6, 3)
plt.rcParams['font.size'] = 12

def plot_series(time, series, format="-", start=0, end=None, label=None):
    plt.plot(time[start:end], series[start:end], format, label=label)
    plt.xlabel("Time")
    plt.ylabel("Value")
    if label:
        plt.legend(fontsize=14)
    plt.grid(True)

# 경향성을 갖는 시계열 데이터
def trend(time, slope=0):
    return slope * time

time = np.arange(4 * 365 + 1)
# 4 * 365 + 1의 시간 동안 시간에 따라 0.1의 기울기를 갖는 그래프
series = trend(time, slope=0.1)

plot_series(time, series)
plt.show()

# 계절성을 갖는 시계열 데이터
def seasonal_pattern(season_time):
    # season_time < 0.6 인 경우 np.cos(season_time * 2 * np.pi) 값을, 그렇지 않은 경우 1 / np.exp(3 * season_time)
    return np.where(season_time < 0.6, np.cos(season_time * 2 * np.pi), 1 / np.exp(3 * season_time))

def seasonality(time, period, amplitude=1, phase=0):
    # 주어진 주기 period에 대해 특정 값을 반복하는 시계열 데이터 반환
    season_time = ((time + phase) % period) / period
    return amplitude * seasonal_pattern(season_time)

amplitude = 40
series = seasonality(time, period=365, amplitude=amplitude)

plot_series(time, series)
plt.show()

# 경향성과 계절성을 모두 갖는 시계열 데이터
baseline = 10
slope = 0.05
series = baseline + trend(time, slope) + seasonality(time, period=365, amplitude=amplitude)

plot_series(time, series)
plt.show()

# 노이즈를 갖는 시계열 데이터
def white_noise(time, noise_level=1, seed=None):
    rnd = np.random.RandomState(seed)
    return rnd.rand(len(time)) * noise_level

noise_level = 5
noise = white_noise(time, noise_level, seed=42)

plot_series(time, noise)
plt.show()

# 경향성, 계절성, 노이즈를 모두 갖는 시계열 데이터
baseline = 10
slope = 0.05
noise_level = 5
series = baseline + trend(time, slope) + seasonality(time, period=365, amplitude=amplitude) + white_noise(time, noise_level, seed=42)

plot_series(time, series)
plt.show()

# 자기상관성을 갖는 시게열 데이터
split_time = 1000
time_train, x_train = time[:split_time], series[:split_time]
time_valid, x_valid = time[split_time:], series[split_time:]

def autocorrelation(time, amplitude, seed=None):
    rnd = np.random.RandomState(seed)
    pi = 0.8
    ar =  rnd.randn(len(time) + 1) # 정규분포를 갖는 임의의 데이터
    for step in range(1, len(time) + 1):
        ar[step] += pi * ar[step - 1]       ## 이전의 값의 0.8배를 더하기
    return ar[1:] * amplitude

series = autocorrelation(time, 10, seed=42)
plot_series(time[:200], series[:200])
plt.show()

# 자기상관성과 경향성을 갖는 시계열 데이터
series = autocorrelation(time, 10, seed=42) + trend(time, 2)
plot_series(time[:200], series[:200])
plt.show()

# 자기상관성, 경향성, 계절성을 갖는 시계열 데이터
series = autocorrelation(time, 10, seed=42) + seasonality(time, period=50, amplitude=150) + trend(time, 2)
plot_series(time[:200], series[:200])
plt.show()

# 2/3 지점 이후로 크기(amplitude), 주기(period), 경향성(slope)이 모두 달라진 특성을 갖는 시계열 데이터
# 전체구간 노이즈
series = autocorrelation(time, 10, seed=42) + seasonality(time, period=50, amplitude=150) + trend(time, 2)
series2 = autocorrelation(time, 5, seed=42) + seasonality(time, period=50, amplitude=2) + trend(time, -1) + 550
series[200:] = series2[200:]        # 자기상관 amp 10->5, 계절성 amp 150->2, 경향성 slope 2->-1 + 550
series += white_noise(time, 30)
plot_series(time[:300], series[:300])
plt.show()