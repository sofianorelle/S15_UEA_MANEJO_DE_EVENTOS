from datetime import date
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios_json = self.archivo_servicio.leer_json('usuarios.json')
        productos_json = self.archivo_servicio.leer_json('productos.json')
        ventas_json = self.archivo_servicio.leer_json('ventas.json')

        self.usuarios = []
        for datos in usuarios_json:
            try:
                u = Usuario(
                    datos.get('identificador', ''),
                    datos.get('nombre', ''),
                    datos.get('usuario', ''),
                    datos.get('contraseña', datos.get('contrasena', ''))
                )
                self.usuarios.append(u)
            except ValueError:
                continue

        self.productos = []
        for datos in productos_json:
            try:
                nombre_prod = datos.get('titulo', datos.get('nombre', ''))
                p = Producto(
                    datos.get('codigo', ''),
                    nombre_prod,
                    datos.get('categoria', ''),
                    datos.get('precio', 0.0)
                )
                self.productos.append(p)
            except ValueError:
                continue

        self.ventas = []
        for datos in ventas_json:
            try:
                v = Venta(
                    datos.get('identificador', ''),
                    datos.get('usuario_id', ''),
                    datos.get('producto_codigo', ''),
                    datos.get('fecha', '')
                )
                self.ventas.append(v)
            except ValueError:
                continue

    def validar_acceso(self, usuario, contrasena):
        for u in self.usuarios:
            if u.usuario == usuario and u.contrasena == contrasena:
                return u
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def cantidad_ventas(self):
        return len(self.ventas)

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def listar_ventas(self):
        return self.ventas

    def guardar_productos(self):
        datos = [
            {
                'codigo': p.codigo,
                'titulo': p.nombre,
                'categoria': p.categoria,
                'precio': f'{p.precio:.2f}'
            }
            for p in self.productos
        ]
        self.archivo_servicio.escribir_json('productos.json', datos)

    def buscar_producto_por_codigo(self, codigo):
        codigo = str(codigo).strip()
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def buscar_usuario_por_identificador(self, identificador):
        identificador = str(identificador).strip()
        for u in self.usuarios:
            if u.identificador == identificador:
                return u
        return None

    def registrar_producto(self, codigo, nombre, categoria, precio):
        nuevo = Producto(codigo, nombre, categoria, precio)
        if self.buscar_producto_por_codigo(nuevo.codigo) is not None:
            raise ValueError('Ya existe un producto con ese ID/Código.')
        self.productos.append(nuevo)
        self.guardar_productos()
        return nuevo

    def actualizar_producto(self, codigo, nombre, categoria, precio):
        prod = self.buscar_producto_por_codigo(codigo)
        if prod is None:
            raise ValueError('No existe un producto registrado con ese ID/Código.')
        datos_validados = Producto(codigo, nombre, categoria, precio)
        prod.nombre = datos_validados.nombre
        prod.categoria = datos_validados.categoria
        prod.precio = datos_validados.precio
        self.guardar_productos()
        return prod

    def eliminar_producto(self, codigo):
        prod = self.buscar_producto_por_codigo(codigo)
        if prod is None:
            raise ValueError('No existe un producto registrado con ese ID/Código.')
        self.productos.remove(prod)
        self.guardar_productos()
        return prod

    def generar_identificador_venta(self):
        siguiente = len(self.ventas) + 1
        return f"V{siguiente:03d}"

    def guardar_ventas(self):
        datos = [
            {
                "identificador": v.identificador,
                "usuario_id": v.usuario_id,
                "producto_codigo": v.producto_codigo,
                "fecha": v.fecha
            }
            for v in self.ventas
        ]
        self.archivo_servicio.escribir_json("ventas.json", datos)

    def registrar_venta(self, usuario_id, producto_codigo):
        usuario_id = str(usuario_id).strip()
        producto_codigo = str(producto_codigo).strip()

        if not usuario_id:
            raise ValueError("Debe seleccionar un usuario.")
        if not producto_codigo:
            raise ValueError("Debe seleccionar un producto.")

        if self.buscar_usuario_por_identificador(usuario_id) is None:
            raise ValueError("El usuario seleccionado no existe.")
        if self.buscar_producto_por_codigo(producto_codigo) is None:
            raise ValueError("El producto seleccionado no existe.")

        nueva_venta = Venta(
            self.generar_identificador_venta(),
            usuario_id,
            producto_codigo,
            date.today().isoformat()
        )
        self.ventas.append(nueva_venta)
        self.guardar_ventas()
        return nueva_venta