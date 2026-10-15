import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def test_ping_returns_201():
    response = requests.get(f"{BASE_URL}/ping", timeout=10)
    assert response.status_code == 201


def test_get_booking_ids_returns_list():
    response = requests.get(f"{BASE_URL}/booking", timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert "bookingid" in body[0]


def test_response_time_under_two_seconds():
    response = requests.get(f"{BASE_URL}/ping", timeout=10)
    assert response.elapsed.total_seconds() < 2


@pytest.fixture
def booking_id():
    response = requests.get(f"{BASE_URL}/booking", timeout=10)
    assert response.status_code == 200
    return response.json()[0]["bookingid"]


def test_get_booking_by_id_has_expected_fields(booking_id):
    response = requests.get(
        f"{BASE_URL}/booking/{booking_id}",
        headers={"Accept": "application/json"},
        timeout=10,
    )
    assert response.status_code == 200
    body = response.json()
    for field in ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]:
        assert field in body, f"Missing field: {field}"


@pytest.mark.parametrize("bad_id", [0, 999999999, -1])
def test_nonexistent_booking_returns_404(bad_id):
    response = requests.get(
        f"{BASE_URL}/booking/{bad_id}",
        headers={"Accept": "application/json"},
        timeout=10,
    )
    assert response.status_code == 404