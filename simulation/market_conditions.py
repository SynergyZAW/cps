def calculate_supply_from_production(farmers):
    return sum(farmer.production for farmer in farmers)
