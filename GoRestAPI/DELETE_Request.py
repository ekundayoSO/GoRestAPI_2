import requests

from GoRestAPI.POST_Request import user_id
from Utilities import Generic

base_url = "https://gorest.co.in"


# DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("DELETE user is done")


delete_request(user_id)
