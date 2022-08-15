print("El numero es Par o Impar")
while True:
    try:
        A= float(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Ingrese un valor numérico.")
if A % 2 == 0:
    print("El número es par")
else:
    print("El numero es impar")
