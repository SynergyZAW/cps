from simulation_state import simulation_state
import streamlit as st


def debug_session_state():
    try:
        if 'initialized' not in simulation_state:
            st.warning('Simulation state not initialized.')
            simulation_state['initialized'] = True
        else:
            st.info('Simulation state already initialized.')
    except Exception as e:
        st.error('Session state debugging failed: {}'.format(e))
        # INPUT_REQUIRED {Specify a recovery or reporting mechanism for session state errors}
