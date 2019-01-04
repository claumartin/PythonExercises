class GildedRose(object):
    def __init__(self, items):
        self.items = items


class Item:
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality
    
    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.sellIn, self.quality)


class Updates():
    def updateQuality(self):
        pass

    def setSellIn(self):
        pass
        
           
class NormalItem(Item):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def setsellIn(self):
        self.sellIn = self.sellIn - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality += valor
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, '%s quality %s out of range' % self.__class__.__name__

    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setsellIn()


class ConjuredItem(NormalItem):

    def __init__(self, name, sellIn, quality):
        NormalItem.__init__(self, name, sellIn, quality)

    def setsellIn(self):
        self.sellIn = self.sellIn - 1

    def updateQuality(self):
        if self.sellIn >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setsellIn()


class Sulfuras(NormalItem):

    def __init__(self, name, sellIn, quality):
        NormalItem.__init__(self, name, sellIn, quality)

    def updateQuality(self):
        pass

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)


class AgedBrie(NormalItem):

    def __init__(self, name, sellIn, quality):
        NormalItem.__init__(self, name, sellIn, quality)

    def setsellIn(self):
        self.sellIn = self.sellIn - 1

    def setQuality(self, valor):

        if self.quality + valor <= 50:
            self.quality = self.quality + valor
        else:
            self.quality = 50
        NormalItem.setQuality(self, valor)
        assert 0 <= self.quality <= 50, '%s quality de out of range' % self.__class__.__name__

    def updateQuality(self):

        if self.sellIn > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setsellIn()

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.sellIn, self.quality)