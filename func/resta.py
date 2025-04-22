def restar(a, b):
    try:
        a = float(a)
        b = float(b)
        resultado = a - b
        print(f"======El resultado de la resta es: {resultado}======")
    except ValueError:
        print("Error: Ambos argumentos deben ser números válidos (enteros o flotantes).")
