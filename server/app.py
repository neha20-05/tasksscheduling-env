from fastapi import FastAPI
from pydantic import BaseModel
import inference
import uvicorn

app = FastAPI()

class RequestData(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Server running 🚀"}

@app.post("/predict")
def predict(data: RequestData):
    return {"result": inference.predict(data.text)}

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
