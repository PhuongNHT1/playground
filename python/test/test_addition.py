import addition
import pytest

def test_add():
    assert addition.add(5, 5) == 10
    assert addition.add(15, 5) == 10

def test_add_new():
    assert True