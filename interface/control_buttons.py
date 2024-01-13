from simulation.simulation_state import simulation_state
import streamlit as st

from simulation.simulation_engine import SimulationEngine


def show():
    st.header("Simulation Control")
    
    if 'sim_engine' not in st.session_state:
        st.session_state.sim_engine = SimulationEngine()

    sim_engine = st.session_state.sim_engine

    if st.button('Start'):
        simulation_state.start()
        st.session_state.sim_engine = sim_engine
        st.experimental_rerun()

    if st.button('Stop'):
        simulation_state.stop()

    if st.button('Reset'):
        simulation_state.reset()
        sim_engine.reset()
        del st.session_state.sim_engine
        st.experimental_rerun()
