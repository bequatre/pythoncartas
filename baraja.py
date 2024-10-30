import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []
        palos = ["corazones","picas","diamantes","tréboles"]
        valores = ["As","2","3","4","5","6","7","8","9","10","Jota","Reina","Rey"]

        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo,valor))

    def barajar(self):
        random.shuffle(self.cartas)
    
    def mostrarCartas(self):
        for carta in self.cartas:
            print(carta)

    def contar(self):
        return len(self.cartas)

    def __repr__(self):
        return f"Baraja de {self.contar()}"
    
    def sacarCarta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None
    
    def quedanCartas(self):
        return len(self.cartas) != 0