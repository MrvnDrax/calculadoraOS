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
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        sumar(a, b)
    elif opcion == '2':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        restar(a, b)
    elif opcion == '3':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        multiplicacion(a, b)
    elif opcion == '4':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        dividir(a, b)
    elif opcion == '5':
        n = int(input("Ingresa el valor de n: "))
        sumAvanzada(n)
    elif opcion == '6':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 6.")
