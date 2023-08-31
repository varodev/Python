from stanfordkarel import *


def main():
    for contador in range(1,4):
        move()

    hacer_tronco()
    hacer_copa()
    turn_left()

    while(front_is_clear()):
        move()
    turn_left()

    for contador in range(1,8):
        move()

    hacer_tronco()
    hacer_copa()

def hacer_tronco():
    turn_left()

    for contador in range(1,5):
        put_beeper()
        move()

def hacer_copa():
    turn_left()

    for contador in range(1,3):
        put_beeper()
        move()
    girar_derecha()

    for contador in range(1,5):
        put_beeper()
        move()
    girar_derecha() 

    for contador in range(1,5):
        put_beeper()
        move()
    girar_derecha()

    for contador in range(1,5):
        put_beeper()
        move()
    girar_derecha()

    for contador in range(1,3):
        put_beeper()
        move()
    
def girar_derecha():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("karel_tarea3_tema6")