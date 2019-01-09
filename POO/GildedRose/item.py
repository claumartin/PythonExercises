class Item:


    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality


    def __repr__(self):
        return '%s, %s, %s' % (self.getName(), self.getSellIn(), self.getquality())



if __name__ == '__main__':

    pato = Item('pato', 20, 4)

    assert pato.getName() == 'pato'
    assert pato.getSellIn() == 20
    assert pato.getQuality() == 4