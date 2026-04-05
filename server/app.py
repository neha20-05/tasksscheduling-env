from fastapi import FastAPI
import gradio as gr
from env import TaskEnv
import inference

app = FastAPI()

env = TaskEnv()
current_state = None

# ---------------------------
# OpenEnv endpoints
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
# Gradio UI
# ---------------------------

def predict_ui(text):
    return inference.predict(text)


demo = gr.Interface(
    fn=predict_ui,
    inputs=gr.Textbox(label="Enter level (easy / medium / hard)"),
    outputs=gr.JSON(label="Result"),
    title="Task Scheduling AI",
    description="Type easy, medium, or hard"
)

app = gr.mount_gradio_app(app, demo, path="/")


# ---------------------------
# ✅ REQUIRED MAIN FUNCTION
# ---------------------------

def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# VERY IMPORTANT
if __name__ == "__main__":
    main()
