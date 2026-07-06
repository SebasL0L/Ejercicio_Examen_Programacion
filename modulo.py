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




# valicaiones 
def validar_codigo(codigo, productos):

    codigo = codigo.strip().upper()

    if codigo == "":
        return False

    if codigo in productos:
        return False

    return True

def validar_nombre(nombre):

    return nombre.strip() != ""


def validar_categoria(categoria):

    return categoria.strip() != ""


def validar_precio(precio):

    return precio > 0


def validar_disponible(disponible):

    disponible = disponible.strip().lower()

    return disponible in ["s", "n"]


def validar_stock(stock):

    return stock >= 0


def validar_vendidos(vendidos):

    return vendidos >= 0

