class Fecha:
    def __init__(self, dia, mes, año):
        
        self.dia = dia
        self.mes = mes
        self.año = año



    def incrementarFecha(fecha, incremento):
        
        diasRestantes = fecha.dia + incremento
        
        while diasRestantes >= 30:
            if diasRestantes >= 360:
                incrementoAños = diasRestantes/360
                fecha.año += int(incrementoAños)
                diasRestantes = diasRestantes % 360
            
            elif diasRestantes >= 30:
                incrementoMeses = diasRestantes/30
                fecha.mes += int(incrementoMeses)
                diasRestantes = diasRestantes % 30
        
        fecha.dia = int(diasRestantes)

        


    

    def setFecha(self, incremento):
        self.incrementarFecha(incremento)


    def getFecha(self):

        return '%s' % (self.dia) + '-' + '%s' % (self.mes) + '-' + '%s' % (self.año)


    def __repr__(self):

        return self.getFecha()




if __name__ == '__main__':

    hoy = Fecha(10, 1, 2019)

    assert hoy.getFecha() == '10-1-2019'

    hoy.setFecha(1)
    mañana = hoy.getFecha()
    assert mañana == '11-1-2019'

    hoy.setFecha(30)
    enUnMes = hoy.getFecha()
    assert enUnMes == '11-2-2019'

    hoy.setFecha(360)
    enUnAño = hoy.getFecha()
    assert enUnAño == '11-2-2020'

    hoy.setFecha(530)
    diaRandom = hoy.getFecha()
    assert diaRandom == '1-8-2021'