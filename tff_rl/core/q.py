"""Routines for q learning"""
from keras.layers import Flatten, Dense, Activation


class QAgent:
    def __init__(self, env, model=None, memory=None, policy=None):
        self.env = env
        self.model = model
        self.memory = memory
        self.policy = policy


    def action(self, action_space, observation, info):  # pylint: disable=no-self-use
        """Mandatory method that calculates the move based on the observation array and the action space."""
        action = None

        return action

    def forward(self):
        raise NotADirectoryError

    def backward(self):
        raise NotADirectoryError

    def load_weights(self):
        raise NotADirectoryError

    def save_weights(self):
        raise NotADirectoryError

    def compute_batch_q_values(self, state_batch):
        batch = self.process_state_batch(state_batch)
        q_values = self.model.predict_on_batch(batch)
        assert q_values.shape == (len(state_batch), self.nb_actions)
        return q_values

    def compute_q_values(self, state):
        q_values = self.compute_batch_q_values([state]).flatten()
        assert q_values.shape == (self.nb_actions,)
        return q_values
