import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
   # rmse = None # TODO: Implement RMSE Calculation here...
    rmse = np.sqrt(((pred - tar) ** 2).mean())
    return rmse