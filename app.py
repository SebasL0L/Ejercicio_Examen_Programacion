import os

# Archivo principal del proyecto
import modulo as mo


def main():

    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    while True:

        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Stock por categoría")
        print("2. Buscar productos por rango de precio")
        print("3. Actualizar precio")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Mostrar productos")
        print("7. Salir")

        opcion = mo.leer_opcion()

        match opcion:

            case 1:
                categoria = input("Ingrese categoría: ")
                mo.stock_categoria(categoria, productos, inventario)

            case 2:
                precio_min = int(input("Precio mínimo: "))
                precio_max = int(input("Precio máximo: "))
                mo.buscar_precio(precio_min, precio_max, productos, inventario)

            case 3:
                codigo = input("Código: ")
                nuevo_precio = int(input("Nuevo precio: "))

                if mo.actualizar_precio(codigo, nuevo_precio, productos):
                    print("Precio actualizado correctamente.")
                else:
                    print("Código inexistente.")

            case 6:
                mo.mostrar_productos(productos, inventario)

            case 7:
                print("Programa finalizado.")
                break


if __name__ == "__main__":
    main()