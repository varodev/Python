from stanfordkarel import *

def main():
    rellenar_al_frente()
    turn_left()
    rellenar_al_frente()
    turn_left()
    rellenar_al_frente()
    turn_left()
    rellenar_al_frente()
    
def rellenar_al_frente():
    while (front_is_clear()):
        move()
        put_beeper()

if __name__ == "__main__":
    run_karel_program("karel_tarea3_tema4")