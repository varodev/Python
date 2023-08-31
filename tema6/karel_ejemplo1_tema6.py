from stanfordkarel import *
"""
	 * Situación inicial:Partimos de un mundo con una serie de beepers, ver dibujo en 
	 * los apuntes. Karel tiene la mochila vacía inicialmente. 
	 * 
	 * Proceso:Buscamos un hueco en la pared de la izquierda para que nos de acceso a 
	 * la zona donde están los beepers.
	 * Una vez que alcanzamos la zona la recorremos en zig zag recogiendo todos los 
	 * beepers
	 * A continuación avanzamos hacia la esquina inferior derecha y ponemos beepers hasta
	 * que se acaben los que están en la mochila
	 * 
	 * Situación final: Sólo habrá beepers en la esquina inferior derecha. Estarán apilados
	 * unos encima de otros por lo que aparecerá un número sobre el beeper que indica 
	 * cuántos hay. Ver dibujo en los apuntes
	 * 
	 
"""

def main():
    buscar_hueco_izquierda()
    turn_left()
    move()
    turn_left()
    coger_beepers_de_zona()
    girar_derecha()
    llevar_beepers_a_esquina()


def buscar_hueco_izquierda():
    while (front_is_clear() and left_is_blocked()):
        move()

def coger_beepers_de_zona():
    recorrer_fila_cogiendo_beepers()
    cambiar_fila_y_girar_derecha()
    recorrer_fila_cogiendo_beepers()
    cambiar_fila_y_girar_izquierda()
    recorrer_fila_cogiendo_beepers()
    cambiar_fila_y_girar_derecha()
    recorrer_fila_cogiendo_beepers()
    cambiar_fila_y_girar_izquierda()
    recorrer_fila_cogiendo_beepers()
    cambiar_fila_y_girar_derecha()
    recorrer_fila_cogiendo_beepers()
    

def recorrer_fila_cogiendo_beepers():
    while (front_is_clear()):
        if (beepers_present()):
            pick_beeper()
        move()
        if (beepers_present()):
            pick_beeper()

def girar_derecha():
    turn_left()
    turn_left()
    turn_left()

def cambiar_fila_y_girar_derecha():
    girar_derecha()
    move()
    girar_derecha()

def cambiar_fila_y_girar_izquierda():
    turn_left()
    move()
    turn_left()

def llevar_beepers_a_esquina():
    while (front_is_clear()):
        move()
    while (beepers_in_bag()):
        put_beeper()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo1_tema6")