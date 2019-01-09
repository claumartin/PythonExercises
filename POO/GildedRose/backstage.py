from regularItem import RegularItem

class Backstage(RegularItem):

    def updateQuality(self):
        if self.getSellIn() > 10:
            self.quality += 1

        elif self.getSellIn() <= 10:
            self.quality += 2

        elif self.getSellIn() <= 5:
            self.quality += 3
        
        else:
            self.quality = 0


if __name__ == '__main__':

    pato = Backstage('pato', 20, 4)

    assert pato.getName() == 'pato'

    pato.setSellIn()
    assert pato.getSellIn() == 19

    pato.updateQuality() 
    assert pato.getQuality() == 5