import streamlit as st
import matplotlib.pyplot as plt
from visualization.production_output import show_total_production
from visualization.compliance_levels import show_compliance_levels

def display_visualizations(simulation_data):
    # Check if simulation_data is valid and contains necessary data
    if simulation_data is not None and not simulation_data.empty:
        st.subheader("Total Production Output")
        total_production_chart = show_total_production(simulation_data)
        st.pyplot(total_production_chart.figure)

        st.subheader("Compliance Levels")
        compliance_levels_chart = show_compliance_levels(simulation_data)
        st.altair_chart(compliance_levels_chart, use_container_width=True)
    else:
        st.write('No data available for visualization.')
