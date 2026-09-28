from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

class MainView(tk.Frame):
    def __init__(self, master, servicio, usuario_actual, al_cerrar_sesion):
        super().__init__(master, bg='#E9E29B')
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion
        self.contenido = None
        self.etiqueta_estado = None
        self.botones_menu = {}
        self.imagenes_cache = {}
        
        # Formulario productos
        self.prod_codigo_entry = None
        self.prod_nombre_entry = None
        self.prod_categoria_combo = None
        self.prod_precio_entry = None
        self.tabla_productos = None
        self.tabla_usuarios = None
        
        # Formulario ventas (Semana 15)
        self.usuario_venta_combo = None
        self.producto_venta_combo = None
        self.tabla_ventas = None
        self.opciones_usuarios_venta = {}
        self.opciones_productos_venta = {}

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        self.MATCHA = '#8E9546'
        self.AVOCADO_CREAM = '#BBCA6F'
        self.WILD_PRIMROSE = '#E9E29B'
        self.TUTU_BUSH = '#F2CFBB'
        self.STRAWBERRY_MILK = '#F1B4AF'
        self.GAMARON_PINK = '#F28892'

        estilo = ttk.Style()
        estilo.theme_use('clam')

        # Estilos Menú Lateral
        estilo.configure(
            'MenuApp.TButton',
            background=self.MATCHA,
            foreground='#FFFFFF',
            font=('Arial', 10, 'bold'),
            padding=(12, 10),
            borderwidth=0,
            anchor='w'
        )
        estilo.map('MenuApp.TButton', background=[('active', self.AVOCADO_CREAM)])

        estilo.configure(
            'MenuActivo.TButton',
            background=self.STRAWBERRY_MILK,
            foreground='#FFFFFF',
            font=('Arial', 10, 'bold'),
            padding=(12, 10),
            borderwidth=0,
            anchor='w'
        )
        estilo.map('MenuActivo.TButton', background=[('active', self.GAMARON_PINK)])

        # Estilos Botones Formulario
        estilo.configure(
            'Accion.TButton',
            background=self.MATCHA,
            foreground='#FFFFFF',
            font=('Arial', 9, 'bold'),
            padding=(8, 6),
            borderwidth=0
        )
        estilo.map('Accion.TButton', background=[('active', self.AVOCADO_CREAM)])

        estilo.configure(
            'Secundario.TButton',
            background=self.STRAWBERRY_MILK,
            foreground='#FFFFFF',
            font=('Arial', 9, 'bold'),
            padding=(8, 6),
            borderwidth=0
        )
        estilo.map('Secundario.TButton', background=[('active', self.GAMARON_PINK)])

        estilo.configure(
            'Eliminar.TButton',
            background=self.GAMARON_PINK,
            foreground='#FFFFFF',
            font=('Arial', 9, 'bold'),
            padding=(8, 6),
            borderwidth=0
        )
        estilo.map('Eliminar.TButton', background=[('active', '#D66D77')])

        # Estilos Treeview
        estilo.configure(
            'Treeview.Heading',
            background=self.AVOCADO_CREAM,
            foreground='#FFFFFF',
            font=('Arial', 10, 'bold')
        )
        estilo.configure(
            'Treeview',
            background='#FFFFFF',
            fieldbackground='#FFFFFF',
            rowheight=24
        )
        estilo.map(
            'Treeview',
            background=[('selected', self.STRAWBERRY_MILK)],
            foreground=[('selected', '#333333')]
        )

    def obtener_imagen(self, subcarpeta, nombre_archivo, escala=1):
        clave = f'{subcarpeta}_{nombre_archivo}_{escala}'
        if clave in self.imagenes_cache:
            return self.imagenes_cache[clave]

        ruta_base = Path(__file__).resolve().parent.parent
        ruta_img = ruta_base / 'assets' / subcarpeta / nombre_archivo
        if not ruta_img.exists():
            return None

        img = tk.PhotoImage(file=str(ruta_img))
        if escala > 1:
            img = img.subsample(escala, escala)
        self.imagenes_cache[clave] = img
        return img

    def crear_boton(self, contenedor, texto, comando, estilo, icono=None):
        imagen = self.obtener_imagen('icons', icono) if icono else None
        if imagen:
            return ttk.Button(
                contenedor,
                text=texto,
                command=comando,
                style=estilo,
                image=imagen,
                compound='left'
            )
        return ttk.Button(contenedor, text=texto, command=comando, style=estilo)

    def construir_interfaz(self):
        frame_sidebar = tk.Frame(self, bg=self.MATCHA, width=200, padx=16, pady=18)
        frame_sidebar.pack(side='left', fill='y')
        frame_sidebar.pack_propagate(False)

        header_sidebar = tk.Frame(frame_sidebar, bg=self.MATCHA)
        header_sidebar.pack(fill='x', pady=(0, 6))

        logo2_img = self.obtener_imagen('logo', 'logo2.png', escala=4)
        if logo2_img:
            lbl_logo2 = tk.Label(header_sidebar, image=logo2_img, bg=self.MATCHA)
            lbl_logo2.pack(side='left', anchor='w')

        info_user_frame = tk.Frame(header_sidebar, bg=self.MATCHA)
        info_user_frame.pack(side='left', fill='both', expand=True, padx=(8, 0))

        tk.Label(
            info_user_frame,
            text=f'Usuario:\n{self.usuario_actual.nombre}',
            bg=self.MATCHA,
            fg=self.WILD_PRIMROSE,
            font=('Arial', 12, 'bold'),
            justify='left'
        ).pack(anchor='w', pady=(2, 0))

        tk.Frame(frame_sidebar, bg=self.AVOCADO_CREAM, height=3).pack(fill='x', pady=(10, 16))

        self.crear_boton_menu(frame_sidebar, 'Inicio', self.mostrar_inicio, 'home.png')
        self.crear_boton_menu(frame_sidebar, 'Productos', self.mostrar_productos, 'productos.png')
        self.crear_boton_menu(frame_sidebar, 'Usuarios', self.mostrar_usuarios, 'users.png')
        self.crear_boton_menu(frame_sidebar, 'Ventas', self.mostrar_ventas, 'sales.png')

        tk.Frame(frame_sidebar, bg=self.MATCHA).pack(fill='both', expand=True)

        self.crear_boton(
            frame_sidebar,
            'Cerrar sesión',
            self.cerrar_sesion,
            'Eliminar.TButton',
            'logout.png'
        ).pack(fill='x', pady=(16, 0))

        # Área principal
        frame_principal = tk.Frame(self, bg=self.WILD_PRIMROSE)
        frame_principal.pack(side='left', fill='both', expand=True)

        header_top = tk.Frame(frame_principal, bg=self.AVOCADO_CREAM, padx=28, pady=12)
        header_top.pack(fill='x')

        icono_app_img = self.obtener_imagen('logo', 'icono.png', escala=3)
        if icono_app_img:
            lbl_icono_top = tk.Label(header_top, image=icono_app_img, bg=self.AVOCADO_CREAM)
            lbl_icono_top.pack(side='left')
        else:
            tk.Label(
                header_top,
                text='BITE ME RESTAURANT KR',
                bg=self.AVOCADO_CREAM,
                fg='#FFFFFF',
                font=('Arial', 18, 'bold')
            ).pack(side='left')

        tk.Label(
            header_top,
            text='Sabores que te atraparán a la primera mordida.❤',
            bg=self.AVOCADO_CREAM,
            fg='#FFFFFF',
            font=('Arial', 11, 'italic')
        ).pack(side='right', anchor='e')

        self.contenido = tk.Frame(frame_principal, bg=self.WILD_PRIMROSE, padx=28, pady=10)
        self.contenido.pack(fill='both', expand=True)

        barra_estado = tk.Frame(frame_principal, bg=self.TUTU_BUSH, padx=18, pady=6)
        barra_estado.pack(fill='x', side='bottom')

        self.etiqueta_estado = tk.Label(
            barra_estado,
            bg=self.TUTU_BUSH,
            fg='#243447',
            font=('Arial', 9, 'bold')
        )
        self.etiqueta_estado.pack(side='left')

        self.mostrar_inicio()

    def crear_boton_menu(self, contenedor, texto, comando, icono):
        boton = self.crear_boton(contenedor, texto, comando, 'MenuApp.TButton', icono)
        boton.pack(fill='x', pady=(0, 8))
        self.botones_menu[texto] = boton

    def marcar_seccion(self, seccion):
        for texto, boton in self.botones_menu.items():
            estilo = 'MenuActivo.TButton' if texto == seccion else 'MenuApp.TButton'
            boton.configure(style=estilo)

    def limpiar_contenido(self):
        self.tabla_productos = None
        self.tabla_usuarios = None
        self.tabla_ventas = None
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def actualizar_barra_estado(self):
        if self.etiqueta_estado and self.etiqueta_estado.winfo_exists():
            self.etiqueta_estado.config(
                text=(
                    f'Productos: {self.servicio.cantidad_productos()} | '
                    f'Usuarios: {self.servicio.cantidad_usuarios()} | '
                    f'Ventas: {self.servicio.cantidad_ventas()} | '
                    'Persistencia: JSON'
                )
            )

    # Vista Inicio (Ajustado: Texto en una sola línea)
    def mostrar_inicio(self):
        self.marcar_seccion('Inicio')
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text='Panel Principal',
            bg=self.WILD_PRIMROSE,
            fg=self.MATCHA,
            font=('Arial', 20, 'bold')
        ).pack(anchor='w', pady=(0, 6))

        tk.Label(
            self.contenido,
            text='Bienvenido/a al sistema de gestión de BITE ME RESTAURANT. Seleccione una opción del menú lateral.',
            bg=self.WILD_PRIMROSE,
            fg='#444444',
            font=('Arial', 11)
        ).pack(anchor='w', pady=(0, 20))

        resumen = tk.Frame(self.contenido, bg=self.WILD_PRIMROSE)
        resumen.pack(fill='x')

        self.crear_tarjeta_resumen(resumen, 'Productos en Menú', self.servicio.cantidad_productos())
        self.crear_tarjeta_resumen(resumen, 'Usuarios del Sistema', self.servicio.cantidad_usuarios())
        self.crear_tarjeta_resumen(resumen, 'Ventas Registradas', self.servicio.cantidad_ventas())

        self.actualizar_barra_estado()

    def crear_tarjeta_resumen(self, contenedor, titulo, valor):
        tarjeta = tk.Frame(contenedor, bg='#FFFFFF', padx=20, pady=18, relief='groove', bd=1)
        tarjeta.pack(side='left', fill='x', expand=True, padx=(0, 14))

        tk.Label(
            tarjeta,
            text=titulo,
            bg='#FFFFFF',
            fg='#555555',
            font=('Arial', 11, 'bold')
        ).pack(anchor='w')

        tk.Label(
            tarjeta,
            text=str(valor),
            bg='#FFFFFF',
            fg=self.MATCHA,
            font=('Arial', 26, 'bold')
        ).pack(anchor='w', pady=(8, 0))

    # Vista Usuarios
    def mostrar_usuarios(self):
        self.marcar_seccion('Usuarios')
        self.limpiar_contenido()

        header_frame = tk.Frame(self.contenido, bg=self.WILD_PRIMROSE)
        header_frame.pack(anchor='w', pady=(0, 12))

        tk.Label(
            header_frame,
            text='Usuarios Registrados',
            bg=self.WILD_PRIMROSE,
            fg=self.MATCHA,
            font=('Arial', 18, 'bold')
        ).pack(side='left')

        listado = tk.LabelFrame(
            self.contenido,
            text=' Consulta de Usuarios',
            bg='#FFFFFF',
            fg=self.MATCHA,
            font=('Arial', 10, 'bold'),
            padx=12,
            pady=12
        )
        listado.pack(fill='both', expand=True)

        self.tabla_usuarios = self.crear_tabla(
            listado,
            ('identificador', 'nombre', 'usuario'),
            ('Identificador', 'Nombre', 'Usuario')
        )
        self.refrescar_usuarios()

    def refrescar_usuarios(self):
        if self.tabla_usuarios and self.tabla_usuarios.winfo_exists():
            self.limpiar_tabla(self.tabla_usuarios)
            for u in self.servicio.listar_usuarios():
                self.tabla_usuarios.insert(
                    '', tk.END, values=(u.identificador, u.nombre, u.usuario)
                )
        self.actualizar_barra_estado()

    # Vista Productos
    def mostrar_productos(self):
        self.marcar_seccion('Productos')
        self.limpiar_contenido()

        header_frame = tk.Frame(self.contenido, bg=self.WILD_PRIMROSE)
        header_frame.pack(anchor='w', pady=(0, 10))

        tk.Label(
            header_frame,
            text='Gestión de Productos',
            bg=self.WILD_PRIMROSE,
            fg=self.MATCHA,
            font=('Arial', 18, 'bold')
        ).pack(side='left')

        form_frame = tk.LabelFrame(
            self.contenido,
            text=' Formulario de Producto',
            bg='#FFFFFF',
            fg=self.MATCHA,
            font=('Arial', 10, 'bold'),
            padx=14,
            pady=10
        )
        form_frame.pack(fill='x', pady=(0, 14))

        tk.Label(form_frame, text='ID/Código:', bg='#FFFFFF', fg='#333333', font=('Arial', 9, 'bold')).grid(row=0, column=0, sticky='w', padx=(0, 5), pady=4)
        self.prod_codigo_entry = tk.Entry(form_frame, width=18, bg=self.TUTU_BUSH)
        self.prod_codigo_entry.grid(row=0, column=1, sticky='w', padx=(0, 25), pady=4)

        tk.Label(form_frame, text='Nombre:', bg='#FFFFFF', fg='#333333', font=('Arial', 9, 'bold')).grid(row=0, column=2, sticky='w', padx=(0, 5), pady=4)
        self.prod_nombre_entry = tk.Entry(form_frame, width=28, bg=self.TUTU_BUSH)
        self.prod_nombre_entry.grid(row=0, column=3, sticky='w', pady=4)

        tk.Label(form_frame, text='Categoría:', bg='#FFFFFF', fg='#333333', font=('Arial', 9, 'bold')).grid(row=1, column=0, sticky='w', padx=(0, 5), pady=4)
        self.prod_categoria_combo = ttk.Combobox(
            form_frame,
            values=['Platos Principales', 'Entradas', 'Sopas y Ramen', 'Bebidas', 'Postres'],
            state='readonly',
            width=16
        )
        self.prod_categoria_combo.set('Platos Principales')
        self.prod_categoria_combo.grid(row=1, column=1, sticky='w', padx=(0, 25), pady=4)

        tk.Label(form_frame, text='Precio ($):', bg='#FFFFFF', fg='#333333', font=('Arial', 9, 'bold')).grid(row=1, column=2, sticky='w', padx=(0, 5), pady=4)
        self.prod_precio_entry = tk.Entry(form_frame, width=18, bg=self.TUTU_BUSH)
        self.prod_precio_entry.grid(row=1, column=3, sticky='w', pady=4)

        acciones_frame = tk.Frame(form_frame, bg='#FFFFFF')
        acciones_frame.grid(row=2, column=0, columnspan=4, sticky='ew', pady=(12, 4))

        botones = (
            ('Guardar / Registrar', self.registrar_producto, 'Accion.TButton', 'add.png'),
            ('Cargar por ID', self.cargar_producto_en_formulario, 'Secundario.TButton', 'search.png'),
            ('Actualizar', self.actualizar_producto, 'Secundario.TButton', 'edit.png'),
            ('Eliminar', self.eliminar_producto, 'Eliminar.TButton', 'delete.png'),
            ('Limpiar', self.limpiar_formulario_producto, 'Secundario.TButton', 'clean.png')
        )

        for texto, comando, estilo, icono in botones:
            btn = self.crear_boton(acciones_frame, texto, comando, estilo, icono)
            btn.pack(side='left', padx=(0, 8))

        listado_frame = tk.LabelFrame(
            self.contenido,
            text=' Lista de Productos Registrados',
            bg='#FFFFFF',
            fg=self.MATCHA,
            font=('Arial', 10, 'bold'),
            padx=12,
            pady=10
        )
        listado_frame.pack(fill='both', expand=True)

        self.tabla_productos = self.crear_tabla(
            listado_frame,
            ('codigo', 'nombre', 'categoria', 'precio'),
            ('ID/Código', 'Nombre del Producto', 'Categoría', 'Precio ($)')
        )
        self.refrescar_productos()

    def obtener_datos_producto(self):
        return (
            self.prod_codigo_entry.get(),
            self.prod_nombre_entry.get(),
            self.prod_categoria_combo.get(),
            self.prod_precio_entry.get()
        )

    def registrar_producto(self):
        try:
            self.servicio.registrar_producto(*self.obtener_datos_producto())
            self.limpiar_formulario_producto()
            self.refrescar_productos()
            messagebox.showinfo('Productos', 'Producto registrado correctamente.')
        except ValueError as error:
            messagebox.showerror('Error', str(error))

    def cargar_producto_en_formulario(self):
        codigo = self.prod_codigo_entry.get().strip()
        prod = self.servicio.buscar_producto_por_codigo(codigo)
        if prod is None:
            messagebox.showerror('Error', 'No existe un producto con ese ID/Código.')
            return
        self.limpiar_formulario_producto()
        self.prod_codigo_entry.insert(0, prod.codigo)
        self.prod_nombre_entry.insert(0, prod.nombre)
        self.prod_categoria_combo.set(prod.categoria)
        self.prod_precio_entry.insert(0, str(prod.precio))

    def actualizar_producto(self):
        try:
            self.servicio.actualizar_producto(*self.obtener_datos_producto())
            self.refrescar_productos()
            messagebox.showinfo('Productos', 'Producto actualizado correctamente.')
        except ValueError as error:
            messagebox.showerror('Error', str(error))

    def eliminar_producto(self):
        try:
            codigo = self.prod_codigo_entry.get().strip()
            self.servicio.eliminar_producto(codigo)
            self.limpiar_formulario_producto()
            self.refrescar_productos()
            messagebox.showinfo('Productos', 'Producto eliminado correctamente.')
        except ValueError as error:
            messagebox.showerror('Error', str(error))

    def limpiar_formulario_producto(self):
        for entrada in (self.prod_codigo_entry, self.prod_nombre_entry, self.prod_precio_entry):
            if entrada is not None and entrada.winfo_exists():
                entrada.delete(0, tk.END)
        if self.prod_categoria_combo is not None and self.prod_categoria_combo.winfo_exists():
            self.prod_categoria_combo.set('Platos Principales')

    def refrescar_productos(self):
        if self.tabla_productos and self.tabla_productos.winfo_exists():
            self.limpiar_tabla(self.tabla_productos)
            for p in self.servicio.listar_productos():
                self.tabla_productos.insert(
                    '', tk.END, values=(p.codigo, p.nombre, p.categoria, f'${p.precio:.2f}')
                )
        self.actualizar_barra_estado()

    # Vista Ventas (Ajustado: Desplegables inician en blanco)
    def mostrar_ventas(self):
        self.marcar_seccion('Ventas')
        self.limpiar_contenido()

        header_frame = tk.Frame(self.contenido, bg=self.WILD_PRIMROSE)
        header_frame.pack(anchor='w', pady=(0, 10))

        tk.Label(
            header_frame,
            text='Registro de Ventas',
            bg=self.WILD_PRIMROSE,
            fg=self.MATCHA,
            font=('Arial', 18, 'bold')
        ).pack(side='left')

        cuerpo = tk.Frame(self.contenido, bg=self.WILD_PRIMROSE)
        cuerpo.pack(fill='both', expand=True)

        # Formulario Venta
        form_frame = tk.LabelFrame(
            cuerpo,
            text=' Nueva Venta ',
            bg='#FFFFFF',
            fg=self.MATCHA,
            font=('Arial', 10, 'bold'),
            padx=14,
            pady=12
        )
        form_frame.pack(side='left', fill='y', padx=(0, 14))

        tk.Label(form_frame, text='Usuario:', bg='#FFFFFF', fg='#333333', font=('Arial', 9, 'bold')).pack(anchor='w', pady=(0, 4))
        
        opciones_usr = self.obtener_opciones_usuarios_venta()
        self.usuario_venta_combo = ttk.Combobox(
            form_frame,
            values=list(opciones_usr.keys()),
            state='readonly',
            width=28
        )
        self.usuario_venta_combo.pack(fill='x', pady=(0, 12))
        self.usuario_venta_combo.set('')  # Se deja en blanco al iniciar

        tk.Label(form_frame, text='Producto:', bg='#FFFFFF', fg='#333333', font=('Arial', 9, 'bold')).pack(anchor='w', pady=(0, 4))
        
        opciones_prod = self.obtener_opciones_productos_venta()
        self.producto_venta_combo = ttk.Combobox(
            form_frame,
            values=list(opciones_prod.keys()),
            state='readonly',
            width=28
        )
        self.producto_venta_combo.pack(fill='x', pady=(0, 16))
        self.producto_venta_combo.set('')  # Se deja en blanco al iniciar

        btn_registrar = self.crear_boton(
            form_frame,
            'Registrar venta',
            self.registrar_venta,
            'Accion.TButton',
            'add.png'
        )
        btn_registrar.pack(fill='x')

        # Tabla de Ventas
        listado_frame = tk.LabelFrame(
            cuerpo,
            text=' Historial de Ventas Registradas ',
            bg='#FFFFFF',
            fg=self.MATCHA,
            font=('Arial', 10, 'bold'),
            padx=12,
            pady=10
        )
        listado_frame.pack(side='left', fill='both', expand=True)

        self.tabla_ventas = self.crear_tabla(
            listado_frame,
            ('identificador', 'usuario', 'producto', 'fecha'),
            ('Venta', 'Usuario', 'Producto', 'Fecha')
        )
        self.refrescar_ventas()

    def obtener_opciones_usuarios_venta(self):
        self.opciones_usuarios_venta = {
            f"{u.identificador} - {u.nombre}": u.identificador
            for u in self.servicio.listar_usuarios()
        }
        return self.opciones_usuarios_venta

    def obtener_opciones_productos_venta(self):
        self.opciones_productos_venta = {
            f"{p.codigo} - {p.nombre} (${p.precio:.2f})": p.codigo
            for p in self.servicio.listar_productos()
        }
        return self.opciones_productos_venta

    def registrar_venta(self):
        seleccion_usr = self.usuario_venta_combo.get()
        seleccion_prod = self.producto_venta_combo.get()

        if not seleccion_usr or not seleccion_prod:
            messagebox.showerror('Error', 'Debe seleccionar un usuario y un producto.')
            return

        usuario_id = self.opciones_usuarios_venta.get(seleccion_usr)
        producto_codigo = self.opciones_productos_venta.get(seleccion_prod)

        try:
            self.servicio.registrar_venta(usuario_id, producto_codigo)
            self.limpiar_formulario_venta()  # Se limpian las selecciones a blanco tras el registro
            self.refrescar_ventas()
            messagebox.showinfo('Ventas', 'Venta registrada con éxito.')
        except ValueError as error:
            messagebox.showerror('Error', str(error))

    def limpiar_formulario_venta(self):
        if self.usuario_venta_combo is not None and self.usuario_venta_combo.winfo_exists():
            self.usuario_venta_combo.set('')
        if self.producto_venta_combo is not None and self.producto_venta_combo.winfo_exists():
            self.producto_venta_combo.set('')

    def refrescar_ventas(self):
        if self.tabla_ventas and self.tabla_ventas.winfo_exists():
            self.limpiar_tabla(self.tabla_ventas)
            for v in self.servicio.listar_ventas():
                usr = self.servicio.buscar_usuario_por_identificador(v.usuario_id)
                prod = self.servicio.buscar_producto_por_codigo(v.producto_codigo)

                nombre_usr = usr.nombre if usr else v.usuario_id
                nombre_prod = prod.nombre if prod else v.producto_codigo

                self.tabla_ventas.insert(
                    '', tk.END, values=(v.identificador, nombre_usr, nombre_prod, v.fecha)
                )
        self.actualizar_barra_estado()

    # Helpers
    def crear_tabla(self, contenedor, columnas, encabezados):
        frame_tabla = tk.Frame(contenedor, bg='#FFFFFF')
        frame_tabla.pack(fill='both', expand=True)

        tabla = ttk.Treeview(frame_tabla, columns=columnas, show='headings', height=10)
        barra = ttk.Scrollbar(frame_tabla, orient='vertical', command=tabla.yview)
        tabla.configure(yscrollcommand=barra.set)

        for col, enc in zip(columnas, encabezados):
            tabla.heading(col, text=enc)
            tabla.column(col, width=130 if col in ('identificador', 'codigo', 'fecha') else 180, anchor='center' if col in ('identificador', 'codigo') else 'w')

        tabla.pack(side='left', fill='both', expand=True)
        barra.pack(side='right', fill='y')
        return tabla

    def limpiar_tabla(self, tabla):
        if tabla and tabla.winfo_exists():
            for item in tabla.get_children():
                tabla.delete(item)

    def cerrar_sesion(self):
        self.al_cerrar_sesion()