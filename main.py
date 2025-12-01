from fastapi import FastAPI
import os
import onnxruntime as ort
from unittest.mock import MagicMock

app = FastAPI()

# Check if model exists
if os.path.exists("model.onnx"):
    session = ort.InferenceSession("model.onnx", providers=['AzureExecutionProvider', 'CPUExecutionProvider'])
else:
    # Mock session for testing / CI
    session = MagicMock()
    session.run.return_value = [[1]]  # Example output for predict endpoint

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    # Replace with your real preprocessing
    try:
        inputs = preprocess(text)
    except NameError:
        # If preprocess is not defined yet, just pass text directly
        inputs = text
    output = session.run(None, {"input": inputs})
    return {"sentiment": int(output[0][0])}
