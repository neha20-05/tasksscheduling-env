from env import TaskEnv
import random

# reproducibility
random.seed(42)

def run_episode(level="easy"):
    env = TaskEnv()
    state = env.reset(level)

    total_reward = 0
    done = False

    while not done:
        available_tasks = [i for i, t in enumerate(state) if not t["done"]]

        if available_tasks:
            action = max(available_tasks, key=lambda i: state[i]["priority"])
        else:
            action = random.randint(0, len(state) - 1)

        state, reward, done, info = env.step(action)
        total_reward += reward

    return total_reward


def normalize_score(score):
    return max(0.0, min(1.0, (score + 15) / 40))


def main():
    levels = ["easy", "medium", "hard"]

    print("Evaluation Scores:")
    for level in levels:
        score = run_episode(level)
        normalized = normalize_score(score)
        print(f"{level}: {normalized:.2f}")


if __name__ == "__main__":
    main()