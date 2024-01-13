import streamlit as st
import matplotlib
matplotlib.use('Agg')
from visualization.production_output import show_total_production
from visualization.compliance_levels import show_compliance_levels

def display_visualizations(simulation_data):
    st.subheader("Total Production Output")
    total_production_chart = show_total_production(simulation_data)
    st.pyplot(total_production_chart)

    st.subheader("Compliance Levels")
    compliance_levels_chart = show_compliance_levels(simulation_data)
    st.altair_chart(compliance_levels_chart, use_container_width=True)
