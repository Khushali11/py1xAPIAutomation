# read the csv or EXCEL files
# create a function create token which can take values from the excel files
# verify the expected result
# read the excel file- openpyxl
# pip install openpyxl

import requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
import pytest
import openpyxl


# read file and put the content into a []

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url=APIConstants.url_create_token(), headers=common_headers_json(), json=payload)
    # assert response.status_code == 200
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel("testdata_ddt.xlsx"))
def test_post_create_token(user_cred: object) -> object:
    # run this function till row we have in excel file
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = make_request_auth(username, password)
    print(response)
    # here write the logic for negative and positive test case
    assert response.status_code == 200
