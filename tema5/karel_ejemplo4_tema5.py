from stanfordkarel import *

def main():

    while (front_is_clear()):
        if (right_is_clear() or left_is_clear()):
                put_beeper()      
        move()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo4_tema5")