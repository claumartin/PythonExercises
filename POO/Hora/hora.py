class Hora:

    def __init__(self, hora, minuto, segundo):

        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    


    def getHora(self):

        listHora = []
        for key in self.__dict__:
            listHora.append(self.__dict__[key])

        return listHora
        


    def __repr__(self):

        return self.getHora()



    def __str__(self):

        return '%s' % (self.hora) + ':' + '%s' % (self.minuto) + ':' + '%s' % (self.segundo)




if __name__ == "__main__":
    
    miHora = Hora(11, 30, 00)
    print(miHora) # It is '11:30:0'
    
    assert miHora.getHora() == [11, 30, 00]