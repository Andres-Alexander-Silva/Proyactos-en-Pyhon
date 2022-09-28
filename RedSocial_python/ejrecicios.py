#Agrega una opción que permita agregar un nuevo amigo a tu lista. Esta funcionalidad solamente agregará al usuario, 
# sin pedir autorización y aceptación por parte del destinatario como hace Facebook. 
# Es decir, que la relación de amistad solamente existe en un sentido.

# def color_frecuente(lista):
#     az = 0
#     rj = 0
#     vr = 0
#     am = 0
#     for i in range(0,len(lista)):
#         if lista[i] == "azul": az += 1
#         elif lista[i] == "rojo": rj += 1
#         elif lista[i] == "verde": vr += 1
#         elif lista[i] == "amarillo": am += 1
#     if (az >= rj) and (az >= vr) and (az >= am): return ("azul",az)
#     elif (rj >= az) and (rj >= vr) and (rj >= am): return ("rojo",rj)
#     elif (vr >= az) and (vr >= rj) and (vr >= am): return ("verde",vr)
#     elif (am >= az) and (am >= rj) and (am >= vr): return ("amarillo",am)

# colores = ["azul","rojo","verde","verde","verde","rojo","verde","verde","azul","amarillo","azul","azul","verde","verde","verde","amarillo","amarillo"]
# print(color_frecuente(colores))


# contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
# splitted = contactos.split(";")
# print(splitted)
# import string

# def remplazo(original):
#     i = 0
#     while i < len(original):
#         if original[i].isupper():
#             original = original.replace(original[i], "$")
#         i = i + 1
#     return original

# palabra = remplazo("Hola Andres")
# print(palabra)

# def ocurrencia(str):
#     return str.count("1") - str.count("0")

# cadena = "0000011111101"
# print(ocurrencia(cadena))

# def mezclador(str_a, str_b):
#     if len(str_a) > 2 and len(str_b) > 2:
#         str_1 = str_a[0:2]
#         str_2 = str_b[-2:]
#         return str_1 + str_2
#     else:
#         return f"Los string introduciodos no cumplen la condicion > 2"

# texto1 = input("Introduce la primera palabra: ")
# texto2 = input("Introduce la segunda palabra: ")
# print(mezclador(texto1, texto2))

# def intercalado(str1, str2):
#     i = 0
#     cadena = " "
#     while (i < len(str1)):
#         cadena += str1[i] + str2
#         i = i + 1
#     return cadena

# txt1 = input("Ingresa la primera palabra: ")
# txt2 = input("Ingresa la segundo palabra: ")
# print(intercalado(txt1, txt2))