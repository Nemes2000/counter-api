import pytest
from unittest.mock import patch, MagicMock
from services.counter_service import CounterService, Counter


@pytest.fixture
def mock_pool():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_cursor.fetchone.return_value = Counter(id=1, value=10)

    mock_pool = MagicMock()
    mock_pool.connection.return_value.__enter__.return_value = mock_conn

    return mock_pool, mock_cursor


@patch("services.counter_service.get_pool")
def test_get_counter_success(mock_get_pool, mock_pool):
    mock_pool, mock_cursor = mock_pool
    mock_get_pool.return_value = mock_pool

    result = CounterService.get_counter()

    assert result == 10
    mock_cursor.execute.assert_called_once_with("SELECT * FROM counter WHERE id=1")


@patch("services.counter_service.get_pool")
def test_get_counter_not_found(mock_get_pool):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None

    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_pool = MagicMock()
    mock_pool.connection.return_value.__enter__.return_value = mock_conn

    mock_get_pool.return_value = mock_pool

    with pytest.raises(KeyError):
        CounterService.get_counter()


@patch("services.counter_service.get_pool")
def test_update_counter(mock_get_pool):
    mock_pool, mock_cursor = MagicMock(), MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_pool.connection.return_value.__enter__.return_value = mock_conn

    mock_get_pool.return_value = mock_pool

    CounterService.update_counter(42)
    mock_cursor.execute.assert_called_once_with(
        "UPDATE counter SET value=%s WHERE id=1", [42]
    )


@patch("services.counter_service.get_pool")
def test_clear_counter(mock_get_pool):
    mock_pool, mock_cursor = MagicMock(), MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_pool.connection.return_value.__enter__.return_value = mock_conn

    mock_get_pool.return_value = mock_pool

    CounterService.clear_counter()
    mock_cursor.execute.assert_called_once_with("UPDATE counter SET value=0 WHERE id=1")
