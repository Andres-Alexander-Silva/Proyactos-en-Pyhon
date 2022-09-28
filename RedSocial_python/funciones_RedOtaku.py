import os
#Funcion para obtener el nombre
def obtener_nombre():
    nombre = input("Para empezar como te llamas: ")
    return nombre
#Funcion para obtener la edad
def obtener_edad():
    edad = int(input("Cuantos años tienes: "))
    return edad
#Funcion para obtener la estatura
def obtener_estatura():
    estatura = float(input("Cuanto mides (en metros): "))
    metros = int(estatura)
    centimetros = int((estatura - metros)*100)
    return (metros, centimetros)
#Funcion para obtener el numero de amigos
def obtener_lista_amigos():
    linea = input("Escribe una lista con los nombres de tus amigos, separados por una ',': ")
    amigos = linea.split(",")
    return amigos
#Funcion para obtener el sexo
def obtener_sexo():
    sexo = input("Que sexo eres (Hombre/Mujer): ")
    while sexo != "Hombre" and sexo != "Mujer":
        sexo = input("Que sexo eres (Hombre/Mujer): ")
    return sexo
#Funcion para obtener el pais
def obtener_pais():
    pais = input("De que pais eres: ")
    return pais
#Funcion para obtener la ciudad
def obtener_ciudad():
    ciudad = input("De que ciudad eres: ")
    return ciudad
#Funcion para obtenr el numero de telefono
def obtener_num_telefono():
    num_telefono = int(input("Cual es tu numero de telefono: "))
    return num_telefono
#Funcion para obtener el anime_Fav  
def obtener_anime():
    anime_fav = input("Cual es tu anime favorito: ")
    return anime_fav
#Funcion para obtener todos los datos
def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (m, cm) = obtener_estatura()
    na = obtener_lista_amigos()
    s = obtener_sexo()
    p = obtener_pais()
    c = obtener_ciudad()
    nt = obtener_num_telefono()
    af = obtener_anime()
    muro = []
    return (n,e,m,cm,na,s,p,c,nt,af,muro)
#Funcion para mostrar el perfil del usuario
def mostrar_datos(nombre, edad, metros, centimetros, amigos, sexo, pais, ciudad, num_telefono, anime_fav):
    dato = "Nombre: {0}\nEdad: {1}\nEstatura: {2} m y {3} cm\nAmigos: {4}\n".format(nombre,edad,metros,centimetros,len(amigos))
    dato += "Sexo: {0}\nPais: {1}\nCiudad: {2}\nTelefono: {3}\nAnime favorito: {4}".format(sexo,pais,ciudad,num_telefono,anime_fav)
    return dato
#Funcion para las opciones del menu
def opcion_menu():
    print("""
    Aciones Disponibles:
    1. Escribir un mensaje publico o a tus amigos
    2. Mostrar los datos del perfil
    3. Actualizar los datos del perfil
    4. Cambiar de Pefil
    5. Mostrar mi Muro
    6. Agregar amigos
    0. Salir
    """)
    opcion = int(input("Ingresa la opcion que deseas realizar: "))
    while opcion < 0 or opcion > 7:
        print("La accion que has ingresado no es valida, Por favor ingresa una accion valida.")
        opcion = int(input("Ingresa la opcion que deseas realizar: "))
    return opcion
#Funcion para obtener el primer mensaje
def obtener_mensaje():
    mensaje = input("Vamos a publicar un mensaje, Que piensas: ")
    return mensaje
#Funcion para escribir nuestro primer mensaje 
def mostar_mensaje(origen, destinatario, mensaje):
    if destinatario == None:
        print(origen,"Dice: ",mensaje)
    else:
        print(origen, "Dice:", "@"+destinatario, mensaje)
#Funcion la cual muestra los mensajes resividos
def mostrar_muro(muro):
    print("------MURO ("+str(len(muro))+" mensaje) ------")
    for mensaje in muro:
        print(mensaje)
    print("-------------------------------------------")
#Funcion para escribir un mensaje nuevo o un mensaje a un amigo
def escrinbir_mensaje(nombre, amigos, muro):
    continuar = True
    while continuar:
        mensaje_n = input("\nDeseas escribir un mensaje (Si/No): ")
        mensaje_amigos = input("\nDeseas escribir un mensaje a tus amigos (Si/No): ")
        if mensaje_n == "Si" and mensaje_amigos == "Si":
            mensaje = obtener_mensaje()
            mostar_mensaje(nombre, None, mensaje)
            mensaje = obtener_mensaje()
            for i in amigos:
                nombre_amigo = input("ingresa el nombre de tu amiga o amigo: ")
                mostar_mensaje(nombre, nombre_amigo, mensaje)
                muro.append(mensaje)
                for amigo in amigos:
                    archivo = open(amigo,"a")
                    archivo.write(nombre+":"+mensaje+"\n")
                    archivo.close()
        elif mensaje_n == "Si"  and mensaje_amigos == "No":
            mensaje = obtener_mensaje()
            mostar_mensaje(nombre, None, mensaje)
        elif mensaje_n == "No" and mensaje_amigos == "Si":
            for i in amigos:
                nombre_amigo = input("ingresa el nombre de tu amiga o amigo: ")
                mensaje = obtener_mensaje()
                mostar_mensaje(nombre, nombre_amigo, mensaje)
                muro.append(mensaje)
                for amigo in amigos:
                    archivo = open(amigo,"a")
                    archivo.write(nombre+":"+mensaje+"\n")
                    archivo.close()
        elif mensaje_n == "" or mensaje_amigos == "":
            continue
        elif mensaje_n == "No" and mensaje_amigos == "No":
            print("\nOk sigue disfrutando de la Red otaku")
            continuar = False 
#Funcion para actualizar el perfil del usuario
def actualizar_perfil():
    actualizar_datos = input("\nQuieres actualizar tus datos (Si/No): ")
    if actualizar_datos == "Si":
        actu_nombre = input("Quieres actualizar tu nombre (Si/No): ")
        if actu_nombre == "Si":
            nombre = obtener_nombre()
        else:
            print("Ok sigue disfrutando de la Red")
        actu_edad = input("Quieres actualizar tu edad (Si/No): ")
        if actu_edad == "Si":
            edad = obtener_edad()
        else:
            print("Ok sigue disfrutando de la Red")
        actu_estatura = input("Quieres actualizar tu estatura (Si/No): ")
        if actu_estatura == "Si":
            (metros, centimetros) = obtener_estatura()
        else:
            print("Ok sigue disfutando de la Red")
        actu_num_amigos = input("Quieres actualizar tu num de amigos (Si/No): ")
        if actu_num_amigos == "Si":
            amigos = obtener_lista_amigos()
        else:
            print("Ok sigue disfrutando de la Red")
        actu_sexo = input("Quieres actualizar tu sexo (Si/No): ")
        if actu_sexo == "Si":
            sexo = obtener_sexo()
        else:
            print("ok sigue disfrutando de la Red")
        actu_pais = input("Quieres actualizar tu pais (Si/No): ")
        if actu_pais == "Si":
            pais = obtener_pais()
        else:
            print("ok sigue disfrutando de la Red")
        actu_ciudad = input("Quieres actualizar tu ciudad (Si/No): ")
        if actu_ciudad == "Si":
            ciudad = obtener_ciudad()
        else:
            print("ok sigue disfrutando de la Red")
        actu_num_telefono = input("Quieres actualizar tu num de telefono (Si/No): ")
        if actu_num_telefono == "Si":
            num_telefono = obtener_num_telefono()
        else:
            print("ok sigue disfrutando de la Red")
        actu_anime_fav = input("Quieres actualizar tu anime favorito(Si/No): ")
        if actu_anime_fav == "Si":
            anime_fav = obtener_anime()
        else:
            print("ok sigue disfrutando de la Red")
    else:
        print("No quieres actualizar tus datos, esta bien sigue disfrutando de la Red")
#Funcion la cual la ruta del archivo
def consultar_archivo(ruta):
    return os.path.isfile(ruta)
#Funcion la cual lee el nombre del usuario y rectifica que haya un archivo con ese nombre
def leer_usuario(nombre):
    archivo_usuario = open(nombre,"r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    metros = int(archivo_usuario.readline().rstrip())
    centimetros = int(archivo_usuario.readline().rstrip())
    amigos = archivo_usuario.readline().rstrip().split(",")
    sexo = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    ciudad = archivo_usuario.readline().rstrip()
    num_telefono = int(archivo_usuario.readline().rstrip())
    anime_fav = archivo_usuario.readline().rstrip()
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    archivo_usuario.close()
    return (nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav,muro)
#FUncion la cual escribe los datos del usuario en un archivo con extencion ".user"
def escribir_usuario(nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav,muro):
    archivo_usuario = open(nombre,"w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(metros)+"\n")
    archivo_usuario.write(str(centimetros)+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(ciudad+"\n")
    archivo_usuario.write(str(num_telefono)+"\n")
    archivo_usuario.write(anime_fav+"\n")
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    archivo_usuario.close()
#Funcion la cual agrega un amigo nuevo a la lista de amigos 
def agregar_amigos(amigos):
    nuevo = input("¿Quieres agregar un nuevo amigo? (Si/No): ")
    if nuevo == "Si":
        nuevo_amigo = input("Ingresa el nombre de tu amigo: ")
        amigos.append(nuevo_amigo)
    elif nuevo == "No":
        print("No quieres agregar un nuevo amigo, esta bien sigue disfurtamdo de la Red Otaku")
    return amigos
#Funcion la cual cambia de perfil al usuario
def cambiar_perfil(nombre):
    cambiar = True
    while cambiar:
        cambiar_usuario = input("Quieres cambiar de usuario (Si/No): ")
        if cambiar_usuario == "Si": 
            usuario = input("Ingresa el nombre del usuario al que quieres accedder: ")   
            if consultar_archivo(usuario):
                print("Leyendo los datos del usuario", usuario, "desde archivo.\n")
                (nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav,muro) = leer_usuario(usuario)
                print("Mostrando los datos del perfil de: ",usuario)
                print(mostrar_datos(nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav))
            else:
                print("No se puede cambiar de usuario por que", nombre, "no esta en nuestros archivos")
        elif cambiar_usuario == "No":
            print("Ok no quieres cambiar de usuario, esta bien sigue disfrutando de la Red")
            cambiar = False
        elif cambiar_usuario == "":
            continue