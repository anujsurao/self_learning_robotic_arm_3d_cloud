import numpy as np

class RoboticArmEnv:
    def __init__(self, grid_size=(5, 5, 5), target_position=(4, 4, 4)):
        self.grid_size = grid_size
        self.state_size = grid_size[0] * grid_size[1] * grid_size[2]
        self.action_size = 6  # Up, Down, Left, Right, Forward, Backward
        self.target_position = target_position
        self.reset()

    def reset(self):
        self.position = (0, 0, 0)
        return self._get_state()

    def step(self, action):
        x, y, z = self.position
        if action == 0:  # Up
            y = max(y - 1, 0)
        elif action == 1:  # Down
            y = min(y + 1, self.grid_size[1] - 1)
        elif action == 2:  # Left
            x = max(x - 1, 0)
        elif action == 3:  # Right
            x = min(x + 1, self.grid_size[0] - 1)
        elif action == 4:  # Forward
            z = max(z - 1, 0)
        elif action == 5:  # Backward
            z = min(z + 1, self.grid_size[2] - 1)

        self.position = (x, y, z)
        reward = 1 if self.position == self.target_position else -0.1
        done = self.position == self.target_position
        return self._get_state(), reward, done

    def _get_state(self):
        state = np.zeros(self.grid_size)
        state[self.position] = 1
        state[self.target_position] = 2
        return state.flatten()
