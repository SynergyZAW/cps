def calculate_total_demand_impact(adjusted_demand, market_conditions):
    """
    Calculate the total demand impact based on adjusted demand, market trends, and consumer behavior.

    Args:
    - adjusted_demand (float): The demand adjusted for regulatory conditions.
    - market_conditions (dict): Dictionary containing market conditions such as market trends and consumer behavior factors.

    Returns:
    - float: The total demand after accounting for market trends and consumer behavior impacts.
    """
    market_trend_impact = market_conditions.get('market_trend_factor', 1)
    consumer_behavior_impact = market_conditions.get('consumer_behavior_factor', 1)

    # Combining the impacts of market trends and consumer behavior with the adjusted demand
    total_demand = adjusted_demand * market_trend_impact * consumer_behavior_impact
    return total_demand
