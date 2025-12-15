import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture(scope="function")
def test_client():
    return TestClient(
        app=app,
        base_url="http://localhost:8000",
    )
