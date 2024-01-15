from interface.user_input import user_inputs

def calculate_compliance_factor():
    reg_conditions = user_inputs['regulatory_conditions']
    if reg_conditions == 'Lenient':
        return 1.1
    elif reg_conditions == 'Strict':
        return 0.8
    elif reg_conditions == 'Custom':
        return user_inputs.get('custom_compliance_factor', 1.0) # INPUT_REQUIRED {Provide default custom compliance factor here}
    else:
        return 1.0 # INPUT_REQUIRED {Define behavior for unspecified regulatory conditions}
