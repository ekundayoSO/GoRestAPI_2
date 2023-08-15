import json

import requests

from GoRestAPI.POST_Request import user_id
from Utilities import Generic

base_url = "https://gorest.co.in"


# PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    data = {
        "name": "Tech Automation Labs",
        "email": Generic.GenericPage.generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_string_put = json.dumps(json_data, indent=4)
    print("json PUT response body:", json_string_put)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Tech Automation Labs"
    assert json_data["gender"] == "male"
    print("PUT user is done")


put_request(user_id)
