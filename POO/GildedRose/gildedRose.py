from sulfuras import Sulfuras
from agedBrie import AgedBrie
from backstage import Backstage

class GildedRose():

    def __init__(self, stock):
        self.stock = stock

    

    def getStock(self):
        return self.stock
    

    def updateStock(self):
        for item in self.stock:
            item.updateQuality()

if __name__ == "__main__":
    

    # TEST CASES #

    stock = [Sulfuras('sulfuras', 10, 80), AgedBrie('agedBrie', 3, 4), Backstage('backstage', 5, 25)]
    tienda = GildedRose(stock)
    tienda.updateStock()

    assert tienda.getStock()[0].getQuality() == 80
    assert tienda.getStock()[0].getName() == "sulfuras"
    assert tienda.getStock()[0].getSellIn() == 10