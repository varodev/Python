#Programa que me pida los datos de un cliente (nombre, email y teléfono)y
#los guarde en en archivo separados por coma y cada cliente por punto y coma.
#Nombre archivo clientes.csv

archivo=open("clientes.csv", "a")
cliente=[]

nombre=input("Inserte el nombre:\n")
email=input("Inserte el email:\n")
telefono=input("Inserte el teléfono:\n")
cliente.append(nombre+",")
cliente.append(email+",")
cliente.append(telefono)

for x in cliente:
    archivo.write(x)
archivo.write(";")
archivo.close()
