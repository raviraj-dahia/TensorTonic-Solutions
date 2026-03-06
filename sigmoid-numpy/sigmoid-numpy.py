import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x_array = np.array(x)
    s = 1/(1+np.exp(-x_array))
    return s
sigmoid([0,2,-2])    
    