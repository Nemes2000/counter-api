import pytest
from api import create_app  # Adjust path as necessary


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
            "SERVER_NAME": "localhost",
        }
    )
    return app


@pytest.fixture
def client(app):
    return app.test_client()
