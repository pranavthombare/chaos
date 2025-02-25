"""
Visualization functions for chaos theory and logistic maps
"""

import numpy as np
import matplotlib.pyplot as plt
from .logistic_map import logistic_function, iterate_logistic


def plot_time_series(n, r, x0, figsize=(10, 6), title=None, save_path=None):
    """
    Plot the time series of the logistic map.

    Parameters
    ----------
    n : int
        Number of iterations
    r : float
        Parameter controlling the behavior of the system
    x0 : float
        Initial value
    figsize : tuple, optional
        Figure size (width, height) in inches
    title : str, optional
        Plot title
    save_path : str, optional
        Path to save the figure

    Returns
    -------
    tuple
        Figure and axes objects
    """
    values = iterate_logistic(n, r, x0)
    x = np.arange(n)

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x, values)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Value')

    if title:
        ax.set_title(title)
    else:
        ax.set_title(f'Logistic Map Time Series (r={r}, x0={x0})')

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig, ax


def plot_bifurcation_map(x0=0.5, r_min=2.5, r_max=4.0, n_points=1000,
                         transient=800, plot_points=200,
                         figsize=(12, 8), title=None, save_path=None,
                         point_size=0.5, color='black'):
    """
    Create a bifurcation diagram for the logistic map.

    Parameters
    ----------
    x0 : float, optional
        Initial value
    r_min : float, optional
        Minimum r value to plot
    r_max : float, optional
        Maximum r value to plot
    n_points : int, optional
        Number of r values to test
    transient : int, optional
        Number of iterations to discard as transient
    plot_points : int, optional
        Number of points to plot for each r value
    figsize : tuple, optional
        Figure size (width, height) in inches
    title : str, optional
        Plot title
    save_path : str, optional
        Path to save the figure
    point_size : float, optional
        Size of plotted points
    color : str, optional
        Color of plotted points

    Returns
    -------
    tuple
        Figure and axes objects
    """
    # Arrays to store values
    r_values = []
    x_values = []

    # Create range of r values to test
    r_range = np.linspace(r_min, r_max, n_points)

    # For each r value, iterate the map and store results
    for r in r_range:
        x = x0

        # Run for transient iterations to reach steady state
        for i in range(transient):
            x = logistic_function(r, x)

        # Record plot_points iterations
        for i in range(plot_points):
            x = logistic_function(r, x)
            r_values.append(r)
            x_values.append(x)

    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(r_values, x_values, s=point_size, color=color)

    ax.set_xlim(r_min, r_max)
    ax.set_ylim(0, 1)
    ax.set_xlabel('r')
    ax.set_ylabel('x')

    if title:
        ax.set_title(title)
    else:
        ax.set_title('Bifurcation Diagram for Logistic Map')

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig, ax