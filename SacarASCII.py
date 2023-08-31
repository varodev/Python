# CIFRADO ASCII:
# en ASCII "z" equivale a 27: son 27 caracteres en el abecedario, por lo tanto, la función que se utiliza es el módulo de 27, ejemplo: 30mod27=3.
# "a" equivale a 65, por lo que tambien se utiliza el módulo de 65, ejemplo:  2mod65=.....

cadena=array[]
cadena="hola"
cifrado=array[]

for i=0;i<length(cadena);i++) #esto es para recorrer una cadena en php.

#cesar=c+3modulo27
c=sacarascii(cadena[i])

