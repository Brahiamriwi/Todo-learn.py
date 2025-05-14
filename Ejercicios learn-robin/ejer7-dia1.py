numero1 = int(input("Ingrese un numero inferior a 100 "))
numero2 = int(input("Ingrese otro numero inferior a 100 "))

if numero1 == numero2 and numero1 and numero2 <100:
    print("Son iguales")

elif numero1 > numero2:
    print("El numero mayor es ",numero1)

elif numero1< numero2:
    print("El numero mayor es ", numero2)    

elif numero2 and numero1 >100:
    print("numeros fuera de rango")