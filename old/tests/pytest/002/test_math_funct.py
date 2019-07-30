import math_func
import pytest

def test_add():
    """Test first function"""
    assert math_func.add(7,3) == 10
    """assert function providing desired result"""
    # assert math_func.add(7,3)==9 for testing errors
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    """Test second function"""
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10
    assert math_func.product(7) == 14

def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == "Hello World"
    assert type(result) is str
    assert "Heldlo" not in result

def test_product_strings():
    assert math_func.product("Hello ", 3) == 'Hello Hello Hello '
    result = math_func.product("Hello ")
    assert result== 'Hello Hello '
    assert type(result) is str
    assert "Hello" in result


""" command in the bash: test_math_funct.py::test_add:
only check whether the first function test_add passed or failed"""
""" command in the bash: pytest -v -k "add":
only check whether the fumction with keyword add pass: letter k added"""
"""command in the bash: pytest -v -k "add or string" :
check for both add or string"""
"""command in the test: pytest -v -k "add and test_add_string":
check for add and string"""



