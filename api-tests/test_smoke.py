import requests

def test_restful_booker_is_up():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    assert response.status_code == 201
