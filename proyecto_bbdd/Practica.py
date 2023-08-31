import moduloBBDDPractica
import mysql.connector

salir = False
while (not salir):
    menu = int(input("""\nQue desea consultar:
    \t1: Dar de alta una serie
    \t2: Dar de alta a un actor
    \t3: Mostrar listado de las series
    \t4: Mostrar en una página web un listado de las series
    \t5: Mostrar info de una serie a partir de su título.
    \t6: Mostrar página web con la información de una serie a partir de su título
    \t7: Mostrar el título de la series donde aparece un determinado actor
    \t8: Mostrar en una página web el título de la series donde aparece un determinado actor. 
    \tJunto al título de cada serie debe aparecer un enlace a la página de IMDB de la serie.
    \t9: Salir
    \n"""))
    miConexBBDD = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "filmoteca_programacion"
    )
    miCursor = miConexBBDD.cursor()
    
    if (menu == 1): 
        codigoSerie = int(input("Intro codigo de serie:\n"))
        titulo = input("Introduzca el titulo:\n")
        numTemporadas = int(input("Intro num de temporadas:\n"))
        enlace = input("Introduzca el enlace:\n")
        moduloBBDDPractica.insertarSerie(codigoSerie,titulo,numTemporadas,enlace,miConexBBDD,miCursor)


    elif (menu == 2):
        codigoPersona = int(input("Intro codigo de la persona:\n"))
        nombre = input("Introduzca el nombre:\n")
        apellidos = input("Introduzca los apellidos:\n")
        fecNac = input("Introduza la fecha de nacimiento (AAAA-MM-DD):\n")
        nacionalidad = input("Introduza la nacionalidad:\n")
        titulo = input("Introduzca el titulo de la serie a la que pertenece:\n")
        repeticion = False
        while (not repeticion):
            rol = int(input("""Introduzca el rol que ocupa en la serie:\n
            1. Actor\n
            2. Director\n"""))
            if (rol == 1):
                rol_serie = "actor"
                repeticion = True
            elif (rol == 2):
                rol_serie = "director"
                repeticion = True
            else:
                repeticion = False
        moduloBBDDPractica.insertarActor(codigoPersona,nombre,apellidos,fecNac,nacionalidad,miConexBBDD,miCursor,titulo,rol_serie)

    elif (menu == 3):
        consulta = "SELECT * FROM series ORDER BY titulo"
        resultado = moduloBBDDPractica.consultarDatos(consulta,miConexBBDD,miCursor)
        for fila in resultado:
            print(fila)

    elif (menu == 4):
        consulta = "SELECT * FROM series ORDER BY titulo"
        resultado = moduloBBDDPractica.construirListadoSeries(consulta,miConexBBDD,miCursor)


    elif (menu == 5):
        titulo = input("Introduzca el titulo:\n")
        consulta = f"SELECT * FROM series WHERE titulo = '{titulo}'"
        resultado = moduloBBDDPractica.consultarDatos(consulta,miConexBBDD,miCursor)
        if (resultado == []):
            print("No disponemos de esa serie")
        else:
            print(resultado)

    elif (menu == 6):
        titulo = input("Introduzca el titulo:\n")
        consulta = f"SELECT * FROM series WHERE titulo = '{titulo}'"
        resultado = moduloBBDDPractica.construirListadoSeries(consulta,miConexBBDD,miCursor)


    elif (menu == 7):
        pagina = False
        nombre = input("Introduzca el nombre:\n")
        apellidos = input("Introduzca el apellido:\n")
        consulta = f"SELECT series.titulo,series.enlace FROM personas,series,seriesPersonas WHERE personas.cod_persona = seriesPersonas.cod_persona AND seriesPersonas.cod_serie = series.cod_serie AND nombre = '{nombre}' AND apellidos = '{apellidos}' AND rol LIKE 'actor%' ORDER BY titulo;"
        resultado = moduloBBDDPractica.buscarSerieActor(consulta,miConexBBDD,miCursor)
        for fila in resultado:
            print(fila)


    elif (menu == 8):
        pagina = False
        nombre = input("Introduzca el nombre:\n")
        apellidos = input("Introduzca el apellido:\n")
        consulta = f"SELECT series.titulo,series.enlace FROM personas,series,seriesPersonas WHERE personas.cod_persona = seriesPersonas.cod_persona AND seriesPersonas.cod_serie = series.cod_serie AND nombre = '{nombre}' AND apellidos = '{apellidos}' AND rol LIKE 'actor%' ORDER BY titulo;"
        resultado = moduloBBDDPractica.buscarSerieActorPagina(consulta,miConexBBDD,miCursor)

    elif (menu == 9):
        salir = True

    else:
        print("Opcion Incorrecta")