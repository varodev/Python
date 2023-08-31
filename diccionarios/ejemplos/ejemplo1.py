def main():
    dic_personas = {
        "4345355W":"Ana Pérez",
        "2435325P":"Lucas Gómez"
    }

    dic_puntuacion_juego = {
        'alex': 3434,
        'nora': 584068,
        'neo':43453
    }

    if ('4345355W' in dic_personas):
        print(dic_personas['2435325P'])
        dic_personas['2435325P'] = "Andrea Sánchez"
        print(dic_personas['2435325P'])

    dic_precios = {}

    dic_precios["trek_8035830"] = 244
    dic_precios["orbea_307850"] = 976

    print(dic_precios)

    dic_precios["orbea_307850"] += 100

    if ("trek_8035830" in dic_precios):
        del dic_precios["trek_8035830"]

    print(dic_precios)

if __name__ == "__main__":
    main()