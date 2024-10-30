print("Mejia Suarez Emmanuel Alexander_3w_1197: practica de funciones")

# Programa 15: Recursividad
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)  # Salida: 1, 3, 6, 10, 15, 21
