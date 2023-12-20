import requests
from src.helpers.api_requests_wrapper import post_requests, put_requests, delete_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json,common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_token, payload_create_booking, payload_update_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
#from tests.integration_test.conftest import create_booking,create_token
import pytest


class TestCreateBooking(object):
       # token / auth  and booking id from the create booking and token call

    def test_update_booking(self,create_token,create_booking):
        print("token------->", create_token)
        print("bookingid-------->", create_booking)
        bookingid=create_booking
        # url= APIConstants.url_patch_put_delete_booking
        # token=
        #put_url = APIConstants.url_create_booking() + "/1"
        #auth = ('admin', 'password123')
        #response = put_requests(url=put_url, auth=auth,
         #                       headers=common_headers_json(),
         #                       payload=payload_update_booking(), in_json=False)
        put_url = APIConstants.url_create_booking() + "/"+str(bookingid)
        response = put_requests(url=put_url, auth=None,
                                headers=common_headers_for_put_delete_patch(),
                                payload=payload_update_booking(), in_json=False)
        print("\n response=", response)
        verify_http_status_code(response, 200)
        print(response.json()["firstname"])
        # updated
        print(response.json())

    # token and booking id from the create booking and token call
    def test_delete_booking(self,create_token,create_booking):
        bookingid=create_booking
        delete_url = APIConstants.url_create_booking() + "/"+str(bookingid)
        #auth = ('admin', 'password123')

        #response = delete_requests(url=delete_url, auth=auth,
        #                           headers=common_headers_json(),
        #                           payload={}, in_json=False
        response = delete_requests(url=delete_url, auth=None,
                                   headers=common_headers_for_put_delete_patch(),
                                   payload={}, in_json=False)
        print("\n response=", response)
        verify_http_status_code(response, 201)

        # updated
        #print(response.json())
