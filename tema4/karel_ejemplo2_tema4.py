from stanfordkarel import *

def main():
    for contador in range(1,6):
        turn_left()
        move()
        girarDerecha()
        move()
        pick_beeper()


def girarDerecha():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo2_tema4")