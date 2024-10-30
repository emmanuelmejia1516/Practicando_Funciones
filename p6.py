print("Mejia Suarez Emmanuel Alexander_3w_1197: practica de funciones")

# Programa 6: Argumentos arbitrarios de palabras clave
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")  # Salida: His last name is Refsnes
