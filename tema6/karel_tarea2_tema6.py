from stanfordkarel import *


def main():
    turn_left()
    while (front_is_clear()):
        move()
    
    girar_derecha()
    buscar_hueco_izquierda()
    turn_left()
    move()
    turn_left()

    coger_beepers_de_zona()
    girar_derecha()
    buscar_hueco_izquierda()
    turn_left()
    move()
    buscar_hueco_izquierda()

    turn_left()
    while (front_is_clear()):
        move()
    
    girar_derecha()
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
    run_karel_program("karel_tarea2_tema6")