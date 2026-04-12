from env import TaskEnv
import random

# reproducibility
random.seed(42)


# -----------------------------
# BASELINE AGENT POLICY
# -----------------------------
def choose_action(state):
    # choose highest priority unfinished task
    available_tasks = [i for i, t in enumerate(state) if not t["done"]]

    if available_tasks:
        return max(available_tasks, key=lambda i: state[i]["priority"])
    else:
        return 0


# -----------------------------
# RUN ONE EPISODE
# -----------------------------
def run_episode(level):
    env = TaskEnv()
    state = env.reset(level)

    done = False

    while not done:
        action = choose_action(state)
        state, reward, done, _ = env.step(action)

    return state


# -----------------------------
# GRADERS
# -----------------------------
def grade_easy(state):
    done_tasks = sum(t["done"] for t in state)
    score = done_tasks / len(state)

    # force into (0,1)
    return max(0.01, min(0.99, score))


def grade_medium(state):
    score = 0
    total = 0

    for t in state:
        weight = t["priority"]
        total += weight

        if t["done"]:
            score += weight

    final = score / total if total > 0 else 0
    return max(0.01, min(0.99, final))


def grade_hard(state):
    score = 0
    total = 0

    for t in state:
        weight = t["priority"]
        total += weight

        # reward if done and deadline still valid
        if t["done"] and t["deadline"] >= 0:
            score += weight

    final = score / total if total > 0 else 0
    return max(0.01, min(0.99, final))


# -----------------------------
# MAIN EVALUATION
# -----------------------------
def evaluate():
    results = {}

    for level in ["easy", "medium", "hard"]:
        final_state = run_episode(level)

        if level == "easy":
            score = grade_easy(final_state)
        elif level == "medium":
            score = grade_medium(final_state)
        else:
            score = grade_hard(final_state)

        # round for clean output
        results[level] = round(score, 2)

    return results


# -----------------------------
# RUN (IMPORTANT FORMAT)
# -----------------------------
if __name__ == "__main__":
    scores = evaluate()
    print(scores)
