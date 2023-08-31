from stanfordkarel import *

def main():
    while(front_is_clear()):
        move()

    turn_left()
    move()
    girarDerecha()

    while(front_is_clear()):
        move()

def girarDerecha():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo3_tema4")