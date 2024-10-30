print("Mejia Suarez Emmanuel Alexander_3w_1197: practica de funciones")

# Programa 14: Combinando argumentos
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)  # Salida: 26
