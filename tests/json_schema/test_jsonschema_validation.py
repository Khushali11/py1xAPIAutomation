import requests
from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest
import json


class TestCreateBooking(object):
    def load_schema(self,schema_file):
        with open(schema_file,"r")as file:
            return json.load(file)
    # positive test case
    @pytest.mark.positive
    def test_create_booking_jsonschema(self):
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
        response_json = response.json()
        print(response_json)
        schema = self.load_schema('schema.json')
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.massage)
