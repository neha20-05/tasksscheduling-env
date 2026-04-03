from env import TaskEnv

env = TaskEnv()

def reset_env():
    return env.reset()

def step_env(action: int):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
