# tests/conftest.py
import sys
import os
import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

# Add root folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

@pytest.fixture
def client(monkeypatch):
    # Mock the ONNX session so tests can run without a model file
    mock_session = MagicMock()
    mock_session.run.return_value = [[1]]  # example output
    monkeypatch.setattr('main.session', mock_session)

    return TestClient(app)
