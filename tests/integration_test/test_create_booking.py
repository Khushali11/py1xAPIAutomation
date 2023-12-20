import requests
from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code

import pytest
import json


class TestCreateBooking(object):
    # positive test case
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        # dynamic payload,change payload
        # payload=payload_create_booking()
        # print(payload)
        # payload.update({"key":"value","key":"value",.....})
        # payload["firstname"]="Pramod"
        # print(payload)

        response: Response | Any = post_requests(url=APIConstants.url_create_booking(), auth=None,
                                                 headers=common_headers_json(),
                                                 payload=payload_create_booking(), in_json=False)
        print("\n response=", response)
        verify_http_status_code(response, 200)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        print("Bookingid=", response.json()["bookingid"])

    # pytest tests/integration_test/test_create_booking.py -s -v --alluredir=./reports
    # -s shows print message ,-v shows logs file
    # allure serve reports
    # negative test case without payload
    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response: Response | Any = post_requests(url=APIConstants.url_create_booking(), auth=None,
                                                 headers=common_headers_json(),
                                                 payload={}, in_json=False)
        print("\n response=", response)
        verify_http_status_code(response, 500)

    # negative test case with payload=None
    @pytest.mark.negative
    def test_create_booking_tc3(self):
        response: Response | Any = post_requests(url=APIConstants.url_create_booking(), auth=None,
                                                 headers=common_headers_json(),
                                                 payload=None, in_json=False)
        print("\n response=", response)
        verify_http_status_code(response, 400)
