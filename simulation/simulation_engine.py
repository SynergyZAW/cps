from .farmer import Farmer
from .regulator import Regulator
from .simulation_state import simulation_state
from interface.user_input import user_inputs
from .data_collector import DataCollector
import logging
import streamlit as st

logging.basicConfig(filename='simulation_errors.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s')

class SimulationEngine:
    def __init__(self):
        self.farmers = [Farmer('Farmer1', 100, True)]
        self.regulators = [Regulator('Regulator1', 0.1)]
        self.market_conditions = {'demand': 0, 'price': 0}
        self.data_collector = DataCollector()

    def set_market_conditions(self):
        self.market_conditions = {
            'demand': user_inputs.get('market_demand', 0),
            'price': 10
        }

    def step(self):
        if not simulation_state.active:
            return
        try:
            regulatory_conditions = self.get_regulatory_conditions()
            for farmer in self.farmers:
                farmer.step(self.market_conditions, regulatory_conditions)
            for regulator in self.regulators:
                regulator.step(self.market_conditions)
            self.data_collector.collect(self.farmers)
            # Here add steps related to any new agents
        except Exception as e:
            logging.error('An error occurred in the simulation step: %s', e)
            st.error('An error occurred in the simulation step. Please check the logs for more details.')

    def get_regulatory_conditions(self):
        reg_conditions = user_inputs.get('regulatory_conditions', 'Lenient')
        custom_compliance_factor = user_inputs.get('custom_compliance_factor', 1)
        compliance_factor = {
            'Lenient': 1.2,
            'Strict': 0.8,
            'Custom': custom_compliance_factor
        }.get(reg_conditions, 1)

        return {
            'compliance_factor': compliance_factor,
            'other_factors': {}
        }

    def run(self, steps=24):
        self.reset()
        simulation_state.start()
        try:
            for _ in range(steps):
                if not simulation_state.active:
                    break
                self.set_market_conditions()
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

