from env import TaskEnv
import random

env = TaskEnv()

state = env.reset("easy")

done = False
total_reward = 0
step_count = 0

print("Starting tasks:", state)

while not done:
    # choose random action
    action = random.randint(0, len(state) - 1)

    state, reward, done ,info = env.step(action)

    total_reward += reward
    step_count += 1

    print(f"\nStep {step_count}")
    print("Action taken:", action)
    print("State:", state)
    print("Reward:", reward)

print("\nAll tasks completed!")
print("Total Reward:", total_reward)