import numpy as np

def log_jitter(arr, scaler=.05):
    noise = (np.random.randn(len(arr)))*(np.asarray(arr)*scaler)
    output = arr + noise
    return output
