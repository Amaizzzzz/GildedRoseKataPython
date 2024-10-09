# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class AgedBrieStrategy:
    def update_item(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        item.quality = min(item.quality, 50)  # Cap at 50


class BackstagePassesStrategy:
    def update_item(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0  # After the concert, quality drops to 0
        else:
            if item.quality < 50:
                item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1  # Increase by 2 if 10 days or less
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1  # Increase by 3 if 5 days or less
        item.quality = min(item.quality, 50)  # Cap at 50


class ConjuredStrategy:
    def update_item(self, item):
        item.sell_in -= 1
        degrade_rate = 2
        if item.sell_in < 0:
            degrade_rate *= 2  # Degrade four times as fast after sell-in
        item.quality = max(item.quality - degrade_rate, 0)


class SulfurasStrategy:
    def update_item(self, item):
        # Sulfuras does not change in quality or sell_in
        pass


class NormalItemStrategy:
    def update_item(self, item):
        item.sell_in -= 1
        degrade_rate = 1
        if item.sell_in < 0:
            degrade_rate = 2  # Degrade twice as fast after sell-in
        item.quality = max(item.quality - degrade_rate, 0)
        item.quality = min(item.quality, 50)  # Ensure quality is capped at 50


class GildedRose:
    def __init__(self, items: list):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        }

    def get_strategy(self, item):
        if "Conjured" in item.name:
            return ConjuredStrategy()
        return self.strategies.get(item.name, NormalItemStrategy())

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update_item(item)
