# 1

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print(asignatura)

# 2

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura in asignaturas:
    print( "yo estudio", asignatura)

# 3

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = []

for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas.append(nota)

print("\nResultados:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

# 4

numeros = []

for i in range(6):
    numeros.append(int(input("Introduce un número ganador: ")))

numeros.sort()
print("Los números ganadores ordenados son:", numeros)

# 5

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
print("Números del 1 al 10 en orden inverso: ", numeros)

# 6

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

repetir = []

print('Evaluemos si aprobaste en base a 100')
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota <= 60:
        repetir.append(asignatura)

if repetir:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in repetir:
        print(asignatura)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")

# 7

abecedario_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', "Ñ", 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abecedario_2 = []

for letra in abecedario_1:
    if (abecedario_1.index(letra) + 1) % 3 == 0:
        continue
    else:
        abecedario_2.append(letra)

print(abecedario_2)

# 8

palabra = input("Ingrese una palabra: ").lower()
palabra_2 = palabra[::-1]

if palabra == palabra_2:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

# 9

palabra = input("Escribe una palabra: ").lower()

vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    print(f"La vocal '{vocal}' aparece {palabra.count(vocal)} veces.")

# 10

precios = [50, 75, 46, 22, 80, 65, 8]
print(max(precios))
print(min(precios))

# 11

vector_1 = [2, 3, 4]
vector_2 = [1, 0, -1]

producto_escalar = 0

for i in range(len(vector_1)):
    producto_escalar += vector_1[i] * vector_2[i]

print(f"El producto escalar es: {producto_escalar}")

# 12

numeros = input("Introduce números separados por comas: ")
lista = numeros.split(",")
media = sum(lista) / len(lista)

suma_cuadrados = 0

for x in lista:
    suma_cuadrados += (x - media) ** 2

desviacion = (suma_cuadrados / len(lista)) ** 0.5

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")



