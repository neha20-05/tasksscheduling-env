from fastapi import FastAPI
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from env import TaskEnv

app = FastAPI()
env = TaskEnv()

class Action(BaseModel):
    action: int

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset(level: str = "easy"):
    state = env.reset(level)
    return {"state": state}

@app.post("/step")
def step(action: Action):
    state, reward, done, _ = env.step(action.action)
    return {"state": state, "reward": reward, "done": done}

@app.get("/state")
def get_state():
    return {"state": env.state()}

async def main(scope, receive, send):
    await app(scope, receive, send)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
