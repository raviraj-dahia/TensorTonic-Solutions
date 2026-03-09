import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)

    if x.shape != p.shape:
        raise ValueError(" x and p shape are not equal")

    if np.abs(np.sum(p)-1) > 1e-6:
        raise ValueError("sum of p value must be 1")

    expected = np.sum(x * p)
    return float(expected)
        