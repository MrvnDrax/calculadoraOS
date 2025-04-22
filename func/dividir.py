def dividir(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = a / b
            print(f"======El resultado de la división es: {resultado}======")
    except ValueError:
        print("Error: Ambos argumentos deben ser números válidos (enteros o flotantes).")
