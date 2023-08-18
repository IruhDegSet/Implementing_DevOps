from math_ops import *

def test_add():
    assert 2 == add(1, 1)

def test_mult():
    assert 1 == mult(1, 1)

def test_subs():
    assert 0 == subs(1, 1)

def test_div():
    assert 1 == div(1,1)
    assert 'division by zero' == div(1,0)
