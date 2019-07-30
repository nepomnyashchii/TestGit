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

"""command in the bash: pytest -v -m number: data with mark number:
only will run bash with mark number"""
"""command in the bash: pytest -v -x:
stop program right away when there is a failure"""

"""command in the bash: pytest -v -x --tb=no:
 number: stop program right away but without any comments about error"""

"""command in the bash: pytest -v --maxfail=2 :
 stop the program when there will be more than 1 failure"""


