import pytest
from ..calc import *

def test_syserror_1():
    with pytest.raises(SystemExit):
        syserror()

def test_multiply_1():
    assert multiply(6,7) == 6*7

def test_flex_add_1():
    assert flex_add(4, "5") == "45"

def test_add_1():
    assert add(3, 4) == 7

def test_inc_1():
    assert inc(3) == 5
    
class TestSubtract:
    def test_one(self):
        assert subtract(6,7) == -1
        
    def test_two(self):
        assert subtract(9,6) == 3
        
        
class Test_Divide:
    def test_one(self):
        assert divide(6,4) == 6/4
        
    def test_two(self):
        assert divide(6,3) == 2
        
    def test_three(self):
        """Type Error Expected"""
        with pytest.raises(TypeError):
            divide("6",3)