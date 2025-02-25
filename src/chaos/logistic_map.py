"""
Logistic map implementation functions
"""

import numpy as np


def logistic_function(r, x):
    """
    Compute one iteration of the logistic map.

    Parameters
    ----------
    r : float
        Parameter controlling the behavior of the system
    x : float
        Current value (typically between 0 and 1)

    Returns
    -------
    float
        Next value in the sequence
    """
    return r * x * (1 - x)


def iterate_logistic(n, r, x0):
    """
    Iterate the logistic map for n steps.

    Parameters
    ----------
    n : int
        Number of iterations
    r : float
        Parameter controlling the behavior of the system
    x0 : float
        Initial value

    Returns
    -------
    numpy.ndarray
        Array of n values from the iteration
    """
    values = np.zeros(n)
    x = x0

    for i in range(n):
        x = logistic_function(r, x)
        values[i] = x

    return values