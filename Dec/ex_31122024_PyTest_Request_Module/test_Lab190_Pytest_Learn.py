import pytest
import allure
import requests

@allure.title("TC# - Verify that 2-2 == 0")
@allure.description("This is the Basic Math Test")
@pytest.mark.smoke
def test_basic_math():
    assert  2-2 == 0

@allure.title("TC# - Verify that 3-3 == 0")
@allure.description("This is the Basic Math Test")
@pytest.mark.regression
def test_basic_sub1():
    assert  3-3 == 0


@allure.title("TC# - Verify that 1-1 == 0")
@allure.description("This is the Basic Math Test")
@pytest.mark.smoke
def test_basic_sub2():
    assert  1-1 == 0

@pytest.mark.skip(reason="Not Working, Skip It")
def test_basic_sub3():
    assert  0-0 != 0