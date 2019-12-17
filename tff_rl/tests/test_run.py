from keras import Sequential
from keras.layers import Flatten, Dense, Activation

import gym
from tff_rl.core.memory import ReplayMemory
from tff_rl.core.policies import PolicyQ1
from tff_rl.core.q import QAgent


def test_cart_pole():
    env = gym.make("CartPole-v1")
    observation = env.reset()

    obs_space_shape = env.observation_space.shape
    nb_actions = env.action_space.n

    model = Sequential()
    model.add(Flatten(input_shape=(1,) + obs_space_shape))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(nb_actions, activation='linear'))

    memory = ReplayMemory()
    policy = PolicyQ1()

    QAgent(env=env, model=model, memory=memory, policy=policy)

    for _ in range(10):
        env.render()
        action = env.action_space.sample()  # your agent here (this takes random actions)
        observation, reward, done, info = env.step(action)

        if done:
            observation = env.reset()
    env.close()
