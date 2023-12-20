from src.constants.api_constants import BASE_URL, APIConstants, base_url


def test_crud():
    print(BASE_URL)

    url_direct_func = base_url()
    print(url_direct_func)

    url_class = APIConstants.base_url()
    # if not write static method then write self in api_constants file and call objects and then function.
    #url_class = APIConstants().base_url()
    print(url_class)



