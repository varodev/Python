saludo = "Hola amigos"

def main():
    for i in range(10):
        saludar()
        saludar_v2()
           
def saludar():
    print(saludo)

def saludar_v2():
    print("*********")
    print(saludo)
    print("*********")
    
if __name__=="__main__":
    main()

    