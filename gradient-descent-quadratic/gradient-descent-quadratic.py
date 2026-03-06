def gradient_descent_quadratic(a, b, c, x, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for _ in range(steps):
        gradient = 2 * a * x + b
        x = x-lr*gradient
    return float(x)    