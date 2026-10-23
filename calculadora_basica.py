
print("CALCULADORA BÁSICA")
print("1. Potencia")
print("2. Raíz cuadrada")

opcion = input("Elige una opción: ")

if opcion == "1":
    base = float(input("Ingresa la base: "))
    exponente = float(input("Ingresa el exponente: "))
    print("Resultado:", base ** exponente)

elif opcion == "2":
    numero = float(input("Ingresa un número: "))

    if numero >= 0:
        print("Resultado:", numero ** 0.5)
    else:
        print("No se puede calcular la raíz real de un número negativo")

else:
    print("Opción no válida")
