# log_jitter

requires: numpy
Parameters: arr: array_like
            List or numpy array of points to be jittered.
            scaler: float optional
            determines the "severity" of the jitter. 
            Defaults to 0.05. 
 
Returns:   output: ndarray
           Jittered entries that are not "distorted" when plotted on log scale. Same shape as arr.
