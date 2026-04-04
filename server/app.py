from fastapi import FastAPI
import gradio as gr
import inference

app = FastAPI()

# Function for Gradio
def predict_ui(text):
    result = inference.predict(text)
    return result

# Gradio Interface
demo = gr.Interface(
    fn=predict_ui,
    inputs=gr.Textbox(label="Enter level (easy / medium / hard)"),
    outputs=gr.JSON(label="Result"),
    title="Task Scheduling AI",
    description="Type easy, medium, or hard to test the model"
)

# Mount Gradio to FastAPI
app = gr.mount_gradio_app(app, demo, path="/")
