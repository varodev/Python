from stanfordkarel import *

def main():
    while (front_is_clear()):
        move()
        
        if(beepers_present()):
            pick_beeper()


if __name__ == "__main__":
    run_karel_program("karel_ejemplo1_tema5")