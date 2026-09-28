from pathlib import Path
import tkinter as tk
from tkinter import ttk


class LoginView(tk.Frame):

  def __init__(self, master, servicio, al_iniciar_sesion):
    super().__init__(master, bg='#E9E29B') 
    self.servicio = servicio
    self.al_iniciar_sesion = al_iniciar_sesion
    self.usuario_entry = None
    self.contrasena_entry = None
    self.mensaje_error = None
    self.logo = None
    self.definir_estilos()
    self.construir_interfaz()

  def definir_estilos(self):
    estilo = ttk.Style()
    estilo.theme_use('clam')
    estilo.configure(
        'Login.TButton',
        background='#8E9546',  
        foreground='#FFFFFF',
        font=('Arial', 11, 'bold'),
        padding=(14, 8),
        borderwidth=0,
    )
    estilo.map('Login.TButton', background=[('active', '#BBCA6F')])

  def cargar_logo(self):
    ruta_base = Path(__file__).resolve().parent.parent
    ruta_logo = ruta_base / 'assets' / 'logo' / 'logo.png'
    if not ruta_logo.exists():
      return None
    logo_original = tk.PhotoImage(file=str(ruta_logo))
    self.logo = logo_original.subsample(2, 2)
    return self.logo

  def construir_interfaz(self):
    contenedor = tk.Frame(self, bg='#FFFFFF', padx=32, pady=28)
    contenedor.place(relx=0.5, rely=0.5, anchor='center')

    logo = self.cargar_logo()
    if logo is not None:
      tk.Label(contenedor, image=logo, bg='#FFFFFF').pack(pady=(0, 12))

    tk.Label(
        contenedor,
        text='BITE ME RESTAURANT 🇰🇷',
        bg='#FFFFFF',
        fg='#8E9546',
        font=('Arial', 18, 'bold'),
    ).pack(pady=(0, 4))

    tk.Label(
        contenedor,
        text='Inicio de Sesión',
        bg='#FFFFFF',
        fg='#516173',
        font=('Arial', 11),
    ).pack(pady=(0, 18))

    tk.Label(
        contenedor,
        text='Usuario',
        bg='#FFFFFF',
        fg='#243447',
        font=('Arial', 10, 'bold'),
    ).pack(anchor='w')
    self.usuario_entry = tk.Entry(
        contenedor, width=30, font=('Arial', 11), bg='#F2CFBB', relief='flat'
    )
    self.usuario_entry.pack(pady=(4, 12), ipady=4)
    self.usuario_entry.focus()

    tk.Label(
        contenedor,
        text='Contraseña',
        bg='#FFFFFF',
        fg='#243447',
        font=('Arial', 10, 'bold'),
    ).pack(anchor='w')
    self.contrasena_entry = tk.Entry(
        contenedor,
        width=30,
        font=('Arial', 11),
        show='*',
        bg='#F2CFBB',
        relief='flat',
    )
    self.contrasena_entry.pack(pady=(4, 12), ipady=4)

    self.mensaje_error = tk.Label(
        contenedor, text='', bg='#FFFFFF', fg='#F28892', font=('Arial', 10)
    )
    self.mensaje_error.pack(pady=(0, 12))

    boton = ttk.Button(
        contenedor,
        text='Iniciar sesión',
        command=self.iniciar_sesion,
        style='Login.TButton',
    )
    boton.pack(fill='x')

  def iniciar_sesion(self):
    usuario = self.usuario_entry.get().strip()
    contrasena = self.contrasena_entry.get().strip()

    if not usuario or not contrasena:
      self.mensaje_error.config(text='Ingrese usuario y contraseña.')
      return

    usuario_validado = self.servicio.validar_acceso(usuario, contrasena)
    if usuario_validado is None:
      self.mensaje_error.config(text='Credenciales incorrectas.')
      return

    self.mensaje_error.config(text='')
    self.al_iniciar_sesion(usuario_validado)