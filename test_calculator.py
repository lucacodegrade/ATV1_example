import pytest
import calculator

def test_add():
    assert calculator.add(3, 2) ==  5
    assert calculator.add(1, -1) ==  0
    assert calculator.add(-1, -1) ==  -2

def test_subtract():
    assert calculator.subtract(5, 2) ==  3
    assert calculator.subtract(1, -1) ==  2
    assert calculator.subtract(-1, -1) ==  0

def test_multiply():
    assert calculator.multiply(3, 2) ==  6
    assert calculator.multiply(1, -1) ==  -1
    assert calculator.multiply(-1, -1) ==  1

def test_divide():
    assert calculator.divide(10, 2) ==  5
    assert calculator.divide(1, -1) ==  -1
    assert calculator.divide(-1, -1) ==  1
    assert calculator.divide(5, 2) ==  2.5
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
