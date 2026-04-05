from fastapi import FastAPI
import gradio as gr
from env import TaskEnv
import inference

app = FastAPI()

# create env
env = TaskEnv()
current_state = None

# ---------------------------
# OpenEnv REQUIRED ENDPOINTS
# ---------------------------

@app.post("/reset")
def reset(level: str = "easy"):
    global current_state
    current_state = env.reset(level)
    return {"state": current_state}


@app.post("/step")
def step(action: int):
    global current_state
    state, reward, done, info = env.step(action)
    current_state = state
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def get_state():
    return {"state": current_state}


# ---------------------------
# Gradio UI (your existing)
# ---------------------------

def predict_ui(text):
    return inference.predict(text)


demo = gr.Interface(
    fn=predict_ui,
    inputs=gr.Textbox(label="Enter level (easy / medium / hard)"),
    outputs=gr.JSON(label="Result"),
    title="Task Scheduling AI",
    description="Type easy, medium, or hard to test the model"
)

app = gr.mount_gradio_app(app, demo, path="/")
