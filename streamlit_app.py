import streamlit as st
from interface import user_input, control_buttons, output_visualization
from simulation.simulation_engine import SimulationEngine
from simulation.simulation_state import simulation_state

def main():
    user_input.show()
    control_buttons.show()

    if 'sim_engine' in st.session_state:
        sim_engine = st.session_state.sim_engine
    
        if simulation_state.active:
            sim_engine.run()
            simulation_data = sim_engine.get_simulation_data()
            output_visualization.display_visualizations(simulation_data)

if __name__ == "__main__":
    main()

