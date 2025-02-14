import pytest


def method1():
    print("Hello World")

@pytest.mark.smoke
def test_method2():
    print("This is a PyTest Case")
    assert 1-1 == 2

@pytest.mark.regression
def test_method3():
    print("This is PyTest Case")
    assert 1 + 1 == 2