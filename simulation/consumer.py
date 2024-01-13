from .agent import Agent


class Consumer(Agent):
    def __init__(self, name, consumption_rate):
        super().__init__(name)
        self.consumption_rate = consumption_rate

    def step(self):
        pass  # // INPUT_REQUIRED {Define the logic for consumer behavior during a simulation step}
