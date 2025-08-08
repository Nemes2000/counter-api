from flask import Flask
from flask.testing import FlaskClient
from flask_openapi3 import OpenAPI
import pytest
from api import create_app  # Adjust path as necessary


@pytest.fixture
def app() -> OpenAPI:
    app = create_app(
        {
            "TESTING": True,
            "SERVER_NAME": "localhost",
        }
    )
    return app


@pytest.fixture
def client(app: Flask ) -> FlaskClient:
    return app.test_client()
