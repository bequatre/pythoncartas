from baraja import Baraja
from mano import Mano
from mano import Mano2

diferencia_jugador1 = 0
diferencia_jugador2 = 0

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()
    
    def jugar(self):
        manoJugador = Mano()
        manoJugador.añadirCarta(self.baraja.sacarCarta())
        manoJugador2 = Mano2()
        manoJugador2.añadirCarta(self.baraja.sacarCarta())
        print(f"La mano del jugador 1 es {manoJugador.cartas}.")
        print(f"Total del jugador 1: {manoJugador.valor}")
        print(f"La mano del jugador 2 es {manoJugador2.cartas2}.")
        print(f"Total del jugador 2: {manoJugador2.valor2}")
        while manoJugador.valor < 21 and manoJugador2.valor2 < 21:
            accion = input("Jugador 1, ¿Quieres PEDIR carta o PASAR? ").lower()
            if accion == "pedir":
                manoJugador.añadirCarta(self.baraja.sacarCarta())
                print(f"La mano del jugador 1 es: {manoJugador.cartas}")
                print(f"Total del jugador 1: {manoJugador.valor}")
            else:
                print(f"Tu puntuación final es {manoJugador.valor}")
                
                
            
            accion = input("Jugador 2, ¿Quieres PEDIR carta o PASAR? ").lower()
            if accion == "pedir":
                manoJugador2.añadirCarta(self.baraja.sacarCarta())
                print(f"La mano del jugador 2 es: {manoJugador2.cartas2}")
                print(f"Total del jugador 2: {manoJugador2.valor2}")
            else:
                print(f"Tu puntuación final es {manoJugador2.valor2}")
                return
                

        diferencia_jugador1 = manoJugador.valor - 21
        diferencia_jugador2 = manoJugador2.valor2 - 21

        if manoJugador.valor == 21:
            print("¡ENHORABUENA!, jugador 1, ¡has ganado!.")
        
        if manoJugador2.valor2 == 21:
            print("¡ENHORABUENA!, jugador 2, ¡has ganado!.")

        if diferencia_jugador1 < diferencia_jugador2:
            print("El jugador 1 se ha quedado más cerca, por lo tanto, ¡ha ganado!")
        elif diferencia_jugador1 > diferencia_jugador2:
            print("El jugador 2 se ha quedado más cerca, por lo tanto, ¡ha ganado!")
        elif diferencia_jugador1 == diferencia_jugador2:
            print("Los dos jugadores están igual de cerca, ¡hay empate!")

if __name__ == '__main__':
    print("JUEGO DE 21")
    juego = Juego()
    juego.jugar()