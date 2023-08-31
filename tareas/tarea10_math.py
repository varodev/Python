import random

def main():
    resultado_tirada = 0
    num_veces_1 = 0
    num_veces_2 = 0
    num_veces_3 = 0
    num_veces_4 = 0
    num_veces_5 = 0
    num_veces_6 = 0

    for i in range(0,1000):
        resultado_tirada = random.randint(1,6)

        if (resultado_tirada == 1):
            num_veces_1 +=1
        elif (resultado_tirada == 2):
            num_veces_2 +=1
        elif (resultado_tirada == 3):
            num_veces_3 +=1
        elif (resultado_tirada == 4):
            num_veces_4 +=1
        elif (resultado_tirada == 5):
            num_veces_5 +=1
        elif (resultado_tirada == 6):
            num_veces_6 +=1
        else:
            #Nos protegemos ante cualquier error 
            print("Resultado tirada erróneo") 
    
    #Con triple comilla podemos poner múltiples líneas en el código
    print(f"""Ha salido el 1 {num_veces_1} veces, el 2 {num_veces_2} veces,
    el 3 {num_veces_3}  veces, el 4 {num_veces_4} veces, el 5 {num_veces_5} veces,
    el 6 {num_veces_6} veces""")


if __name__=="__main__":
    main()