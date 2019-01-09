from regularItem import RegularItem


class Sulfuras(RegularItem):

    def setSellIn(self):
        pass


    def updateQuality(self):
        pass




if __name__ == '__main__':

    pato = Sulfuras('pato', 0, 80)

    assert pato.getName() == 'pato'

    pato.setSellIn()
    assert pato.getSellIn() == 0

    pato.updateQuality() 
    assert pato.getQuality() == 80