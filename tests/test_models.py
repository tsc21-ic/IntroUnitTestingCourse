import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean
from inflammation.models import daily_min
from inflammation.models import daily_max
from pytest import raises


def test_everything_works():
    npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_array = np.array([[0, 0], [0, 0], [0, 0]])

    npt.assert_array_equal(np.array([0, 0]), daily_mean(test_array))


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers"""

    test_array = np.array([[1, 2], [3, 4], [5, 6]])

    npt.assert_array_equal(np.array([3, 4]), daily_mean(test_array))


def test_daily_min():
    """Test that mean function works for an array of positive integers"""

    test_array = np.array([[1, 2], [3, 4], [5, 6]])

    npt.assert_array_equal(np.array([1, 2]), daily_min(test_array))


def test_daily_max():
    """Test that mean function works for an array of positive integers"""

    test_array = np.array([[1, 2], [3, 4], [5, 6]])

    npt.assert_array_equal(np.array([5, 6]), daily_max(test_array))


def test_daily_mean_string():
    """Test for TypeError when passing strings"""

    with raises(TypeError):
        daily_min([["Cannot", "min"], ["string", "arguments"]])
