from blueprints import applyFactorOnBP


def validate_stats(stat1, stat2, stat3):
    if not (0 <= stat1 <= 5 and 0 <= stat2 <= 5 and 0 <= stat2 <= 5):
        raise ValueError('Stats values out of range')

    if stat1 < 4 and (stat2 or stat3):
        raise ValueError('Stat 1 less then 4, but other one exists')

    if stat2 < 5 and stat3:
        raise ValueError('Stat 2 less then 5, but stat 3 exists')


def apply_stats_to_craft_skill(builder1, builder2, builder3):
    default_resource_consumption = 150

    builder1 = builder1 * 6
    builder2 = builder2 * 4
    builder3 = builder3 * 1

    return default_resource_consumption - builder1 - builder2 - builder3


def load_market_prices(file_path):
    return []


def calculate(builder1, builder2, builder3, blueprint, save_path):
    validate_stats(builder1, builder2, builder3)

    resource_consumption_result = apply_stats_to_craft_skill(
        builder1, builder2, builder3)

    modifiedBP = applyFactorOnBP(resource_consumption_result, blueprint)

    market_prices = load_market_prices(save_path)

    totalPrice = 0

    for resource in modifiedBP:
        totalPrice += market_prices[resource.id] * resource

    return totalPrice


