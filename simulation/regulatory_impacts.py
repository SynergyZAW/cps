from interface.user_input import user_inputs

def calculate_adjusted_demand(current_demand, regulatory_conditions):
    # This function will calculate the adjusted demand based on regulatory conditions
    # The 'regulatory_conditions' parameter is a string that can be 'Lenient', 'Strict' or 'Custom'
    demand_adjustment_factor = {
        'Lenient': 1.1,
        'Strict': 0.9,
        'Custom': user_inputs.get('custom_compliance_factor', 1)
    }
    return current_demand * demand_adjustment_factor.get(regulatory_conditions, 1)
