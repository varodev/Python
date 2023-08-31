#Pintar rectángulo
#Rectángulo = base(b) X altura(a) = rectangulo(altura,base)

def pintarRectangulo(base,altura):
    for x in range(altura):
        print("*"*base)

print("Inserte la base: ")
b=int(input())
print("Inserte la altura: ")
a=int(input())
pintarRectangulo(b,a)

