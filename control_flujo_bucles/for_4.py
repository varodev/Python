def main():
    numero1 = int(input("Intro num 1: \n"))
    numero2 = int(input("Intro num 2: \n"))
    for contador in range(numero1,numero2):
        if ((contador%2) == 0):
            print(contador)

if __name__ == "__main__":
    main()


    