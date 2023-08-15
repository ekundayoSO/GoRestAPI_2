import json
import os

import requests

from Utilities import Generic

base_url = "https://gorest.co.in"

# POST Request
def post_request():
    url = base_url + "/public/v2/users/"
    print("Get url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    data = {
        "name": "Tech Automation",
        "email": Generic.GenericPage.generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_string_post = json.dumps(json_data, indent=4)
    print("json POST response body:", json_string_post)
    user_id = json_data["id"]
    print("User id ====>", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Tech Automation"
    return user_id


user_id = post_request()
