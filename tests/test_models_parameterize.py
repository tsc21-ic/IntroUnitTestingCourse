from inflammation.models import daily_mean
from inflammation.models import daily_min
from inflammation.models import daily_max

import numpy as np
import numpy.testing as npt
import pytest


test1 = [[0, 0], [0, 0], [0, 0]]
expected1 = [0, 0]

test2 = [[1, 2], [3, 4], [5, 6]]
expected2 = [3, 4]


test3 = [[-1, 2], [1, 4], [3, 6]]
expected3 = [1, 4]


@pytest.mark.parametrize(
    "test, expected", [(test1, expected1), (test2, expected2), (test3, expected3)]
)
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers"""

    npt.assert_array_equal(np.array(expected), daily_mean(np.array(test)))


## Not again



from inflammation.models import daily_mean
from inflammation.models import daily_min
from inflammation.models import daily_max

import numpy as np
import numpy.testing as npt
import pytest


test1 = [[0, 0], [0, 0], [0, 0]]
expected1 = [0, 0]

test2 = [[1, 2], [3, 4], [5, 6]]
expected2 = [3, 4]


test3 = [[-1, 2], [1, 4], [3, 6]]
expected3 = [1, 4]


@pytest.mark.parametrize(
    "test, expected", [(test1, expected1), (test2, expected2), (test3, expected3)]
)
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers"""

    npt.assert_array_equal(np.array(expected), daily_mean(np.array(test)))


## Not again
