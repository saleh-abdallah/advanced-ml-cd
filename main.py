<<<<<<< HEAD
from fastapi import FastAPI
import onnxruntime as ort

app = FastAPI()
session = ort.InferenceSession("model.onnx")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    # Your preprocessing → input conversion
    # Example only:
    inputs = preprocess(text)
    output = session.run(None, {"input": inputs})
    return {"sentiment": int(output[0][0])}
=======
from fastapi import FastAPI
import onnxruntime as ort

app = FastAPI()
session = ort.InferenceSession("model.onnx")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(text: str):
    # Your preprocessing → input conversion
    # Example only:
    inputs = preprocess(text)
    output = session.run(None, {"input": inputs})
    return {"sentiment": int(output[0][0])}
>>>>>>> 1a1f71ae28618944827e6543f0f861c593d8a044
