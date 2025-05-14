cuenta = float(input("Ingresa el valor de la cuenta "))

print("Que porcentaje de propina deseas dar")
print("1:10%")
print("2:15%")
print("3:20%")

Opcion= input ("Elige el porcentaje: 1,2,3: ")

if Opcion == "1":
    calcular = 0.10
elif Opcion == "2":
    calcular = 0.15
elif Opcion == "3":
    calcular = 0.20

propina = cuenta * calcular
total = cuenta + propina 

print("El valor a pagar es",total)