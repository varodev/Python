def main():
    numero1 = int(input("Intro num 1: \n"))
    numero2 = int(input("Intro num 2: \n"))

    while(numero1 <= numero2):
        if ((numero1 % 2) == 0):
            print(numero1)
        numero1+=1

if __name__ == "__main__":
    main()