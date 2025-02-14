import pytest
import allure
import requests

@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This Testcase check Booking 1 and Verify the response")
@pytest.mark.positive
def test_get_request_positive():
    URL_get1 = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url= URL_get1)
    print(response_data.text)
    assert response_data.status_code == 200


@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and Verify the response")
@pytest.mark.negative
def test_get_request_negative():
    URL_get2 = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url= URL_get2)
    print(response_data.text)
    assert response_data.status_code == 404



