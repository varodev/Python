
saludo = "Hola amigos"

def main():
    global saludo
    for i in range(10):
        saludo = "Adios"
        saludar()
        
def saludar():
    print(saludo)
    
if __name__=="__main__":
    main()

    