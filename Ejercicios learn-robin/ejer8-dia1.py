peso = int(input("Ingrese su peso: "))
estatura = float(input("Ingrese su medida en metros: "))
 
imc = peso/estatura

if imc < 18.5:
    print("bajo peso")

elif 18.5>imc<24.9:
    print("Normal")    

elif 25>imc<29.9:
    print("sobrepeso")   

elif imc>=30:
    print("Obesidad")   