
print("CALCULADORA BÁSICA")
print("1. Sumar")
print("2. Restar")

opcion = input("Elige una opción: ")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if opcion == "1":
    print("La suma total es:", a + b)
elif opcion == "2":
    print("La resta es:", a - b)
else:
    print("Opción incorrecta")