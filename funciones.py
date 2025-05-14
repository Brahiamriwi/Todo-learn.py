#ejercicio 1
def saludo():
    nombre = input("Ingresa tu nombre: ")
    saludo = "Como estas hoy?"
    print(f"Hola {nombre} {saludo}")
    
#ejercicio 2    
def suma():
    num1 = int(input("Ingresa un numero positivo: "))
    num2 = int(input("Ingresa un numero positivo: "))
    suma = num1 +num2
    print(f"La suma es {suma} ")

#ejercicio 3   
def par_impar():
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        print("Es par")
    else: 
        print("Es impar")

#ejercicio 4 
def mayor_edad():
    edad = input("Ingrese su edad: ")
    if edad <= 18:
        print("Eres menor de edad")
        
    else:
        print("Eres mayor de edad")
#ejercicio 5       
def conversor():
    temperatura = float(input("Ingrese temperatura: "))
    farengeith = (temperatura* 9/5) + 32   
    print(f"La temperatura en grados farenheith es: {farengeith}")   

#ejercicio 6   
def area_triangulo() :
    base = float(input("Ingrese la base del traingulo: "))
    altura = float(input("Ingrese la altura del traingulo: "))
    area = (base * altura)/2
    print(f"El area del triangulo es: {area}")

#ejercicio 7    
def numero_mayor():
    numeros = input("Ingresa la lista de numeros, separados por comas: ")
    comas = numeros.split(",")
    lista_numeros = []
    for numero in comas:
        numero = numero.strip()  
        if numero.isdigit(): 
            lista_numeros.append(int(numero))
        else:
            print(f"{numero} no es valido")
            
    num_mayor = max(lista_numeros)
    print(lista_numeros)
    print(f"El numero mayor es {num_mayor}")

#ejercicio 8    
def contar_letra():
    palabra = input("Ingrese una palabra: ")
    repetir = input("Ingrese la letra que desee contar: ")
    cantidad = palabra.count(repetir)

    print(f"La letra {repetir}, se repite {cantidad}, veces")

#ejercicio 9
def devuelve_pares():
    numeros = input("Ingresa la lista de numeros, separados por comas: ")
    comas = numeros.split(",")
    lista_numeros = []
    for numero in comas:
        numero = numero.strip()  
        if numero.isdigit(): 
            lista_numeros.append(int(numero))
        else:
            print(f"{numero} no es valido")
    
    for i in lista_numeros:
        if i % 2 == 0:
           print(f"los numeros pares son {i}")
        
#ejercicio 10           
def palidronomo():
    palabra = input("Ingrese una palabra: ")
    lista1 = list(palabra)
    lista2 = lista1.copy()
    reverso = list(reversed(lista2))
    
    if lista2 == reverso:
        print("Es polidronomo")
        
    else:
        print("No es polidronomo")

#ejercicio 11       
def factorial():
    numero = int(input("Ingrese un numero: "))
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")

#ejercicio 12  
def eliminar_duplicados():
    numeros = input("Ingresa la lista de numeros, separados por comas: ")
    comas = numeros.split(",")
    lista_numeros = []
    for numero in comas:
        numero = numero.strip()  
        if numero.isdigit(): 
            lista_numeros.append(int(numero))
        else:
            print(f"{numero} no es valido")
    
    sin_duplicados = list(set(lista_numeros))
    print(sin_duplicados)

#ejercicio 13   
def Fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#ejercicio 14
def contar_vocales():
    palabra = input("Ingrese una palabra: ")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"La palabra {palabra} tiene {contador} vocales.")

#ejercicio 15    
def invertir_texto():
    texto = input("Ingrese un texto: ")
    texto_invertido = texto[::-1]
    print(f"El texto invertido es: {texto_invertido}")

#ejercicio 16
def validar_contraseña_segura():
    contraseña = input("Ingrese una contraseña: ")
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    if not any(char.isdigit() for char in contraseña):
        print("La contraseña debe contener al menos un número.")
        return False
    if not any(char.isupper() for char in contraseña):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False
    if not any(char.islower() for char in contraseña):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False
    print("Contraseña válida.")
    return True

#ejercicio 17
def simular_dado():
    import random
    dado = random.randint(1, 6)
    print(f"El resultado del dado es: {dado}")

#ejercicio 18
def suma_elementos_unicos():
    numeros = input("Ingresa la lista de numeros, separados por comas: ")
    comas = numeros.split(",")
    lista_numeros = []
    for numero in comas:
        numero = numero.strip()  
        if numero.isdigit(): 
            lista_numeros.append(int(numero))
        else:
            print(f"{numero} no es valido")
    
    suma = sum(set(lista_numeros))
    print(f"La suma de los elementos unicos es: {suma}")

#ejercicio 19  
def generador_contraseñas():
    import random
    import string
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")   

#ejercicio 20   
def composicion_funciones():
    def suma(x, y):
        return x + y

    def multiplicacion(x, y):
        return x * y

    def composicion(x, y):
        return suma(x, y) * multiplicacion(x, y)

    resultado = composicion(2, 3)
    print(f"El resultado de la composición es: {resultado}")
    
 

        
