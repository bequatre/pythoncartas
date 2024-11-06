from carta import Carta

class Mano:
    def __init__(self):
        self.cartas = []
        self.valor = 0
    
    def añadirCarta(self,carta):
        self.cartas.append(carta)
        self.valor = 0
        for carta in self.cartas:
            if carta.valor in ["Jota","Reina","Rey"]:
                self.valor += 10
            elif carta.valor == "As":
                self.valor += 11
            else:
                self.valor += int(carta.valor)
        return self.valor
    
    def mostrarMano(self):
        for carta in self.cartas:
            print(carta)

class Mano2:
    def __init__(self):
        self.cartas2 = []
        self.valor2 = 0
    
    def añadirCarta(self,carta):
        self.cartas2.append(carta)
        self.valor2 = 0
        for carta in self.cartas2:
            if carta.valor in ["Jota","Reina","Rey"]:
                self.valor2 += 10
            elif carta.valor == "As":
                self.valor2 += 11
            else:
                self.valor2 += int(carta.valor)
        return self.valor2
    
    def mostrarMano(self):
        for carta in self.cartas2:
            print(carta)