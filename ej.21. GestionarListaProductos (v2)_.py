#ejercicio 21 - Gestionar los datos de stock de una tienda de comestibles
print("Gestionar los datos de stock de una tienda de comestibles, la informacion a recoger sera:")
print("nombre del producto, precio, cantidad de stock. la tienda dispone de 10 productos distintos.")
print("El programa debe ser capaz de:")
texto1="Dar de alta un producto nuevo."
texto2="Buscar un producto por su nombre."
texto3="Modificar el stock y precio de un producto dado."
print("1 "+texto1+"\n2 "+texto2+"\n3 "+texto3)

listaproductos=["pan","agua","leche","bizcocho","tomate","lechuga","pimiento",
                "platano","harina","sal"]
listaprecios=["0,75","1,20","0,80","2,50","0,90","1,40","0,30","1,10",
              "1","0,20"]
def main():
    print("1 "+texto1+"\n2 "+texto2+"\n3 "+texto3)
    print("\nPor favor, inserte una opción o 'q' para salir\n")
    opcion=input()
    if opcion == "1":
        buscarProducto()
    elif opcion == "2":
        altaNuevoProducto()
    elif opcion == "3":
        buscarNombreProducto()
    elif opcion == "4":
        modificarStock()
    elif opcion == "5":
        modificarPrecio()
    elif opcion == "q":
        salir()
    else:
        print("\nInserte una opción válida\n")
        main()

def buscarProducto():
    producto=input("Inserte el producto a buscar: \n")
    existe=False
    contador=0
    for x in listaproductos:
        contador+=1
        if x == producto:
            existe=True
            break
    if existe:
        print("\nHay existencia de este producto " + str(contador) + "\n")
    else:
        print("\nNo hay stock\n")
    main()

def altaNuevoProducto():



    main()

def modificarStock():
    producto=input("Inserte el producto a modificar su existencia: \n")


    main()

def modificarPrecio():
    producto=input("Inserte el producto a modificar su precio: \n")
    existe=False
    contador=0
    for x in listaproductos:
        contador+=1
        if x == producto:
            existe=True
            break
    if existe:
        print("\nHay existencia de este producto " + str(contador) + "\n")
        #str(contador-1)    
        print("Su precio es "+ str(listaprecios[contador-1]))
        precioModificado=float(input("Inserte el nuevo precio.\n"))
        listaproductos[contador-1]=precioModificado
        print("El nuevo precio es "+ str(listaprecios[contador-1]))
        print(listaprecios)
    else:
        print("\nNo hay stock\n")
    main()


def salir():
    print("\nSaliendo")
    
main()
