class Hora:

    def __init__(self, hora, minuto, segundo):

        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    


    def setHora(self):

        assert 0 <= self.hora <= 23 and 0 <= self.minuto <= 59 and 0 <= self.segundo <= 59
        
        

    def getHora(self):

        listHora = []
        for key in self.__dict__:
            listHora.append(self.__dict__[key])

        return listHora
        


    def __repr__(self):

        return self.getHora()



    def devuelveStringHora(self):

        return '%s' % (self.hora) + ':' + '%s' % (self.minuto) + ':' + '%s' % (self.segundo)



    def __str__(self):

        return self.devuelveStringHora()




if __name__ == "__main__":
    
    miHora = Hora(11, 30, 00)
    assert miHora.devuelveStringHora() == '11:30:0'
    
    assert miHora.getHora() == [11, 30, 00]