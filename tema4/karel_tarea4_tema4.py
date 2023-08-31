from stanfordkarel import *

def main():
    rellenar_al_frente()
    put_beeper()
    turn_left()
    move()
    turn_left()

    rellenar_al_frente()
    put_beeper()
    girar_derecha()
    move()
    girar_derecha()

    rellenar_al_frente()
    put_beeper()
    turn_left()
    move()
    turn_left()

    rellenar_al_frente()
    put_beeper()
    girar_derecha()
    move()
    girar_derecha()

    rellenar_al_frente()
    put_beeper()
    turn_left()
    move()
    turn_left()

    rellenar_al_frente()
    put_beeper()    
    
def rellenar_al_frente():
    while (front_is_clear()):
        put_beeper()
        move()

def girar_derecha():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("karel_tarea4_tema4")