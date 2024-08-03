from dqn_agent import DQNAgent
from environment import RoboticArmEnv
import numpy as np

def train_model(episodes=1000, max_steps=500, batch_size=32):
    env = RoboticArmEnv()
    agent = DQNAgent(state_size=env.state_size, action_size=env.action_size)

    for e in range(episodes):
        state = env.reset()
        state = np.reshape(state, [1, env.state_size])
        total_reward = 0

        for time in range(max_steps):
            action = agent.act(state)
            next_state, reward, done = env.step(action)
            total_reward += reward
            next_state = np.reshape(next_state, [1, env.state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print(f"Episode: {e}/{episodes}, Score: {total_reward}")
                break

            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        if e % 50 == 0:
            agent.save(f"model_{e}.h5")
