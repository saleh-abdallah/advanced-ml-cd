from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This will be mocked in tests
session = None

class PredictRequest(BaseModel):
    text: str

def preprocess(text):
    return text

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: PredictRequest):
    text = request.text
    # Use mocked session in tests
    if session is None:
        return {"sentiment": 1}  # default fake prediction
    # Normal ONNX prediction (replace with real preprocessing)
    inputs = preprocess(text)
    output = session.run(None, {"input": inputs})
    return {"sentiment": int(output[0][0])}
