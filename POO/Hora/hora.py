class Hora:

    def __init__(self, hora, minuto, segundo):

        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        





    def __str__(self):

        return '%s' % (self.hora) + ':' + '%s' % (self.minuto) + ':' + '%s' % (self.segundo)




if __name__ == "__main__":
    
    miHora = Hora(11, 30, 00)
    assert print(miHora) # It is '11:30:0'