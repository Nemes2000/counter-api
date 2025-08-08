from unittest.mock import patch
from http import HTTPStatus


@patch("services.counter_service.CounterService.get_counter", return_value=42)
def test_get_counter_success(mock_get, client):
    response = client.get("/api/v1/counter")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"value": 42}


@patch(
    "services.counter_service.CounterService.get_counter", side_effect=Exception("fail")
)
def test_get_counter_failure(mock_get, client):
    response = client.get("/api/v1/counter")
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert "Failed to get counter value." in response.json["msg"]


@patch("services.counter_service.CounterService.update_counter")
def test_post_counter_success(mock_update, client):
    response = client.post("/api/v1/counter", json={"value": 15})
    assert response.status_code == HTTPStatus.OK


@patch("services.counter_service.CounterService.update_counter")
def test_post_counter_high_number(mock_update, client):
    response = client.post("/api/v1/counter", json={"value": 10000000000})
    assert response.status_code == HTTPStatus.OK


def test_post_counter_negative(client):
    response = client.post("/api/v1/counter", json={"value": -1})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "Value must be a positive number" in response.json["msg"]


@patch(
    "services.counter_service.CounterService.update_counter",
    side_effect=Exception("fail"),
)
def test_post_counter_internal_error(mock_update, client):
    response = client.post("/api/v1/counter", json={"value": 5})
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert "Failed to update counter." in response.json["msg"]


@patch("services.counter_service.CounterService.clear_counter")
def test_delete_counter_success(mock_clear, client):
    response = client.delete("/api/v1/counter")
    assert response.status_code == HTTPStatus.NO_CONTENT


@patch(
    "services.counter_service.CounterService.clear_counter",
    side_effect=Exception("fail"),
)
def test_delete_counter_error(mock_clear, client):
    response = client.delete("/api/v1/counter")
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert "Failed to clear counter value." in response.json["msg"]
