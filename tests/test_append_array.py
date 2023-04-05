import pytest

from src.append_array import append_array

def test_append_array(array_fixsture):
    assert append_array(array_fixsture, 4) == [1, 2, 3, 4]

def test_append_array_a(array_fixsture):
     assert append_array(array_fixsture, 5) == [1, 2, 3, 5]