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


# valicaiones.


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


# Consultas


def buscar_codigo(codigo, productos):

    codigo = codigo.strip().upper()

    return codigo in productos


def stock_categoria(categoria, productos, inventario):

    total = 0

    for codigo in productos:

        if productos[codigo][1].lower() == categoria.lower():
            total += inventario[codigo][0]

    print("Stock total:", total)


def buscar_precio(precio_min, precio_max, productos, inventario):

    encontrados = []

    for codigo in productos:

        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock > 0:
            encontrados.append((productos[codigo][0], codigo))

    encontrados.sort()

    if len(encontrados) == 0:
        print("No se encontraron productos.")

    else:
        for nombre, codigo in encontrados:
            print(nombre, "-", codigo)


def mostrar_productos(productos, inventario):

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for codigo in productos:

        print("\n----------------------------")
        print("Código:", codigo)
        print("Nombre:", productos[codigo][0])
        print("Categoría:", productos[codigo][1])
        print("Precio: $", productos[codigo][2])
        print("Disponible:", productos[codigo][3])
        print("Stock:", inventario[codigo][0])
        print("Vendidos:", inventario[codigo][1])
        print("----------------------------")


# Gestión de productos


def actualizar_precio(codigo, nuevo_precio, productos):

    codigo = codigo.strip().upper()

    if codigo in productos:
        productos[codigo][2] = nuevo_precio
        return True

    return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):

    codigo = codigo.strip().upper()

    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]

    return True


def eliminar_producto(codigo, productos, inventario):

    codigo = codigo.strip().upper()

    if codigo in productos:
        del productos[codigo]
        del inventario[codigo]
        return True

    return False
