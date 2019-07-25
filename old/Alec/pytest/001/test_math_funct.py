import math_func
import pytest

@pytest.mark.number
def test_add():
    """Test first function"""
    assert math_func.add(7,3) == 10
    """assert function providing desired result"""
    # assert math_func.add(7,3)==9 for testing errors
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    """Test second function"""
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10
    assert math_func.product(7) == 14

@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == "Hello World"
    assert type(result) is str
    assert "Heldlo" not in result

@pytest.mark.string
def test_product_strings():
    assert math_func.product("Hello ", 3) == 'Hello Hello Hello '
    result = math_func.product("Hello ")
    assert result== 'Hello Hello '
    assert type(result) is str
    assert "Hello" in result

"""command: pytest test_math_funct_py"""
"""more detailed command: pytest test_math_func.py"""
""" we can run command py.test to run the function"""
""" we can test only one function: test_math_funct.py::test_add"""
"""pytest -v -k "add or string" """
"""pytest -v -k "add or string"""
"""pytest -v -k "add and string"""
"""pytest -v -m number""" """data with mark number"""
"""pytest -v -x""" """stop program right away when there is a failure"""


