numerosecreto = 7

numerodigitado =int(input("Ingresa un numero del 1 al 20: "))

if numerodigitado == 7:
    print("adivinaste el numero secreto")

elif numerodigitado >7 and numerodigitado<20:
    print("Es mayor al numero secreto") 

elif numerodigitado<7:
    print("Es menor al numero secreto")  

elif numerodigitado >20:
    print("Numero fuera de rango")       