from fastapi import FastAPI
from pydantic import BaseModel
import inference

app = FastAPI()

class RequestData(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Server running "}

@app.post("/predict")
def predict(data: RequestData):
    return {"result": inference.predict(data.text)}

# ADD THIS MAIN FUNCTION
def main():
    return app
