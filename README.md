# log_jitter

# requires: numpy

# Parameters: arr: array_like
#            List or numpy array of points to be jittered.
#            scaler: float optional
#            determines the "severity" of the jitter. 
#            Defaults to 0.05. 
# Returns:    output: ndarray
#            Jittered entries that are not "distorted" when plotted on log scale. Same shape as arr.

def log_jitter(arr, scaler=.05):
    noise = (np.random.randn(len(arr)))*(np.asarray(arr)*scaler)
    return arr + noise
