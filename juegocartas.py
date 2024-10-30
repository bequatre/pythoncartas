from baraja import Baraja
from mano import Mano

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()
    
    def jugar(self):
        manoJugador = Mano()
        manoJugador.añadirCarta(self.baraja.sacarCarta())
        print(f"Tu mano es {manoJugador.cartas}.")
        print(f"Total: {manoJugador.valor}")
        while manoJugador.valor < 21:
            accion = input("¿Quieres PEDIR carta o PASAR? ").lower()
            if accion == "pedir":
                manoJugador.añadirCarta(self.baraja.sacarCarta())
                print(f"Tu mano es: {manoJugador.cartas}")
                print(f"Total: {manoJugador.valor}")
            else:
                print(f"Tu puntuación final es {manoJugador.valor}")
                return
        if manoJugador.valor == 21:
            print("¡ENHORABUENA!")
        elif manoJugador.valor < 21:
            print("No has llegado a 21.")
        else:
            print("Te has pasado.")

if __name__ == '__main__':
    print("JUEGO DE 21")
    juego = Juego()
    juego.jugar()