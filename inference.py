from fastapi import FastAPI
from pydantic import BaseModel
from env import TaskEnv

app = FastAPI()
env = TaskEnv()
@app.get("/")
def home():
    return {"message": "API is working"}

class Action(BaseModel):
    action: int

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: Action):
    state, reward, done = env.step(action.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
