#Calculo de letra de NIE para extranjeros

#Crea un programa que te pida los números del DNI extranjeros y te devuelva la letra. 
#Los DNI extranjeros empiezan por las letras X Y Z , y tienen 7 digitos en lugar de 8
#Tenemos que sustituir las letras por un numero para llegar a los 8 digitos, la equivalencia es:
#X=0	Y=1	Z=2
#Una vez tengamos el numero de 8 cifras, dividirlo entre 23 y con el resto de la división miramos la tabla siguiente:

# 0=T 	1=R 	2=W 	3=A 	4=G 	5=M 	6=Y 	7=F 	8=P 	9=D 	10=X 	11=B 
# 12=N 	13=J 	14=Z 	15=S 	16=Q 	17=V 	18=H 	19=L 	20=C 	21=K 	22=E



print("Inserte su número de NIE con el digito de control (X, Y o Z)")
nie=input()
primerDigito=nie[0]
print(primerDigito)
#demasDigitos=nie[1:8]
demasDigitos=nie[1:len(nie)]
print(demasDigitos)
if primerDigito=="X":
    niefinal="0"+demasDigitos
if primerDigito=="Y":
    niefinal="1"+demasDigitos
if primerDigito=="Z":
    niefinal="2"+demasDigitos
print(niefinal)
resultado=int(niefinal)%23
#Otra opción
#resultado=int(dni)%23
letras="TRWAGMYFPDXBNJZSQVHLCKE"
print("La letra que corresponde al NIE "+nie+ " es "+ letras[resultado])
