from random import shuffle

class Carta():
    def __init__(self, tipo, num):
        self.tipo = tipo
        self.num = num
    
    def printear(self):
        print(f"{self.num} de {self.tipo}")
    
    def comparar(self, otra_Carta):
        return (self.tipo == otra_Carta.tipo) and (self.num == otra_Carta.num)

class Mazo():
    def __init__(self):
        self.cartas = [Carta("Comodin", 0), Carta("Comodin", 0)]
        for tipo in ["Basto", "Oro", "Espada", "Copa"]:
            for num in range(1,13):
                self.cartas.append(Carta(tipo, num))
    
    def mezclar(self):
        shuffle(self.cartas)
    
    def sacar_carta(self, Carta):
        for i in self.cartas:
            if i.comparar(Carta):
                self.cartas.remove(i)
                return True
        return False

    def sacar_tope(self):
        return self.cartas.pop(0)
    
    def vacio(self):
        return self.cartas == []

    def repartir_manos(self, mano1, mano2, cant):
        for i in range(cant): mano1.tomar_carta(self)
        for i in range(cant): mano2.tomar_carta(self)

class Mano():
    def __init__(self):
        self.cartas = []
    
    def tomar_carta(self, mazo_cartas):
        self.cartas.append(mazo_cartas.sacar_tope())
    
    def ver_cartas(self):
        for carta in self.cartas: carta.printear()

    def tirar_carta(self, i):
        return self.cartas.pop(i)

class Juego():
    def __init__(self):
        self.mazo = Mazo()

class TrucoArg(Juego):
    def __init__(self):
        super().__init__()
        self.mazo.sacar_carta(Carta("Comodin", 0))
        self.mazo.sacar_carta(Carta("Comodin", 0))        
        for tipo in ["Basto", "Oro", "Espada", "Copa"]:
            for num in range(8,10):
                self.mazo.sacar_carta(Carta(tipo, num))
        self.mazo.mezclar()
        self.mano1 = Mano()
        self.mano2 = Mano()
        self.mazo.repartir_manos(self.mano1, self.mano2, 3)

    def gana_envido(self):
        pass
        


#mazo1 = Mazo()
#mano1 = Mano()
#mano1.tomar_carta(mazo1)
#mano1.cartas[0].printear()


JuegoTruco = TrucoArg()
JuegoTruco.mano1.ver_cartas()
JuegoTruco.mano2.ver_cartas()
