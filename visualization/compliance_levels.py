import altair as alt

def show_compliance_levels(df):
    compliance_df = df.explode('compliance_levels')
    chart = alt.Chart(compliance_df).mark_bar().encode(
        x=alt.X('index:O', title='Time Step'),
        y=alt.Y('mean(compliance_levels):Q', title='Average Compliance Level'),
        tooltip=['mean(compliance_levels)']
    ).properties(
        title='Compliance Levels Over Time',
        width=600,
        height=400
    )
    return chart
