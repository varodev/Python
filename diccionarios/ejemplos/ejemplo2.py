def main():
   
    dic_puntuacion_juego = {
        'alex': 3434,
        'nora': 584068,
        'neo':43453
    }

    #for elemento in dic_puntuacion_juego:
    #    print(elemento)

    #for elemento in dic_puntuacion_juego:
    #    print(dic_puntuacion_juego[elemento])

    print(dic_puntuacion_juego.keys())
    print(dic_puntuacion_juego.values())

    for elemento in dic_puntuacion_juego.keys():
        print(elemento)

if __name__ == "__main__":
    main()