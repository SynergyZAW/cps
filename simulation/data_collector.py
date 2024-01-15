import pandas as pd
from simulation.agents.farmer import Farmer
from simulation.agents.investor import Investor
from simulation.agents.consumer import Consumer

class DataCollector:
    def __init__(self):
        self.data = {
            'total_production': [],
            'compliance_levels': [],
            'investment_levels': [],
            'consumption_rates': [],
        }
    
    def collect(self, agents):
        for agent in agents:
            if isinstance(agent, Farmer):
                self.data['total_production'].append(agent.production)
                self.data['compliance_levels'].append(agent.compliance)
            elif isinstance(agent, Investor):
                self.data['investment_levels'].append(agent.investment_capital)
            elif isinstance(agent, Consumer):
                self.data['consumption_rates'].append(agent.consumption_rate)

    def to_dataframe(self):
        return pd.DataFrame(self.data)
        
    def reset(self):
        self.data = {
            'total_production': [],
            'compliance_levels': [],
            'investment_levels': [],
            'consumption_rates': [],
        }

    def calculate_total_supply(self):
        return sum(self.data['total_production'][-1])
