#Ejercicio 1:numero positivo o negativo
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

#Ejercicio 2:numero par o impar
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
#Ejercicio 3:mayor de 2 numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print(f"El numero mayor es {num1}") 
elif num2 > num1:
    print(f"El numero mayor es {num2}")
else:
    print("Los numeros son iguales")

#Ejercicio 4: calsificacion de edad
edad = int(input("Ingrese su edad: "))
if edad < 12 and edad >= 0:
    print("Eres un niño")
elif edad < 18 and edad >= 12:
    print("Eres un adolescente")    
elif edad < 60 and edad >= 18:
    print("Eres un adulto")     
else:
    print("Eres un adulto mayor")
    
#Ejercicio 5: nota aprobatoria
nota = float(input("Ingrese su nota de 1 a 10: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")
    
#Ejercicio 6: multiplo de 3 y/o 5
numero = int(input("Ingrese un numero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("El numero es multiplo de 3 y 5")
elif numero % 3 == 0:
    print("El numero es multiplo de 3")
elif numero % 5 == 0:
    print("El numero es multiplo de 5")
else:
    print("El numero no es multiplo de 3 ni de 5")
    
#Ejercicio 7: comparar 3 numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if num1 > num2 and num1 > num3:
    print(f"El numero mayor es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El numero mayor es {num2}")     
elif num3 > num1 and num3 > num2:
    print(f"El numero mayor es {num3}")
elif num1 == num2 and num1 > num3:
    print(f"El numero mayor es {num1} y {num2}")
elif num2 == num3 and num2 > num1:
    print(f"El numero mayor es {num2} y {num3}")
elif num1 == num3 and num1 > num2:
    print(f"El numero mayor es {num1} y {num3}")
else:
    print("Los tres numeros son iguales")

#Ejercicio 8: calculadora simple
def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operacion = input("Ingresa el número de la operación (1/2/3/4): ")
    
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if operacion == '1':
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == '2':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == '3':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Operación no válida.")

# ejercicio 9: verificar año bisiesto
def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
año = int(input("Ingrese un año: "))
if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
    
# ejercicio 10: validar contraseña con una previa
contraseña_previa = "contraseña123"
contraseña = input("Ingrese su contraseña: ")
if contraseña == contraseña_previa:
    print("Contraseña válida.")     
else:
    print("Contraseña incorrecta.")
    
# ejercicio 11: usar ciclo para contar del 1 al 10
for i in range(1, 11):
    print(i)

# ejercicio 12: contador descendente
for i in range(10, 0, -1):
    print(i)
    
# ejercicio 13: sumar N numeros
def sumar_numeros(n):
    suma = 0
    for i in range(n):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        suma += numero
    return suma
n = int(input("¿Cuántos números desea sumar? "))
suma_total = sumar_numeros(n)
print(f"La suma total es: {suma_total}")

# ejercicio 14: tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")  
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# ejercicio 15: suma hasta numero ingresado
def suma_hasta_numero(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma
numero = int(input("Ingrese un número: "))
suma_total = suma_hasta_numero(numero)
print(f"La suma de los números desde 1 hasta {numero} es: {suma_total}")

# ejercicio 16: numero secreto 
import random
def adivinar_numero_secreto():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        intento = int(input("Adivina el número secreto (entre 1 y 100): "))
        intentos += 1
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"Adivinaste el número en {intentos} intentos.")
            break

# ejercicio 17: cuenta gresiva con pausa
import time
def cuenta_regresiva():
    segundos = int(input("Ingrese el número de segundos para la cuenta regresiva: "))
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("¡Tiempo terminado!")
    
# ejercicio 18: multiplos de 3 entre 1 y 100
def multiplos_de_tres():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)

# ejercicio 19: factorial de un numero
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(n)
print(f"El factorial de {n} es: {resultado}")

# ejercicio 20: dibujar una pirame de asteriscos
def dibujar_piramide(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
n = int(input("Ingrese la altura de la pirámide: "))
dibujar_piramide(n)

# ejercicio 21:suma de numeros en una lista hasta que se escriba fin
def suma_lista():
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    suma_total = sum(numeros)
    print(f"La suma de los números ingresados es: {suma_total}")
suma_lista()

# ejercicio 22: buscar un elemento en una lista
def buscar_elemento(lista, elemento):
    if elemento in lista:
        print(f"{elemento} está en la lista.")
    else:
        print(f"{elemento} no está en la lista.")
lista = [1, 2, 3, 4, 5]
elemento = int(input("Ingrese el elemento a buscar: "))
buscar_elemento(lista, elemento)

# ejercicio 23: promedio de calificaciones
def promedio_calificaciones():
    calificaciones = []
    while True:
        entrada = input("Ingrese una calificación (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            calificacion = float(entrada)
            calificaciones.append(calificacion)
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de las calificaciones es: {promedio}")
    else:
        print("No se ingresaron calificaciones.")
promedio_calificaciones()

# ejercicio 24: numeros pares de una lista
def numeros_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    return pares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = numeros_pares(lista)
print(f"Números pares en la lista: {pares}")

# ejercicio 25: ordenar una lista   
def ordenar_lista(lista):
    return sorted(lista)
lista = [5, 2, 9, 1, 5, 6]
lista_ordenada = ordenar_lista(lista)
print(f"Lista ordenada: {lista_ordenada}")

# ejercicio 26: eliminar duplicados de una lista
def eliminar_duplicados(lista):
    return list(set(lista))
lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = eliminar_duplicados(lista)
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# ejercicio 27: lista al reves
def lista_al_reves(lista):
    return lista[::-1]
lista = [1, 2, 3, 4, 5]
lista_reversa = lista_al_reves(lista)
print(f"Lista al revés: {lista_reversa}")

# ejercicio 28: contar ocurrencias de una letra en una palabra
def contar_ocurrencias(palabra, letra):
    return palabra.count(letra)     
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese la letra a contar: ")
ocurrencias = contar_ocurrencias(palabra, letra)
print(f"La letra '{letra}' se repite {ocurrencias} veces en la palabra '{palabra}'.")

# ejercicio 29: encontrar el mayor y el menor de una lista
def mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor
lista = [4, 1, 7, 3, 9, 2]
mayor, menor = mayor_menor(lista)
print(f"Mayor: {mayor}")    
print(f"Menor: {menor}")

# ejercicio 30: separar pares e impares
def separar_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(numeros)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")







