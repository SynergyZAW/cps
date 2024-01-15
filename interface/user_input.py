import streamlit as st

user_inputs = {}

def show():
    st.sidebar.header("User Inputs")

    user_inputs['market_demand'] = st.sidebar.slider('Market Demand', min_value=0, max_value=100, value=50)
    reg_conditions = st.sidebar.radio('Regulatory Conditions', ['Lenient', 'Strict', 'Custom'])
    user_inputs['regulatory_conditions'] = reg_conditions

    if reg_conditions == 'Custom':
        compliance_factor = st.sidebar.number_input('Custom Compliance Factor', 
                                                    min_value=0.5, 
                                                    max_value=2.0, 
                                                    value=1.0)
        user_inputs['custom_compliance_factor'] = compliance_factor
