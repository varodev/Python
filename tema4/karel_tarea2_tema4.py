from stanfordkarel import *

def main():
    while (front_is_clear()):
        move()
        put_beeper()

    turn_left()

    while (front_is_clear()):
        move()
        put_beeper()
    
    turn_left()

    while (front_is_clear()):
        move()
        put_beeper()

    turn_left()

    while (front_is_clear()):
        move()
        put_beeper()
    

if __name__ == "__main__":
    run_karel_program("karel_tarea2_tema4")