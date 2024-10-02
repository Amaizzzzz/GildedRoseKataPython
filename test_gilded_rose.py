# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)
    
    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [Item("+5 Dexterity Vest", 0, 10)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 9)

    def test_quality_never_negative(self):
        items = [Item("+5 Dexterity Vest", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, -1) 

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 10, 40)] 
        gilded_rose = GildedRose(items)  
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 39)

    def test_sulfuras_never_decreases_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 79)  
        self.assertEqual(items[0].sell_in, 9)

if __name__ == '__main__':
    unittest.main()
