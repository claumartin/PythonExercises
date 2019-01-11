class Fecha:

    def __init__(self, dia, mes, año):
        
        self.dia = dia
        self.mes = mes
        self.año = año


    def incrementarFecha(fecha, incremento):
        
        assert isinstance(incremento, int) and incremento > 0

        diasTotales = fecha.dia + incremento

        while diasTotales > 31:

            mesesTotales = int(diasTotales / 30) + fecha.mes

            while mesesTotales > 12:

                añosIncremento = int(mesesTotales / 12)
                fecha.año += añosIncremento
                mesesTotales = int(mesesTotales % 12)

            
            fecha.mes = mesesTotales
            diasTotales = int(diasTotales % 31)
        
        fecha.dia = diasTotales
                
            

               
			
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

    hoy.setFecha(31)
    enUnMes = hoy.getFecha()
    assert enUnMes == '11-FEBRERO-2019'

    hoy.setFecha(372)
    enUnAño = hoy.getFecha()
    assert enUnAño == '11-FEBRERO-2020'

    hoy.setFecha(20)
    ultimoDiaMes = hoy.getFecha()
    assert ultimoDiaMes == '31-FEBRERO-2020'

    hoy.setFecha(289)
    ultimoMes = hoy.getFecha()
    assert ultimoMes == '10-DICIEMBRE-2020'

    