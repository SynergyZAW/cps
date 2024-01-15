from simulation.agents.farmer import Farmer
from simulation.agents.regulator import Regulator
from simulation.agents.investor import Investor
from simulation.agents.consumer import Consumer

class AgencyRegistry:
    def __init__(self):
        self.farmers = [Farmer('Farmer1', 100, True)]
        self.regulators = [Regulator('Regulator1', 0.1)]
        self.investors = [Investor('Investor1', 10000)]
        self.consumers = [Consumer('Consumer1', 1.5)]

    def step_agents(self, market_conditions):
        for agent_list in [self.farmers, self.regulators, self.investors, self.consumers]:
            for agent in agent_list:
                agent.step(market_conditions)

    def get_all_agents(self):
        return self.farmers + self.regulators + self.consumers + self.investors
