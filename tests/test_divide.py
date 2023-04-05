import pytest

from src.divide import divide

def test_divide():
    assert divide(10, 5) == 2
    assert divide(6.6, 2) == 3.1
    assert divide(10, 5) == 2

def test_divide_division_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)