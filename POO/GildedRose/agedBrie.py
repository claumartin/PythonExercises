from regularItem import RegularItem

class AgedBrie(RegularItem):


    def updateQuality(self):

        if self.getSellIn() >= 0:
            self.quality += 1
        
        else:
            self.quality += 2


if __name__ == '__main__':

    pato = AgedBrie('pato', 20, 4)

    assert pato.getName() == 'pato'

    pato.setSellIn()
    assert pato.getSellIn() == 19

    pato.updateQuality() 
    assert pato.getQuality() == 5