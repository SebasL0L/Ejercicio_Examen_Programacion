<div align="center">

# 🛒 Sistema de Gestión de Productos e Inventario

### 📚 Proyecto desarrollado en **Python** utilizando **Programación Modular**

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode)
![Estado](https://img.shields.io/badge/Estado-Finalizado-success?style=for-the-badge)

**Sistema desarrollado para administrar productos e inventario mediante un menú interactivo en consola.**

</div>

---

# 📖 Descripción

Este proyecto consiste en el desarrollo de un **Sistema de Gestión de Productos e Inventario** implementado en **Python**, utilizando **programación modular** y buenas prácticas de desarrollo.

El sistema permite administrar un inventario completo de productos mediante un menú interactivo, utilizando diccionarios para almacenar la información y funciones independientes para cada proceso.

El proyecto fue desarrollado sin utilizar variables globales, enviando toda la información mediante parámetros entre funciones.

---

# ✨ Características

- 📦 Gestión de productos
- 📊 Gestión de inventario
- 🔎 Búsqueda por rango de precios
- 📂 Consulta de stock por categoría
- ✏ Actualización de precios
- ➕ Agregar nuevos productos
- ❌ Eliminar productos
- 📄 Mostrar inventario completo
- ✔ Validación de datos
- ⚠ Manejo de excepciones
- 🧩 Programación modular

---

# 📁 Estructura del Proyecto

```text
📁 EJERCICIO_EXAMEN
│
├── 📄 app.py
├── 📄 modulo.py
├── 📄 README.md
└── 📄 .gitignore
```

---

# 🛠 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| 🐍 Python | Desarrollo del sistema |
| 💻 Visual Studio Code | Editor de código |
| 🌐 Git | Control de versiones |
| ☁ GitHub | Repositorio remoto |

---

# 🖥 Menú Principal

```text
===============================
      MENÚ PRINCIPAL
===============================

1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
```

---

# ⚙ Funcionamiento

```text
            Usuario
                │
                ▼
          Menú Principal
                │
                ▼
             app.py
                │
      Solicita información
                │
                ▼
            modulo.py
                │
      ┌─────────┴─────────┐
      ▼                   ▼
 Productos           Inventario
      │                   │
      └─────────┬─────────┘
                ▼
      Resultado en pantalla
```

---

# 📦 Estructuras de Datos

El sistema trabaja con dos diccionarios relacionados por el código del producto.

## Productos

```python
productos = {

    "P101":["Cuaderno","Papelería",2490,True],

    "P102":["Lápiz","Papelería",590,True]

}
```

| Campo | Descripción |
|-------|-------------|
| Código | Identificador único |
| Nombre | Nombre del producto |
| Categoría | Tipo de producto |
| Precio | Valor del producto |
| Disponible | Estado del producto |

---

## Inventario

```python
inventario = {

    "P101":[30,15],

    "P102":[120,50]

}
```

| Campo | Descripción |
|-------|-------------|
| Stock | Cantidad disponible |
| Vendidos | Cantidad vendida |

---

# 🚀 Funciones Implementadas

## 📂 Gestión de Productos

- ➕ Agregar productos
- ❌ Eliminar productos
- ✏ Actualizar precios
- 📄 Mostrar productos

---

## 🔍 Consultas

- Buscar productos por rango de precio.
- Consultar stock por categoría.
- Buscar productos mediante su código.

---

## ✔ Validaciones

El sistema valida:

- Código
- Nombre
- Categoría
- Precio
- Disponibilidad
- Stock
- Productos vendidos

---

# 📚 Conceptos Aplicados

- 🧩 Programación Modular
- 🐍 Python
- 📦 Diccionarios
- 📋 Listas
- 🔁 Ciclos `while`
- 🔄 Ciclos `for`
- 🔀 Condicionales
- 🛡 Validación de datos
- ⚠ Manejo de excepciones (`try-except`)
- 📥 Entrada de datos
- 📤 Salida de datos
- 📌 Parámetros
- 🔙 Retorno de funciones

---

# ▶ Cómo ejecutar el proyecto

### Clonar el repositorio

```bash
git clone https://github.com/SebasL0L/Ejercicio_Examen_Programacion.git
```

### Ingresar al proyecto

```bash
cd Ejercicio_Examen_Programacion
```

### Ejecutar

```bash
python app.py
```

---

# 📸 Capturas

Puedes agregar imágenes del programa creando una carpeta llamada **imagenes**.

```text
📁 imagenes
│
├── menu.png
├── agregar_producto.png
├── eliminar_producto.png
├── mostrar_productos.png
└── buscar_precio.png
```

Luego solo debes agregarlas así:

```markdown
![Menú](imagenes/menu.png)

![Agregar](imagenes/agregar_producto.png)
```

---

# 👨‍💻 Autor

**Sebastián Carrasco**

Proyecto desarrollado como práctica de **Fundamentos de Programación**, aplicando programación modular, estructuras de datos y control de versiones con Git y GitHub.

---

<div align="center">

## ⭐ ¡Gracias por visitar este proyecto!

Si el proyecto te resultó útil o interesante, puedes darle una ⭐ al repositorio.

</div>