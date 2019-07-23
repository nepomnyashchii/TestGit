import math_func

def test_add():
    """Test first function"""
    # assert math_func.add(7,3)==10
    assert math_func.add(7)==9
    assert math_func.add(5) == 7

def test_product():
    """Test second function"""
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10
    assert math_func.product(7) == 14

"""command: pytest test_math_funct_py"""
"""more detailed command: pytest test_math_func.py"""

