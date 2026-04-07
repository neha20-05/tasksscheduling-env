from fastapi import FastAPI
import inference

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API running"}


# ✅ REQUIRED: RESET ENDPOINT
@app.post("/reset")
def reset():
    return {"status": "reset done"}


# ✅ REQUIRED: STEP ENDPOINT
@app.post("/step")
def step():
    return {"status": "step done"}


# existing predict
@app.get("/predict")
def predict(text: str):
    return inference.predict(text)
