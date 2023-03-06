import numpy as np

def monte(fun, low, high, sample_size=100, repeat=10):
    int_len = np.abs(high - low)
    stat = []

    for _ in range(repeat):
        x = np.random.uniform(low=low, high=high, size=sample_size)
        fun_x = fun(x)
        int_val = int_len * np.mean(fun_x)
        stat.append(int_val)

    return np.mean(stat), np.std(stat)


## 주어진 함수
def f_x(x):
    return np.exp(-x**2)


print(monte(f_x, low=-1, high=1, sample_size=1000, repeat=100))
