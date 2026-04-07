from fastapi import FastAPI
import inference

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Task Scheduling API running"}

@app.get("/predict")
def predict(text: str):
    return inference.predict(text)
