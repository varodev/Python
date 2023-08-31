from stanfordkarel import *

def main():
    while (front_is_clear() or left_is_clear()):
        if (left_is_clear()):
            turn_left()
        move()

if __name__ == "__main__":
    run_karel_program("karel_tarea5_tema5")