import csv
import math
from collections import namedtuple
from datetime import datetime

from blueprints import applyFactorOnBP, bpNames, PLANETARY_TO_INGAME_NAME, \
    MINERALS_TO_INGAME_NAME


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


LOADED_DATA_HEADER_FORMAT = 'item_id,name,time,sell,buy,lowest_sell,highest_buy'
# DataFormat = namedtuple('DataFormat', LOADED_DATA_HEADER_FORMAT)


class DataFormat:
    def __init__(self, item_id, name, time, sell, buy, lowest_sell, highest_buy):
        self.item_id = int(item_id)
        self.name = name
        self.time = datetime.fromisoformat(time)
        self.sell = float(sell) if sell else 0
        self.buy = float(buy) if buy else 0
        self.lowest_sell = float(lowest_sell) if lowest_sell else 0
        self.highest_buy = float(highest_buy) if highest_buy else 0


def load_market_prices(file_path):
    if not file_path:
        raise ValueError('File name is empty!')
    if not file_path.endswith('.csv'):
        raise ValueError('Trying to load not csv file!')

    loaded_blueprints = {}

    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header = next(spamreader)
        if header != LOADED_DATA_HEADER_FORMAT.split(','):
            raise RuntimeError('Invalid data header fields')
        for row in spamreader:
            item_name = row[1]
            if ('Blueprint' in item_name and item_name in bpNames or
                item_name in PLANETARY_TO_INGAME_NAME.values() or
                item_name in MINERALS_TO_INGAME_NAME.values()
            ):
                data = DataFormat(*row)
                loaded_blueprints[data.name] = data

    return loaded_blueprints


def collect_items_prices(
        item, market_prices, internalItemsDict, result_price_info,
        dictToIngame):

    ingame_item_name = dictToIngame[item]
    item_price = market_prices[ingame_item_name]
    internal_items_count = internalItemsDict[item]
    item_sell_price = int(item_price.buy)
    total_items_price = item_sell_price * internal_items_count
    result_price_info[ingame_item_name] = '({}) x {} = {}'.format(
        item_sell_price,
        internal_items_count,
        total_items_price,
    )

    return total_items_price


def calculate(builder1, builder2, builder3, blueprint, save_path):
    validate_stats(builder1, builder2, builder3)

    resource_consumption_result = apply_stats_to_craft_skill(
        builder1, builder2, builder3)

    modifiedBP = applyFactorOnBP(resource_consumption_result, blueprint)

    market_prices = load_market_prices(save_path)

    totalPrice = 0

    bp_price = market_prices[modifiedBP.name].buy

    result_price_info = {
        'name': modifiedBP.name,
        'bp price': bp_price
    }

    totalPrice += bp_price

    for item in modifiedBP.planetary.dictionary:
        if not modifiedBP.planetary.dictionary[item]:
            continue
        totalPrice += collect_items_prices(
            item, market_prices, modifiedBP.planetary.dictionary,
            result_price_info, PLANETARY_TO_INGAME_NAME)

    for item in modifiedBP.minerals.dictionary:
        if not modifiedBP.minerals.dictionary[item]:
            continue
        totalPrice += collect_items_prices(
            item, market_prices, modifiedBP.minerals.dictionary,
            result_price_info, MINERALS_TO_INGAME_NAME)

    totalPrice += modifiedBP.productionStartCost
    result_price_info['Build start cost:'] = modifiedBP.productionStartCost

    result_price_info['Total price:'] = math.ceil(totalPrice)
    
    return result_price_info
