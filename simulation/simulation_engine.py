from .agency_registry import AgencyRegistry
from .data_collector import DataCollector
from .market_conditions import calculate_supply_from_production
from simulation.agents.regulator import Regulator
from interface.user_input import user_inputs

class SimulationEngine:
    def __init__(self):
        self.agency_registry = AgencyRegistry()
        self.data_collector = DataCollector()
        self.market_conditions = {}
        self.regulators = [Regulator('Regulator1', 0.1)]

    def run(self):
        supply = calculate_supply_from_production(self.agency_registry.farmers)
        self.market_conditions['supply'] = supply
        self.agency_registry.step_agents(self.market_conditions)
        self.data_collector.collect(self.agency_registry.get_all_agents())

        for regulator in self.regulators:
            regulator.regulate_agencies(self.agency_registry)
            self.data_collector.collect_regulatory_data(regulator)

        print('Simulation run complete. Data collected.')

    #... rest of the code
