from unittest.mock import MagicMock, patch
from http import HTTPStatus

from flask.testing import FlaskClient


@patch("services.counter_service.CounterService.get_counter", return_value=42)
def test_get_counter_success(mock_get: MagicMock, client: FlaskClient) -> None:
    response = client.get("/api/v1/counter")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"value": 42}


@patch(
    "services.counter_service.CounterService.get_counter", side_effect=Exception("fail")
)
def test_get_counter_failure(mock_get: MagicMock, client: FlaskClient) -> None:
    response = client.get("/api/v1/counter")
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json and "Failed to get counter value." in response.json["msg"]


@patch("services.counter_service.CounterService.update_counter")
def test_post_counter_success(mock_update: MagicMock, client: FlaskClient) -> None:
    response = client.post("/api/v1/counter", json={"value": 15})
    assert response.status_code == HTTPStatus.OK


@patch("services.counter_service.CounterService.update_counter")
def test_post_counter_high_number(mock_update: MagicMock, client: FlaskClient) -> None:
    response = client.post("/api/v1/counter", json={"value": 10000000000})
    assert response.status_code == HTTPStatus.OK


def test_post_counter_negative(client: FlaskClient) -> None:
    response = client.post("/api/v1/counter", json={"value": -1})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json and "Value must be a positive number" in response.json["msg"]


@patch(
    "services.counter_service.CounterService.update_counter",
    side_effect=Exception("fail"),
)
def test_post_counter_internal_error(mock_update: MagicMock, client: FlaskClient) -> None:
    response = client.post("/api/v1/counter", json={"value": 5})
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json and "Failed to update counter." in response.json["msg"]


@patch("services.counter_service.CounterService.clear_counter")
def test_delete_counter_success(mock_clear: MagicMock, client: FlaskClient) -> None:
    response = client.delete("/api/v1/counter")
    assert response.status_code == HTTPStatus.NO_CONTENT


@patch(
    "services.counter_service.CounterService.clear_counter",
    side_effect=Exception("fail"),
)
def test_delete_counter_error(mock_clear: MagicMock, client: FlaskClient) -> None:
    response = client.delete("/api/v1/counter")
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response.json and "Failed to clear counter value." in response.json["msg"]
