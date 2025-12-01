from fastapi import FastAPI
import onnxruntime as ort

app = FastAPI()
session = ort.InferenceSession("model.onnx", providers=['AzureExecutionProvider', 'CPUExecutionProvider'])

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
