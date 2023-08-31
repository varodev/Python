#Calculo de letra de NIF
#Crea un programa que te pida los números del DNI y te devuelva la letra. La fórmula para calcular la letra del DNI es:
#El numero de 8 cifras del DNI, dividirlo entre 23 y con el resto de la división miramos la tabla.

# 0=T 	1=R 	2=W 	3=A 	4=G 	5=M 	6=Y 	7=F 	8=P 	9=D 	10=X 	11=B 
# 12=N 	13=J 	14=Z 	15=S 	16=Q 	17=V 	18=H 	19=L 	20=C 	21=K 	22=E

print("Inserte su número de DNI sin letra")
dni=input()
dni=int(dni)
resultado=dni%23
#Otra opción
#resultado=int(dni)%23
letras="TRWAGMYFPDXBNJZSQVHLCKE"
print("La letra que corresponde al DNI "+str(dni)+ " es "+ letras[resultado])
