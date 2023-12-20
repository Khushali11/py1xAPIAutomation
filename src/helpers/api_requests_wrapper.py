# to make the post,put,patch,delete
# HTTP  methods-generic function
import json

import requests


def get_requests(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_requests(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def put_requests(url: object, auth: object, headers: object, payload: object, in_json: object) -> object:
    put_response = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response


def patch_requests(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


def delete_requests(url, auth, headers, payload, in_json):
    delete_response = requests.delete(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return delete_response



# data=get_requests( "https://restful-booker.herokuapp.com",in_json=False)
# True json response, False normal response
# if xml file convert into json first
