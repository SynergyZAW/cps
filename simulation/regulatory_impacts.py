from interface.user_input import user_inputs

def calculate_compliance_factor_effect():
    """
    Calculate the compliance factor effect based on regulatory conditions provided by the user.

    Returns:
    float: The compliance factor to be applied to farmer's production.
    """
    reg_conditions = user_inputs['regulatory_conditions']
    if reg_conditions == 'Lenient':
        return 1.1  # for lenient conditions, farmers might produce more due to relaxed rules
    elif reg_conditions == 'Strict':
        return 0.8  # for strict conditions, farmers might produce less due to stringent rules
    elif reg_conditions == 'Custom':
        # Custom compliance factor as input by the user
        return user_inputs.get('custom_compliance_factor', 1)
    else:
        return 1  # default if condition is not recognized