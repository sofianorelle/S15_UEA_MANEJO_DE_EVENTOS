class Producto:

  def __init__(self, codigo, nombre, categoria, precio):
    self.codigo = codigo
    self.nombre = nombre
    self.categoria = categoria
    self.precio = precio

  @staticmethod
  def validar_texto(valor, campo):
    if not valor or not str(valor).strip():
      raise ValueError(f'El campo "{campo}" no puede estar vacío.')
    return str(valor).strip()

  @property
  def codigo(self):
    return self._codigo

  @codigo.setter
  def codigo(self, valor):
    self._codigo = self.validar_texto(valor, 'código')

  @property
  def nombre(self):
    return self._nombre

  @nombre.setter
  def nombre(self, valor):
    self._nombre = self.validar_texto(valor, 'nombre')

  @property
  def categoria(self):
    return self._categoria

  @categoria.setter
  def categoria(self, valor):
    self._categoria = self.validar_texto(valor, 'categoría')

  @property
  def precio(self):
    return self._precio

  @precio.setter
  def precio(self, valor):
    try:
      val = float(valor)
      if val < 0:
        raise ValueError
      self._precio = val
    except ValueError:
      raise ValueError('El precio debe ser un número mayor o igual a 0.')