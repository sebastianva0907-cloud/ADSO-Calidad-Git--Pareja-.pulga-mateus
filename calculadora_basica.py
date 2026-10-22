def calculadora_basica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicación:", num1 * num2)

    if num2 != 0:
        print("División:", num1 / num2)
    else:
        print("No se puede dividir entre cero.")

calculadora_basica()