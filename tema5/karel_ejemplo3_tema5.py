from stanfordkarel import *

def main():
    turn_left()
    move()
    girarDerecha()

    while (front_is_clear()):
        move()
        while (front_is_clear()):
            move()
            if (right_is_clear() and beepers_in_bag()):
                rellenarBache()      

def girarDerecha():
    turn_left()
    turn_left()
    turn_left()

def rellenarBache():
    girarDerecha()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    girarDerecha()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo2_tema5")