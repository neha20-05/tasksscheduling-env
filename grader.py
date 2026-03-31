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
# GRADERS (IMPORTANT PART)
# -----------------------------
def grade_easy(state):
    """
    Easy:
    Just complete tasks
    """
    done_tasks = sum(t["done"] for t in state)
    return done_tasks / len(state)


def grade_medium(state):
    """
    Medium:
    Completion + priority weighting
    """
    score = 0
    total = 0

    for t in state:
        weight = t["priority"]
        total += weight

        if t["done"]:
            score += weight

    return score / total if total > 0 else 0


def grade_hard(state):
    """
    Hard:
    Completion + priority + deadline respect
    """
    score = 0
    total = 0

    for t in state:
        weight = t["priority"]
        total += weight

        # only reward if done BEFORE deadline
        if t["done"] and t["deadline"] >= 0:
            score += weight

    return score / total if total > 0 else 0


# -----------------------------
# MAIN EVALUATION FUNCTION
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

        results[level] = round(score, 2)

    return results


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    scores = evaluate()

    print("Evaluation Scores:")
    for level, score in scores.items():
        print(f"{level}: {score}")