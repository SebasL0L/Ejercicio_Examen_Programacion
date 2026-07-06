# Funciones del sistema

def leer_opcion():

    while True:

        try:

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 7:
                return opcion

            print("Debe seleccionar una opción válida.")

        except ValueError:

            print("Debe ingresar un número.")