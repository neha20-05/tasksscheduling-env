from typing import List, Dict

class TaskEnv:
    def __init__(self):
        self.tasks: List[Dict] = []
        self.current_step: int = 0

    def state(self):
        return self.tasks

    def reset(self, level="easy"):
      self.current_step = 0

      if level == "easy":
        self.tasks = [
            {"task": "Study", "priority": 3, "deadline": 3, "done": False},
            {"task": "Exercise", "priority": 2, "deadline": 2, "done": False},
            {"task": "Sleep", "priority": 1, "deadline": 4, "done": False},
        ]
        self.max_steps = len(self.tasks)

      elif level == "medium":
        self.tasks = [
            {"task": "Study", "priority": 3, "deadline": 2, "done": False},
            {"task": "Exercise", "priority": 2, "deadline": 2, "done": False},
            {"task": "Sleep", "priority": 1, "deadline": 3, "done": False},
            {"task": "Project Work", "priority": 4, "deadline": 2, "done": False},
        ]
        self.max_steps = len(self.tasks) - 2

      else:  # hard
        self.tasks = [
            {"task": "Study", "priority": 3, "deadline": 1, "done": False},
            {"task": "Exercise", "priority": 2, "deadline": 1, "done": False},
            {"task": "Sleep", "priority": 1, "deadline": 1, "done": False},
            {"task": "Project Work", "priority": 4, "deadline": 1, "done": False},
            {"task": "Meeting", "priority": 5, "deadline": 1, "done": False},
        ]
        self.max_steps = len(self.tasks) - 3

      return self.state()
    def step(self, action):
        reward = 0

        # task completion
        if not self.tasks[action]["done"]:
            reward = self.tasks[action]["priority"] * 1.5
            self.tasks[action]["done"] = True
        else:
            reward = -1

        self.current_step += 1

        # deadlines update
        for task in self.tasks:
            if not task["done"]:
                task["deadline"] -= 1
                if task["deadline"] < 0:
                    reward -= 1.5

        # completion check
        done = all(task["done"] for task in self.tasks) or self.current_step  >= self.max_steps

        if done:
         if self.max_steps == len(self.tasks):  # easy level
          reward += 3
        else:
         reward += 2

        # partial progress reward
        completed_tasks = sum(task["done"] for task in self.tasks)
        reward += completed_tasks * 0.3

        return self.state(), reward, done,{}