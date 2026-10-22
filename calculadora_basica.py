
print("CALCULADORA BÁSICA")
print("1. Multiplicar")
print("2. Dividir")

opcion = input("Elige una opción: ")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if opcion == "1":
    print("El resultado de la multiplicación es:", a * b)
elif opcion == "2":
    if b != 0:
        print("El resultado de la división es:", a / b)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Opción no válida")
