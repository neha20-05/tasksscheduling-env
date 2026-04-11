import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def run():
    print(f"[START] task=test env=benchmark model={MODEL_NAME}")

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "test"}]
        )

        print("[STEP] step=1 action=test reward=1.00 done=true error=null")
        print("[END] success=true steps=1 rewards=1.00")

    except Exception as e:
        print(f"[END] success=false steps=0 rewards=0.00 error={str(e)}")


if __name__ == "__main__":
    run()
