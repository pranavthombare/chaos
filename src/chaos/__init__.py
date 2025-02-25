"""
ChaosMaps - A package for exploring chaos theory through the logistic map
"""

__version__ = '0.1.0'

from .logistic_map import logistic_function, iterate_logistic
from .visualization import plot_time_series, plot_bifurcation_map
from .cli import main

__all__ = [
    'logistic_function',
    'iterate_logistic',
    'plot_time_series',
    'plot_bifurcation_map',
    'main',
]