from fastapi import FastAPI
from env import TaskEnv

app = FastAPI()
env = TaskEnv()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/reset")
def reset(level: str = "easy"):
    state = env.reset(level)
    return {"state": state}

@app.post("/step")
def step(action: int):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
