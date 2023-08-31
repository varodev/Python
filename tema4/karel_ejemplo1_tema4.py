from stanfordkarel import *

def main():
    for contador in range(1,5):
        put_beeper()
        move()

    turn_left()

if __name__ == "__main__":
    run_karel_program()