from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

@pytest.fixture
def client(monkeypatch):
    mock_session = MagicMock()
    mock_session.run.return_value = [[1]]
    monkeypatch.setattr('main.session', mock_session)
    return TestClient(app)
