from stanfordkarel import *

def main():

    while (front_is_clear()):
        move()
        if (left_is_clear()):
            turn_left()


if __name__ == "__main__":
    run_karel_program("karel_tarea2_tema5")