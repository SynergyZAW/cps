from interface.user_input import user_inputs

def calculate_adjusted_demand(regulatory_conditions):
    current_demand = user_inputs.get('market_demand', 50)  # default to 50 if not provided

    demand_adjustment_factor = {
        'Lenient': 1.1,
        'Strict': 0.9,
        'Custom': user_inputs.get('custom_compliance_factor', 1)
    }
    
    adjusted_demand = current_demand * demand_adjustment_factor.get(regulatory_conditions, 1)

    return {
        'adjusted_demand': adjusted_demand
    }

def calculate_compliance_factor_effect():
    """
    Calculate the compliance factor effect based on regulatory conditions provided by the user.

    Returns:
    float: The compliance factor to be applied to farmer's production.
    """
    reg_conditions = user_inputs['regulatory_conditions']
    if reg_conditions == 'Lenient':
        return 1.1  
    elif reg_conditions == 'Strict':
        return 0.8  
    elif reg_conditions == 'Custom':
        return user_inputs.get('custom_compliance_factor', 1)
    else:
        return 1  
