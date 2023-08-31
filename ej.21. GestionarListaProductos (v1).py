#ejercicio 21 - Gestionar los datos de stock de una tienda de comestibles.

print("\n"*2+"#"*60)
print("\n24. Que gestione los datos de stock de una tienda de comestibles, la información a recoger será: nombre del producto, precio, cantidad en stock. La tienda dispone de 10 productos distintos. El programa debe ser capaz de:\n")
print("  1.	Dar de alta un producto nuevo.\n")
print("  2.	Buscar un producto por su nombre.\n")
print("  3.	Modificar el stock y precio de un producto dado.\n")
print("#"*60+"\n"*3)

nombreProducto=["atún","leche","cebollas","pan","naranjas","agua","aceitunas",
        "tomate","almendras","castañas"]
precioProducto=[1.02,0.99,0.35,0.40,1.2,0.70,1.50,1.23,2.80,2.40]
cantidadProducto=[30,12,15,8,3,12,17,34,22,56]
tienda=[]
def main():
    print("Que desea hacer:\n")
    print("  1.	Dar de alta un producto nuevo.\n")
    print("  2.	Buscar un producto por su nombre.\n")
    print("  3.	Modificar el stock y precio de un producto dado.\n")
    print("Inserte una opción válida o 'q' para salir.\n")
    opcion=input()
    if opcion == "1":
        altaProducto()
    elif opcion == "2":
        buscarProducto()
    elif opcion == "3":
        modificarProducto()
    elif opcion == "q":
        salir()
    else:
        main()

def salir():
    print("\n"*2+"Saliendo"+"\n"*3)

def altaProducto():
    for x in range(3):
        nombre=input("Inserte el nombre")
        precio=float(input("Inserte el precio"))
        cantidad=int(input("Inserte el stock"))             
        tienda.append([nombre,precio,cantidad])
    print(tienda)

main()
