import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, i/(1+np.exp(z)),np.exp(-z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    N,D = X.shape
    w = np.zeros(D)
    b = 0.0

    for _ in range(steps):
        # linear model
        z = X @ w + b

        # prediction using sigmoid
        y_hat = _sigmoid(z)
        
        #  error
        error = y_hat - y

        # update parameters
        dw = (X.T @ error)/N
        db = np.sum(error)/N

        # update parameters
        w = w - lr * dw
        b = b - lr *db

    return w, float(b)    