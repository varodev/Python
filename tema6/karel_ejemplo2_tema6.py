from stanfordkarel import *

def main():
    while (no_beepers_present()):
        if (right_is_clear()):
            girar_derecha()
        while (front_is_blocked()):
            turn_left()
        move()

def girar_derecha():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo2_tema6")