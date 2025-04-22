from func.sumar import sumar
from func.resta import restar
from func.multiplicacion import multiplicacion
from func.dividir import dividir
from func.suma_avanzada import sumAvanzada

def mostrar_menu():
    print("======= Calculadora Básica =======")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar los primeros n números")
    print("6. Salir")
    print("==================================")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ")

    if opcion == '1':
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            continue
        sumar(a, b)

    elif opcion == '2':
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            continue
        restar(a, b)

    elif opcion == '3':
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            continue
        multiplicacion(a, b)

    elif opcion == '4':
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            continue
        dividir(a, b)

    elif opcion == '5':
        try:
            n = int(input("Ingresa el valor de n: "))
            if n < 0:
                print("Error: El valor de n debe ser un entero no negativo.")
                continue
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            continue
        sumAvanzada(n)

    elif opcion == '6':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elige un número del 1 al 6.")
