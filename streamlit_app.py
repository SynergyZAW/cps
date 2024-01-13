import streamlit as st
from interface import user_input, control_buttons, output_placeholders
from simulation.simulation_engine import SimulationEngine
from simulation.simulation_state import simulation_state
from interface.output_visualization import display_visualizations

def main():
    user_input.show()
    control_buttons.show()
    output_placeholders.show()

    if 'sim_engine' in st.session_state:
        sim_engine = st.session_state.sim_engine
    
        if simulation_state.active:
            sim_engine.run()
            simulation_data = sim_engine.get_simulation_data()
            display_visualizations(simulation_data)

if __name__ == "__main__":
    main()
