# 🍜 BITE ME RESTAURANT 🇰🇷

### *Sabores que te atraparán a la primera mordida. ♥*

Aplicación de gestión para un restaurante de comida coreana desarrollada en **Python**, utilizando **Programación Orientada a Objetos (POO)**, **Tkinter** para la interfaz gráfica y archivos **JSON** para la persistencia de información.

Este proyecto corresponde a la **Semana 15** de la asignatura de **Programación Orientada a Objetos** y representa la evolución del sistema desarrollado en semanas anteriores.

---

## 📚 Semana 15 — Manejo de eventos

En esta semana se incorporan los **conceptos fundamentales del manejo de eventos** dentro de la aplicación.

La principal mejora consiste en agregar la gestión de **ventas**, permitiendo relacionar un usuario con un producto mediante una acción realizada desde la interfaz gráfica.

El funcionamiento sigue el siguiente flujo:

```text
👤 Usuario
   ↓
🖱️ Acción en la interfaz
   ↓
🔘 Botón
   ↓
⚡ command=
   ↓
🔄 Callback
   ↓
⚙️ RestauranteServicio
   ↓
💾 Persistencia en ventas.json
   ↓
🖥️ Actualización de la interfaz
```

De esta manera, la interfaz se encarga de recibir las acciones del usuario, mientras que la lógica de negocio y la persistencia permanecen dentro de las capas correspondientes.

---

## 🎯 Objetivo del proyecto

El objetivo de esta semana es comprender cómo una acción realizada por el usuario puede generar una respuesta dentro de una aplicación gráfica.

Para ello, se implementa una operación de venta que permite:

* 👤 Seleccionar un usuario registrado.
* 🍜 Seleccionar un producto existente.
* 🛒 Registrar una venta.
* ⚡ Utilizar `command=` para asociar un botón con un callback.
* ⚙️ Delegar la operación a `RestauranteServicio`.
* 💾 Guardar la información en `ventas.json`.
* 📋 Mostrar las ventas registradas dentro de la interfaz.
* 🔄 Actualizar la información después de realizar una venta.

---

## ✨ Evolución del proyecto

BITE ME RESTAURANT se desarrolla de manera progresiva durante las diferentes semanas de trabajo.

En esta Semana 15 se conserva la estructura construida anteriormente y se incorpora una nueva funcionalidad:

### Antes

* 🔐 Inicio de sesión.
* 🏠 Panel principal.
* 👤 Gestión y consulta de usuarios.
* 🍜 Gestión de productos.
* 💾 Persistencia mediante archivos JSON.
* 🎨 Interfaz gráfica con Tkinter.
* 🖼️ Recursos visuales mediante `assets/`.

### Nueva implementación

* 🛍️ Sección de **Ventas**.
* 👤 Selección de usuario.
* 🍜 Selección de producto.
* 🧾 Registro de una venta.
* ⚡ Manejo de eventos mediante `command=`.
* 🔄 Uso de callbacks.
* 💾 Persistencia de ventas en `ventas.json`.
* 📋 Visualización de las ventas registradas.

---

## 🏗️ Arquitectura del proyecto

El proyecto mantiene una arquitectura modular para separar las responsabilidades de cada componente.

```text
restaurante_app/
│
├── 📁 datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── 📁 modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── 📁 servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── 📁 ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── 📁 assets/
│   ├── 📁 icons/
│   └── 📁 logo/
│
├── main.py
│
└── README.md
```

---

## 📂 Organización de carpetas

### 📁 datos

Contiene los archivos JSON utilizados para conservar la información del sistema.

* `productos.json` → almacena los productos disponibles.
* `usuarios.json` → almacena los usuarios registrados.
* `ventas.json` → almacena las ventas realizadas.

Los archivos JSON permiten conservar la información incluso después de cerrar y volver a ejecutar la aplicación.

---

### 📁 modelos

Contiene las clases principales del sistema.

#### 🍜 `producto.py`

Representa los productos disponibles en el restaurante.

Un producto contiene información como:

* Código.
* Nombre.
* Categoría.
* Precio.

#### 👤 `usuario.py`

Representa a los usuarios registrados en el sistema.

Contiene información como:

* Identificador.
* Nombre.
* Usuario.
* Contraseña.

#### 🧾 `venta.py`

Representa una venta realizada en el restaurante.

La venta relaciona:

```text
👤 Usuario
     +
🍜 Producto
     +
📅 Fecha
```

---

### 📁 servicios

Contiene la lógica encargada de trabajar con los datos.

#### 💾 `archivo_servicio.py`

Se encarga de leer y escribir los archivos JSON.

Permite mantener la información almacenada sin colocar directamente esta responsabilidad dentro de la interfaz.

#### ⚙️ `restaurante_servicio.py`

Contiene las operaciones y reglas principales del restaurante.

Entre sus responsabilidades se encuentran:

* Validar usuarios.
* Consultar productos.
* Registrar productos.
* Actualizar productos.
* Eliminar productos.
* Consultar usuarios.
* Registrar ventas.
* Validar la información de una venta.
* Guardar las ventas.

---

### 📁 ui

Contiene las vistas de la aplicación gráfica.

#### 🔐 `login_view.py`

Muestra la pantalla de inicio de sesión y valida las credenciales mediante `RestauranteServicio`.

#### 🖥️ `main_view.py`

Contiene la interfaz principal de la aplicación.

Desde esta vista se puede acceder a las diferentes secciones del sistema:

* 🏠 Inicio.
* 🍜 Productos.
* 👤 Usuarios.
* 🛍️ Ventas.
* 🚪 Cerrar sesión.

---

### 📁 assets

Contiene los recursos gráficos utilizados por la aplicación.

Incluye:

* 🖼️ Logo.
* 🔰 Icono de la aplicación.
* 🏠 Iconos del menú.
* ➕ Icono para agregar.
* ✏️ Icono para editar.
* 🗑️ Icono para eliminar.
* 🔍 Icono de búsqueda.
* 🧹 Icono para limpiar.
* 🚪 Icono para cerrar sesión.

Estos recursos permiten mantener una identidad visual coherente en toda la aplicación.

---

## 🎨 Identidad visual

La aplicación mantiene una paleta inspirada en tonos suaves y relacionados con la identidad visual de BITE ME RESTAURANT.

| Color              | Código    | Uso                                |
| ------------------ | --------- | ---------------------------------- |
| 🫒 Matcha          | `#8E9546` | Menú y botones principales         |
| 🌱 Avocado Cream   | `#BBCA6F` | Encabezados y elementos destacados |
| 🌼 Wild Primrose   | `#E9E29B` | Fondo principal                    |
| 🌸 Tutu Bush       | `#F2CFBB` | Campos y barra de estado           |
| 🌷 Strawberry Milk | `#F1B4AF` | Elementos activos                  |
| 💗 Gamaron Pink    | `#F28892` | Acciones secundarias y eliminación |

---

## ⚡ Manejo de eventos

Uno de los conceptos principales de la Semana 15 es el **manejo de eventos**.

En Tkinter, un botón puede ejecutar una función cuando el usuario realiza una acción.

Por ejemplo:

```python
ttk.Button(
    contenedor,
    text='Registrar venta',
    command=self.registrar_venta
)
```

En este caso:

```text
Usuario
   ↓
Presiona "Registrar venta"
   ↓
command=self.registrar_venta
   ↓
Callback registrar_venta()
   ↓
RestauranteServicio
   ↓
Registro de la venta
   ↓
ventas.json
   ↓
Actualización de la interfaz
```

Es importante utilizar:

```python
command=self.registrar_venta
```

y no:

```python
command=self.registrar_venta()
```

porque `command=` debe recibir la referencia al método que será ejecutado cuando ocurra el evento.

---

## 🛍️ Gestión de ventas

La sección de ventas permite realizar una operación sencilla dentro del restaurante.

El proceso comienza cuando el usuario selecciona los datos necesarios desde la interfaz.

### 1️⃣ Selección del usuario

Se selecciona un usuario existente del sistema.

### 2️⃣ Selección del producto

Se selecciona un producto registrado en el menú.

### 3️⃣ Registrar venta

El usuario presiona el botón:

**🛒 Registrar venta**

Este botón utiliza `command=` para ejecutar el callback correspondiente.

### 4️⃣ Procesamiento

El callback obtiene la información seleccionada y solicita a `RestauranteServicio` que procese la operación.

### 5️⃣ Persistencia

La venta se guarda en:

```text
datos/ventas.json
```

### 6️⃣ Actualización

Finalmente, la interfaz actualiza la tabla de ventas para mostrar el nuevo registro.

---

## 🔄 Flujo general de la aplicación

```text
              🚀 INICIO
                  │
                  ▼
             🔐 LOGIN
                  │
                  ▼
       RestauranteServicio
                  │
                  ▼
          🖥️ PANEL PRINCIPAL
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     👤 USUARIOS 🍜 PRODUCTOS 🛍️ VENTAS
        │         │         │
        ▼         ▼         ▼
     Consulta   Gestión   Selección
                          usuario +
                          producto
                              │
                              ▼
                       🔘 Registrar venta
                              │
                              ▼
                           command=
                              │
                              ▼
                           Callback
                              │
                              ▼
                    RestauranteServicio
                              │
                              ▼
                        ventas.json
                              │
                              ▼
                     📋 Tabla de ventas
```

---

## 🧩 Separación de responsabilidades

El proyecto mantiene una separación clara entre la interfaz, la lógica y los datos.

```text
┌──────────────────────────────┐
│            UI                │
│     Tkinter / ttk            │
│                              │
│ Recibe acciones del usuario  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          SERVICIOS           │
│                              │
│ Reglas y lógica del sistema  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│            DATOS             │
│                              │
│        Archivos JSON         │
└──────────────────────────────┘
```

De esta manera, la interfaz no se encarga directamente de manipular los archivos JSON.

---

## 🖥️ Interfaz principal

La aplicación cuenta con una interfaz gráfica desarrollada con **Tkinter**.

La ventana principal utiliza una distribución con:

* 📌 Menú lateral.
* 🖼️ Logo.
* 👤 Información del usuario.
* 🏠 Inicio.
* 🍜 Productos.
* 👥 Usuarios.
* 🛍️ Ventas.
* 🚪 Cerrar sesión.
* 📊 Tablas para mostrar información.
* 🔘 Botones con iconos.
* 🎨 Estilos personalizados.

La aplicación mantiene una ventana principal de aproximadamente:

```text
960 × 600 píxeles
```

y cuenta con un tamaño mínimo para conservar una distribución adecuada.

---

## 🍜 Productos del restaurante

BITE ME RESTAURANT utiliza productos de comida coreana organizados por categorías.

Entre las categorías utilizadas se encuentran:

* 🍚 Platos Principales.
* 🥟 Entradas.
* 🍜 Sopas y Ramen.
* 🥤 Bebidas.
* 🍰 Postres.

Algunos productos registrados son:

| Código | Producto    | Categoría          | Precio |
| ------ | ----------- | ------------------ | -----: |
| P001   | Bibimbap    | Platos Principales |  $6.50 |
| P002   | Bulgogi     | Platos Principales |  $7.00 |
| P003   | Japchae     | Platos Principales |  $6.00 |
| E001   | Tteokbokki  | Entradas           |  $4.50 |
| E002   | Mandu       | Entradas           |  $4.00 |
| B001   | Banana Milk | Bebidas            |  $2.50 |
| D001   | Bingsu      | Postres            |  $2.75 |

---

## 👤 Usuarios

El sistema permite almacenar usuarios y utilizarlos para la autenticación y para relacionarlos con las operaciones de venta.

El inicio de sesión valida:

```text
Usuario + Contraseña
```

mediante:

```python
RestauranteServicio
```

Si las credenciales son correctas, el sistema permite acceder al panel principal.

---

## 💾 Persistencia de información

La aplicación utiliza archivos **JSON** para almacenar la información.

```text
📁 datos/
│
├── productos.json
├── usuarios.json
└── ventas.json
```

La lectura y escritura de los archivos se realiza mediante `ArchivoServicio`.

Esto permite conservar los registros cuando la aplicación se cierra y vuelve a ejecutarse.

---
## 🧠 Aprendizaje de la Semana 15

Durante esta semana se refuerza el conocimiento sobre el **manejo de eventos en interfaces gráficas**.

El concepto principal aprendido es que una acción realizada por el usuario puede generar una secuencia de operaciones dentro del sistema:

```text
Acción del usuario
        ↓
Evento
        ↓
command=
        ↓
Callback
        ↓
Servicio
        ↓
Persistencia
        ↓
Respuesta visual
```

También se refuerza la importancia de mantener separadas las responsabilidades de la interfaz, los servicios y los datos.

---

## 📌 Tecnologías utilizadas

* 🐍 **Python**
* 🖥️ **Tkinter**
* 🎨 **ttk**
* 🧩 **Programación Orientada a Objetos**
* 💾 **JSON**
* 📁 **Pathlib**
* 🖼️ **PNG**
* 🔧 **Git / GitHub**

---

## 👩‍💻 Autora

**Sofia Norelle Borja Heras**

🎓 Universidad Estatal Amazónica
💻 Tecnologías de la Información
📚 Programación Orientada a Objetos

---

# 🍜 BITE ME RESTAURANT 🇰🇷

### *Sabores que te atraparán a la primera mordida. ♥*

**Semana 15 — Conceptos fundamentales de manejo de eventos**

---
