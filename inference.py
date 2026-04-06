import os
from openai import OpenAI
from server.env import TaskEnv

# -------------------------
# REQUIRED ENV VARIABLES
# -------------------------
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# -------------------------
# MAIN PREDICT FUNCTION
# -------------------------
def predict(level="easy"):
    env = TaskEnv()

    state = env.reset(level)

    print(f"[START] task=task-scheduling env=custom model={MODEL_NAME}")

    done = False
    step = 0
    rewards = []

    while not done and step < 10:
        step += 1

        # simple action logic
        action = 0

        state, reward, done, info = env.step(action)
        rewards.append(reward)

        print(f"[STEP] step={step} action={action} reward={reward} done={done} error=null")

    success = done
    score = sum(rewards)

    print(f"[END] success={success} steps={step} score={score} rewards={rewards}")

    return {
        "success": success,
        "score": score
    }

def main():
    predict("easy")


if __name__ == "__main__":
    main()
