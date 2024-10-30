print("Mejia Suarez Emmanuel Alexander_3w_1197: practica de funciones")

# 1. Definiendo una función simple que imprime un mensaje
def my_function():
    print("Hello from a function")

# Llamando a la función
my_function()

# 2. Función con un argumento
def greet(fname):
    print(fname + " Refsnes")

# Llamando a la función con diferentes argumentos
greet("Emil")
greet("Tobias")
greet("Linus")

# 3. Función que espera dos argumentos
def full_name(fname, lname):
    print(fname + " " + lname)

# Llamando a la función con dos argumentos
full_name("Emil", "Refsnes")

# 4. Función que acepta un número desconocido de argumentos (*args)
def kids_names(*kids):
    print("The youngest child is " + kids[2])

# Llamando a la función con varios argumentos
kids_names("Emil", "Tobias", "Linus")

# 5. Función que acepta argumentos de palabra clave (key=value)
def youngest_child(child1, child2, child3):
    print("The youngest child is " + child3)

# Llamando a la función con argumentos clave=valor
youngest_child(child1="Emil", child2="Tobias", child3="Linus")

# 6. Función que acepta un número arbitrario de argumentos de palabra clave (**kwargs)
def print_last_name(**kid):
    print("His last name is " + kid["lname"])

# Llamando a la función con argumentos de palabra clave
print_last_name(fname="Tobias", lname="Refsnes")

# 7. Función con un valor de parámetro predeterminado
def country_origin(country="Norway"):
    print("I am from " + country)

# Llamando a la función con y sin argumentos
country_origin("Sweden")
country_origin("India")
country_origin()  # Usa el valor por defecto
country_origin("Brazil")

# 8. Función que recibe una lista como argumento
def print_food(food):
    for item in food:
        print(item)

# Creando una lista de frutas
fruits = ["apple", "banana", "cherry"]

# Llamando a la función y pasando la lista
print_food(fruits)

# 9. Regresando valores
def add_numbers(x, y):
    return x + y

print(add_numbers(3, 5))
print(add_numbers(5, 7))
print(add_numbers(9, 1))

# 10. Declaración del pass
def empty_function():
    pass  # Esta función no hace nada

# 11. Recursividad
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Example Results")
tri_recursion(6)  # Llamando a la función recursiva
