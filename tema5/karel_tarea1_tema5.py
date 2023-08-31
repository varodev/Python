from stanfordkarel import *

def main():

    while (front_is_clear()):
        move()
        if (beepers_present()):
            pick_beeper()

    turn_left()
    move()
    turn_left()

    while (front_is_clear()):
        if (beepers_in_bag()):
            put_beeper()
        move()

if __name__ == "__main__":
    run_karel_program("karel_tarea1_tema5")