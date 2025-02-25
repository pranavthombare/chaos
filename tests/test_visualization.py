"""
Tests for the chaosmaps visualization functionality
"""

import pytest
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt
from chaosmaps.visualization import plot_time_series, plot_bifurcation_map


def test_plot_time_series():
    """Test that the time series plotting function returns figure and axes."""
    fig, ax = plot_time_series(n=10, r=2.0, x0=0.5)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    plt.close(fig)


def test_plot_bifurcation_map():
    """Test that the bifurcation map function returns figure and axes."""
    # Use minimal settings for quick test
    fig, ax = plot_bifurcation_map(
        r_min=3.5, r_max=3.6,
        n_points=5,
        transient=5,
        plot_points=5
    )
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    plt.close(fig)


def test_plot_time_series_save(tmp_path):
    """Test that saving works."""
    output_file = tmp_path / "test_output.png"
    fig, ax = plot_time_series(n=10, r=2.0, x0=0.5, save_path=str(output_file))
    assert output_file.exists()
    plt.close(fig)