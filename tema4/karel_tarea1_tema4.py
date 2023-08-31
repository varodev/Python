from stanfordkarel import *

def main():
    move()
    move()
    turn_left()

    for contador in range(1,6):
        put_beeper()
        move()

if __name__ == "__main__":
    run_karel_program("karel_tarea1_tema4")