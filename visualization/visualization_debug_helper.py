import streamlit as st


def visualize_data_debug(data):
    try:
        st.write(data)
    except Exception as e:
        st.error('An error occurred in visualization: {}'.format(e))
        # INPUT_REQUIRED {Include instructions to report this error or a way to handle it}
