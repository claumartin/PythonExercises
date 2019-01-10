class Fecha:

    def __init__(self, dia, mes, año):
        
        self.dia = dia
        self.mes = mes
        self.año = año


    def incrementarFecha(fecha, incremento):
        
        assert isinstance(incremento, int) and incremento > 0

        #Para operar interpretaremos los meses del 0 al 11 
        # y los días del 0 al 30

        fecha.mes -= 1
        fecha.dia -= 1

        diasTotales = fecha.dia + incremento

        while diasTotales > 31:

            mesesIncremento = diasTotales / 30

            if mesesIncremento > 11:

                añosIncremento = mesesIncremento / 11
                fecha.año += int(añosIncremento) 
                
                diasTotales = diasTotales % 30

            else:
            
                fecha.mes += int(mesesIncremento)

                diasTotales = diasTotales % 30

        fecha.dia = int(diasTotales) + 1
        fecha.mes += 1
        


    def setFecha(self, incremento):

        assert 1 <= self.dia <= 31 and 1 <= self.mes <= 12 and 1900 <= self.año <= 3000

        self.incrementarFecha(incremento)

        assert 1 <= self.dia <= 31 and 1 <= self.mes <= 12 and 1900 <= self.año <= 3000
        


    
    def devuelveNombreMes(self):

        meses = {'1': 'ENERO', '2': 'FEBRERO', '3': 'MARZO', '4': 'ABRIL', '5': 'MAYO', '6': 'JUNIO', '7': 'JULIO', 
       '8': 'AGOSTO', '9': 'SEPTIEMBRE', '10': 'OCTUBRE','11': 'NOVIEMBRE', '12': 'DICIEMBRE'}

        key = str(self.mes)
        mes = meses[key]

        assert isinstance(mes, str)

        return mes
        


    def getFecha(self):
        return '%s' % (self.dia) + '-' + self.devuelveNombreMes() + '-' + '%s' % (self.año)



    def __repr__(self):

        return self.getFecha()






if __name__ == '__main__':

    hoy = Fecha(10, 1, 2019)
    assert hoy.getFecha() == '10-ENERO-2019'

    hoy.setFecha(1)
    mañana = hoy.getFecha()
    assert mañana == '11-ENERO-2019'

    hoy.setFecha(30)
    enUnMes = hoy.getFecha()
    assert enUnMes == '11-FEBRERO-2019'

    hoy.setFecha(360)
    enUnAño = hoy.getFecha()
    assert enUnAño == '11-FEBRERO-2020'

    hoy.setFecha(20)
    ultimoDiaMes = hoy.getFecha()
    assert ultimoDiaMes == '31-FEBRERO-2020'

    hoy.setFecha(279)
    ultimoMes = hoy.getFecha()
    assert ultimoMes == '10-DICIEMBRE-2020'
