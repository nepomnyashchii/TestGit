import math_func
import pytest

def test_add():
    """Test first function"""
    assert math_func.add(7,3) == 10
    """assert function providing desired result for function add in math function"""
    # assert math_func.add(7,3)==9 for testing errors
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    """Test second function"""
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10
    assert math_func.product(7) == 14


"""command in the bash: pytest test_math_funct.py"""



