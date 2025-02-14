import pytest
import allure

@allure.title("Verify that create booking,with valida data is working")
@allure.description("This Testcase check for positive create booking")
@pytest.mark.positive
def test_create_booking_positive():
    print("This is a PyTest positive Test Case")
    assert 1-1 == 2

@allure.title("Verify that create booking,with invalid data is working")
@allure.description("This Testcase check for negative create booking")
@pytest.mark.negative
def test_create_booking_negative1():
    print("This is PyTest negative Case")
    assert 1 + 1 == 2

@allure.title("Verify that create booking,with invalid data is working")
@allure.description("This Testcase check for negative create booking")
@pytest.mark.negative
def test_create_booking_negative2():
    print("This is PyTest negative Case")
    assert 1 + 1 == 2