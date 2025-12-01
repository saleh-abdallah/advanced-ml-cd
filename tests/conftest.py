import sys
import os
from unittest.mock import MagicMock
import pytest
from fastapi.testclient import TestClient

# Mock ONNX so pytest won't crash
sys.modules['onnxruntime'] = MagicMock()

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import your FastAPI app after mocking ONNX
from main import app

@pytest.fixture
def client(monkeypatch):
    # Mock the ONNX session in your app
    mock_session = MagicMock()
    mock_session.run.return_value = [[1]]  # fake prediction output
    monkeypatch.setattr('main.session', mock_session)
    
    return TestClient(app)
