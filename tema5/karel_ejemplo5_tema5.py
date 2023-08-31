from stanfordkarel import *

def main():

    while (front_is_clear() and beepers_in_bag()):
        if (beepers_present()):
                pick_beeper()  
        else:
            put_beeper()

        move()

if __name__ == "__main__":
    run_karel_program("karel_ejemplo5_tema5")