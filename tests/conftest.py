import sys
import os
from unittest.mock import MagicMock
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import main  # import module, not string

@pytest.fixture
def client(monkeypatch):
    mock_session = MagicMock()
    mock_session.run.return_value = [[1]]
    # Correct way: patch the module's attribute
    monkeypatch.setattr(main, 'session', mock_session)
    return TestClient(main.app)
