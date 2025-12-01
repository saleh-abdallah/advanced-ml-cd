# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from main import app  # make sure this is your FastAPI app

@pytest.fixture
def client():
    return TestClient(app)
