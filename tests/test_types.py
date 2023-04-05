import pytest

from src.list_types import types_count

@pytest.mark.parametrize("array, type_in_array, expected", [
    ([1, 2, 3], int, 3),
    ([1, "2", "3"], int, 1),
    ([1, "2", "3"], str, 2)
])
def test_types_count(array, type_in_array, expected):
    assert types_count(array, type_in_array) == expected
   # assert types_count([1, "2", "3"], int) == 1
   # assert types_count([1, "2", "3"], str) == 2