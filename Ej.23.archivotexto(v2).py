manolo=open("Ej.23.archivotexto(v2).txt","r")

for x in manolo:
    print(x)


print("\n"+"#"*60+"\n")

manolo=open("Ej.23.archivotexto(v2).txt","a")
texto=("Esto es una línea de texto")
manolo.write(texto)

manolo=open("Ej.23.archivotexto(v2).txt","r")

for x in manolo:
    print(x)
