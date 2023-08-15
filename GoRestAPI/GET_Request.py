import json

import requests

from Utilities import Generic

base_url = "https://gorest.co.in"


# GET Request
def get_request():
    url = base_url + "/public/v2/users/"
    print("Get url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_string_get = json.dumps(json_data, indent=4)
    print("json response body:", json_data)
    print("json GET response body:", json_string_get)  # pretty format version
    print("GET user is done")


# Call Requests
get_request()
