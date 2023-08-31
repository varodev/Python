#Ejemplo 1
"""
def f1():
    def f2():
            nivel2=2
            print(nivel0,nivel1,nivel2)

    nivel1=1
    f2()
    print(nivel0,nivel1)

nivel0=0
f1()
print(nivel0)

#Ejemplo 2
def f1():
    def f2():
            nivel2=2
            print(nivel0,nivel1,nivel2)

    global nivel0
    nivel0=3
    nivel1=1
    f2()
    print(nivel0,nivel1)

nivel0=0
f1()
print(nivel0)
"""
#Ejemplo 3
def f1():
    def f2():
            global nivel0
            global nivel1
            nivel0=5
            nonlocal nivel1
            nivel1=4
            nivel2=2
            print(nivel0,nivel1,nivel2)

    nivel1=1
    f2()
    print(nivel0,nivel1)

nivel0=0
f1()
print(nivel0)
