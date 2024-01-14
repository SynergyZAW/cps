import logging
from .farmer import Farmer
from .regulator import Regulator
from .data_collector import DataCollector
from .agency_registry import AgencyRegistry
from .simulation_state import simulation_state
from interface.user_input import user_inputs
import streamlit as st

logging.basicConfig(filename='simulation_errors.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s')

class SimulationEngine:
    def __init__(self):
        self.farmers = [Farmer('Farmer1', 100, True)]
        self.regulators = [Regulator('Regulator1', 0.1)]
        self.market_conditions = {'demand': 0, 'price': 0}
        self.data_collector = DataCollector()
        self.agency_registry = AgencyRegistry()

    def step(self):
        if not simulation_state.active:
            return
        try:
            regulatory_conditions = self.get_regulatory_conditions()
            for farmer in self.farmers:
                farmer.step(self.market_conditions, regulatory_conditions)
            for regulator in self.regulators:
                regulator.step(self.market_conditions)
            self.agency_registry.step_agents(self.market_conditions)
            self.data_collector.collect(self.farmers)
            self.data_collector.collect(self.agency_registry.get_all_agents())
        except Exception as e:
            logging.error('An error occurred in the simulation step: %s', e)
            st.error('An error occurred in the simulation step. Please check the logs for more details.')

    def run(self, steps=24):
        self.reset()
        simulation_state.start()
        try:
            for _ in range(steps):
                if not simulation_state.active:
                    break
                user_input = user_inputs()
                if user_input.get('manual_override'):
                    demand = user_input.get('manual_demand', 0)
                    price = user_input.get('manual_price', 0)
                    self.market_conditions = {'demand': demand, 'price': price}
                else:
                    # Placeholder for future market condition logic
                    self.market_conditions = {'demand': 0, 'price': 0}
                self.step()
        except Exception as e:
            logging.error('An error occurred during the simulation run: %s', e)
            st.error('An error occurred during the simulation run. Please check the logs for more details.')
        finally:
            simulation_state.stop()

    def reset(self):
        self.farmers = [Farmer('Farmer1', 100, True)]
        self.regulators = [Regulator('Regulator1', 0.1)]
        self.market_conditions = {'demand': 0, 'price': 0}
        self.data_collector.reset()
    
    def get_simulation_data(self):
        return self.data_collector.to_dataframe()

