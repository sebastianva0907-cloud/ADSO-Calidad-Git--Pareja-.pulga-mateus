
print("CALCULADORA BÁSICA")
print("1. Sumar")
print("2. Restar")

opcion = input("Elige una opción: ")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if opcion == "1":
    print("Resultado:", a + b)
elif opcion == "2":
    print("Resultado:", a - b)
else:
    print("Opción no válida")