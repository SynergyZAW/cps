from .agent import Agent


class Investor(Agent):
    def __init__(self, name, investment_capital):
        super().__init__(name)
        self.investment_capital = investment_capital

    def step(self):
        pass  # // INPUT_REQUIRED {Define the logic for investor behavior during a simulation step}
