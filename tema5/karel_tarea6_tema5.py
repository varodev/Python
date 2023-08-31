from stanfordkarel import *

def main():
    while (front_is_clear() or left_is_clear()):
        if (beepers_present()):
            pick_beeper()
        else:
            put_beeper()

        if (left_is_clear()):
            turn_left()
            
        move()

if __name__ == "__main__":
    run_karel_program("karel_tarea6_tema5")