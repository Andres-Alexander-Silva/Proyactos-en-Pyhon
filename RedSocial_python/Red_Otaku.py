import funciones_RedOtaku as Red
#Mensaje de Bienvenida
print("Bienvanidos a la Red Otaku\n")
nombre = Red.obtener_nombre()
print("Hola ",nombre, " Bienvenido a la Red Otaku")
#Verificamos si el archivo existe
if Red.consultar_archivo(nombre):
    print("Leyendo los datos del usuario", nombre, "desde archivo.")
    (nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav,muro) = Red.leer_usuario(nombre)
else:
    (nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav,muro) = Red.obtener_datos()
print("\nMuy Bien ",nombre," Estos son los datos de tu perfil.")
print("----------------------")
print(Red.mostrar_datos(nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav))
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con la Red Otaku")
print("-----------------------------------")
#Ciclo el cual evalua las apciones que el usuario realizara
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        Red.escrinbir_mensaje(nombre, amigos, muro)
    elif opcion == 2:
        print("----------------------")
        print(Red.mostrar_datos(nombre,edad,metros,centimetros,amigos,sexo,pais,ciudad,num_telefono,anime_fav))
        print("----------------------")
    elif opcion == 3:
        Red.actualizar_perfil()
    elif opcion == 4:
        Red.cambiar_perfil(nombre)
    elif opcion == 5:
        Red.mostrar_muro(muro)
    elif opcion == 6:
        Red.agregar_amigos(amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en", nombre)
        Red.escribir_usuario(nombre, edad, metros, centimetros, amigos, sexo, pais, ciudad, num_telefono, anime_fav,muro)
        print("Archivo", nombre, "Guardado")
#Mensaje de despedida
print("Gracias por utilizar la Red Otaku. !Hasta Pronto¡")