# log_jitter

requires: numpy\n
Parameters: arr: array_like\n
            List or numpy array of points to be jittered.\n
            scaler: float optional\n
            determines the "severity" of the jitter. \n
            Defaults to 0.05. \n
 
Returns:   output: ndarray\n
           Jittered entries that are not "distorted" when plotted on log scale. Same shape as arr.\n
