from fastapi import FastAPI
from pydantic import BaseModel
import inference

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}

@app.post("/predict")
def predict(data: InputData):
    result = inference.predict(data.text)
    return {"result": result}
