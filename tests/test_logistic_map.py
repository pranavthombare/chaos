"""
Tests for the chaosmaps logistic map functionality
"""

import pytest
import numpy as np
from chaosmaps.logistic_map import logistic_function, iterate_logistic


def test_logistic_function():
    """Test the logistic function with known values."""
    assert logistic_function(1.0, 0.5) == 0.5  # r=1, x=0.5 → rx(1-x) = 0.5
    assert logistic_function(2.0, 0.5) == 1.0  # r=2, x=0.5 → rx(1-x) = 1.0
    assert logistic_function(3.0, 0.1) == 0.27  # r=3, x=0.1 → rx(1-x) = 0.27
    assert logistic_function(4.0, 0.2) == 0.64  # r=4, x=0.2 → rx(1-x) = 0.64


def test_iterate_logistic():
    """Test the iteration function."""
    # Test with a stable point (r=3, x=2/3)
    values = iterate_logistic(10, 3.0, 2 / 3)
    assert len(values) == 10
    np.testing.assert_allclose(values, np.ones(10) * 2 / 3, atol=1e-10)

    # Test with r=2, should converge to 0.5
    values = iterate_logistic(20, 2.0, 0.1)
    assert len(values) == 20
    np.testing.assert_allclose(values[-5:], np.ones(5) * 0.5, atol=1e-4)

    # Test with r=0, should go to 0
    values = iterate_logistic(5, 0.0, 0.5)
    assert len(values) == 5
    np.testing.assert_array_equal(values, np.zeros(5))