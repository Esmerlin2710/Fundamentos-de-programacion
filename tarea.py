"""Crea un programa que permita crear, leer y actualizar archivos de texto. 

El archivo debe tener la siguiente estructura:

NOMBRE: XXXXX

MATRICULA: XXXXXX

CORREO: XXXXXX

TELEFONO: XXXXXXX

Crea un menu de opciones con las siguientes opciones:

crear archivo
guardar registros
leer archivo
actualizar nombre ( permite escribir un nombre y lo busca en el archivo para reemplazarlo con otro valor)
cerrar
S

ubir a github"""

import os

def crearAr():
    archivo = open("Archivo.txt", "w")
    print("Creando archivo...")
    print("Archivo creado exitosamente.")
    archivo.close()

def crearRe():
    archivo = open("Archivo.txt", "a+")
    nombre = input("Ingrese su nombre: ")
    matricula = input("Ingrese su matricula: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su telefono: ")

    archivo.write(f"Nombre: {nombre}, Matricula: {matricula}, Correo: {correo}, Telefono: {telefono}\n")
    print("Datos agregados correctamente.")
    archivo.close()
    

def leerAr():
    archivo = open("Archivo.txt", "r")
    print(archivo.read())
    archivo.close()

def actuaNom():
    lista = []
    archivo = open("Archivo.txt", "r")
    for x in archivo.readlines():
        lista.append(x)
    archivo.close()
    nombre_2 = input("Ingrese el nombre a cambiar: ")
    encontrado = False  
    for index, linea in enumerate(lista):
        if linea.startswith(f"Nombre: {nombre_2}"):
            partes = linea.split(",")
            nombre_3 = input("Ingrese el nuevo nombre: ")
            lista[index] = f"Nombre: {nombre_3}, {partes[1]}, {partes[2]}, {partes[3]}\n"
            encontrado = True
            print("Nombre cambiado.")
    if not encontrado:
        print("Nombre no encontrado en el archivo.")
    archivo = open("Archivo.txt", "w")
    for linea in lista:
        archivo.write(linea)
    archivo.close()

def menu():
    while True:
        print("-" * 50)
        print("MENU")
        print("-" * 50)
        print("1. Crear Archivos")
        print("2. Crear Registros")
        print("3. Leer archivo")
        print("4. Actualizar Nombre")
        print("5. Salir")
        print("6. Eliminar registro.")
        

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            crearAr()
        elif opcion == "2":
            crearRe()
        elif opcion == "3":
            leerAr()
        elif opcion =="4":
            actuaNom()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        elif opcion == "6":
            os.remove("Archivo.txt")
     
menu()
