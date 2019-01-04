from gildedRose import *

if __name__ == '__main__':
    
    ##TEST PRINT OUTPUT (__repr__)
    item = Sulfuras('Sulfuras, mano de Maradona', 3, 80)
    print(item)

    ## TEST SULFURAS
    # test updateQuality
    for dia in range(1, 10):
        item.updateQuality()
        print(item)

    # test updateQuality incorret input
    item = Sulfuras('Sulfuras, mano de Dios', 3, 10000)
    for dia in range(1, 10):
        item.updateQuality()
        print(item)

    ## TEST AGED BRIE
    item = AgedBrie('Aged Brie', 2, 0)
    print(item)
    # test updateQuality
    for dia in range(1, 10):
        item.updateQuality()
        print(item)

    # test updateQuality incorret input
    item = AgedBrie('Aged Brie', 2, 100)
    for dia in range(1, 10):
        item.updateQuality()
        print(item)

    ## TEST NORMAL ITEM
    item = NormalItem('Elixir of the Mongoose', 5, 7)
    print(item)
    for dia in range(1, 10):
        item.updateQuality()
        print(item)

    ## TEST CONJURED ITEM
    item = ConjuredItem('Conjured Mana Cake', 3, 6)
    for dia in range(1, 10):
        item.updateQuality()
        print(item)

