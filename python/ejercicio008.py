#ingrese un número y diga si es par o impar


numero = int (input("ingrese un número: "))
if (numero == 0):
    print("Cero")
if(numero % 2 == 0):
    print("Es par")
else:
    print("Es impar")
