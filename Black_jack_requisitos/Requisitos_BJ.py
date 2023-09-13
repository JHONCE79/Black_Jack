class Jugador:
    def __init__(self):
        self.mano = []
        self.saldo = 1000

    def pedir_carta(self, mazo):
        carta = mazo.repartir_carta()
        self.mano.append(carta)

    def plantarse(self):
        pass

    def calcular_puntuacion(self):
        pass  

    def determinar_resultado(self):
        pass

class Mazo:
    def __init__(self):
        self.cartas = []

    def repartir_carta(self):
        pass

    ######################
