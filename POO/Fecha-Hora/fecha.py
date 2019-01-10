class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    



    def getFecha(self):

        return '%s' % (self.dia) + '-' + '%s' % (self.mes) + '-' + '%s' % (self.año)


    def __repr__(self):

        return self.getFecha()




if __name__ == '__main__':

    hoy = Fecha(10, 1, 2019)

    assert hoy.getFecha() == '10-1-2019'