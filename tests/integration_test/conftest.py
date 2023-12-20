import requests
from src.helpers.api_requests_wrapper import post_requests, put_requests, delete_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_token, payload_create_booking, payload_update_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code

import pytest


# class TestCreateBooking(object):
@pytest.fixture(scope="class")
def create_token():
    response = post_requests(url=APIConstants.url_create_token(), headers=common_headers_json(), auth=None,
                             payload=payload_create_token(), in_json=False)
    print(response)
    verify_http_status_code(response, 200)
    token = response.json()['token']
    print(token)
    verify_response_key_should_not_be_none(token)
    return token


@pytest.fixture(scope="class")
def create_booking():
    response = post_requests(url=APIConstants.url_create_booking(), auth=None,
                             headers=common_headers_json(),
                             payload=payload_create_booking(), in_json=False)
    print("\n response=", response)
    verify_http_status_code(response, 200)
    bookingid: object = response.json()["bookingid"]
    verify_response_key_should_not_be_none(bookingid)
    print("Bookingid=", bookingid)
    return bookingid
