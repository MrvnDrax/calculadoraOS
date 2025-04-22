def sumAvanzada(a):
    try:
        a = int(a)
        if a < 0:
            print("Error: El número debe ser un entero no negativo.")
        else:
            resultado = (a * (a + 1)) // 2
            print(f"=====El resultado de la suma avanzada es: {resultado}=====")
    except ValueError:
        print("Error: El argumento debe ser un número entero válido.")
