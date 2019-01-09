from item import Item
from updateable import Updateable


class RegularItem(Item, Updateable):
    
    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)
    

    def getName(self):
        return self.name


    def getSellIn(self):
        return self.sellIn


    def getQuality(self):
        return self.quality
    

    def setSellIn(self):
        self.sellIn -= 1


    def updateQuality(self):

        if self.getSellIn() >= 0:
            self.quality -= 1
        
        else:
            self.quality -= 2


    def setQuality(self):
        
        if updateQuality() >= 50:
            self.quality = 50

        elif updateQuality() < 0:
            self.quality = 0

        else:
            self.quality = updateQuality()

        assert 0 <= self.quality <= 50, '%s quality de out of range' % self.__class__.__name__




if __name__ == '__main__':

    pato = RegularItem('pato', 20, 4)

    assert pato.getName() == 'pato'

    pato.setSellIn()
    assert pato.getSellIn() == 19

    pato.updateQuality() 
    assert pato.getQuality() == 3