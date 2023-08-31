#Escribe un programa Python que tome dos listas y genera una tercera lista 
# con los elementos que tienen en común las listas anteriores.

lista1 = [34,21,6,8,79,45,77]
lista2 = [21,66,6,21,54,64,657]
lista_comunes = []

#Recorremos una lista y para cada uno de los elementos
#comprobamos si está en la lista 2

for elemento in lista1:
    if (elemento in lista2):
        lista_comunes.append(elemento)

print(lista_comunes)

        
if __name__ == "__main__":
    main()