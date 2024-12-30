import tkinter as tk
from tkinter import *
from tkinter import ttk  
from circular import listacirculardoble
from vehiculos import ArbolB, Vehiculos
from rutas import Rutas, ListaAdyacencia, Lista
from Viajes import LinkedList

linked = LinkedList()
lcde = listacirculardoble()
arbolb=ArbolB(5)
ady = ListaAdyacencia()


class Myapp(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.bg_menubar = 'lightblue'
        self.fg_menubar = 'black'
        self.active_menubar = '#dedede'
        self.active_fg_menubar = 'black'
        self.bg_menu = '#f3f4f5'
        self.fg_menus = 'black'
        self.active_bg_menus = '#bcdff2'
        self.active_fg_menus = 'black'

        self.bg_app = '#1f1f1f'

        super().__init__(root, bg=self.bg_app)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.root.option_add('*tearOff', tk.FALSE)
        self.ventanaclientes1 = None  # Inicializamos la variable para la ventana secundaria
        self.ventanaclientes2 = None
        self.ventanaclientes3 = None
        self.ventanaclientes4 = None
        self.ventanavehiculos1 = None
        self.ventanavehiculos2 = None
        self.ventanavehiculos3 = None
        self.ventanavehiculos4 = None
        self.ventanarutas = None
        self.ventanarutas2 = None
        self.ventanaviajes1 = None
        self.ventanaviajes2 = None
        self.ventanaviajes3 = None
        self.ventanareportes1 = None
        self.create_menubar()

    def create_menubar(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.clientes = tk.Menu(self.menubar)
        self.viajes = tk.Menu(self.menubar)
        self.rutas = tk.Menu(self.menubar)
        self.vehiculos = tk.Menu(self.menubar)
        self.reportes = tk.Menu(self.menubar)

        self.menubar.add_cascade(label='Clientes', menu=self.clientes)
        self.menubar.add_cascade(label='Viajes', menu=self.viajes)
        self.menubar.add_cascade(label='Rutas', menu=self.rutas)
        self.menubar.add_cascade(label='Vehiculos', menu=self.vehiculos)
        self.menubar.add_cascade(label='Reportes', menu=self.reportes)

        self.add_clientes_items()
        self.add_vehiculos_items()
        self.add_rutas_items()
        self.add_viajes_items()
        self.add_reportes_items()

    #aqui esta todo lo de clientes --------------------------------------------------------------------------------------------------
    #sub lista en el menu de clientes
    def add_clientes_items(self):
        self.clientes.add_command(label='Agregar cliente', command=self.agregarc_ventana)
        self.clientes.add_command(label='Modificar/Eliminar cliente', command=self.modificarc_ventana)
        self.clientes.add_command(label='Mostrar cliente', command=self.mostrarc_ventana)
        self.clientes.add_command(label='Generar grafico', command=self.graficoc_ventana)
    
    #sub lista en el menu de vehiculos
    def add_vehiculos_items(self):
        self.vehiculos.add_command(label='Agregar Vehiculo', command=self.agregarv_ventana)
        self.vehiculos.add_command(label='Modificar/Eliminar Vehiculo', command=self.modificarv_ventana)
        self.vehiculos.add_command(label='Mostrar Vehiculo', command=self.mostrarv_ventana)
        self.vehiculos.add_command(label='Generar grafico', command=self.graficov_ventana)
    
    #sub lista en el menu de rutas
    def add_rutas_items(self):
        self.rutas.add_command(label='Cargar Rutas', command=self.cargarrutas_ventana)
        self.rutas.add_command(label='Generar grafico', command=self.graficor_ventana)
    
    #sub lista en el menu de viajes
    def add_viajes_items(self):
        self.viajes.add_command(label='Agregar Viaje', command=self.agregarviaje_ventana)
        self.viajes.add_command(label='Mostrar Viaje', command=self.mostrarviaje_ventana)
        self.viajes.add_command(label='Generar grafico', command=self.graficarviaje_ventana)

    def add_reportes_items(self):
        self.reportes.add_command(label='top 5 viajes mas largos', command=self.reportes1_ventana)
        self.reportes.add_command(label='top 5 viajes mas caros')
        self.reportes.add_command(label='top 5 clientes con mayor cantidad de viajes')
        self.reportes.add_command(label='top 5 vehiculos con mayor cantidad de viajes')
        self.reportes.add_command(label='Ruta de un viaje')


#------------------------------------------------------------------------------------------------------------------------------

    #ventana de agregar cliente
    def agregarc_ventana(self):
        if self.ventanaclientes1 is None or not self.ventanaclientes1.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanaclientes1 = tk.Toplevel(self.root)
            self.ventanaclientes1.title('Agregar Cliente')
            self.ventanaclientes1.geometry('400x500')
            self.create_widgets_in_ventanaclientes()
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaclientes1.deiconify()


    #ventana para mostrar
    def mostrarc_ventana(self):
        if self.ventanaclientes4 is None or not self.ventanaclientes4.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanaclientes4 = tk.Toplevel(self.root)
            self.ventanaclientes4.title('Mostrar Cliente')
            self.create_widgets_in_ventanaclientesmostrar()
            self.ventanaclientes4.geometry('400x500')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaclientes4.deiconify()

    #ventana para modificar
    def modificarc_ventana(self):
        if self.ventanaclientes2 is None or not self.ventanaclientes2.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanaclientes2 = tk.Toplevel(self.root)
            self.ventanaclientes2.title('Modificar/Eliminar Cliente')
            self.create_widgets_in_ventanaclientesmodificar()
            self.ventanaclientes2.geometry('400x500')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaclientes2.deiconify()
    #ventana para generar y ver el grafico de la estructura
    def graficoc_ventana(self):
        if self.ventanaclientes3 is None or not self.ventanaclientes3.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanaclientes3 = tk.Toplevel(self.root)
            self.ventanaclientes3.title('Grafico Clientes')
            self.create_widgets_in_ventanaclientesgrafico()
            self.ventanaclientes3.geometry('700x700')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaclientes3.deiconify()
    
    #------------------------------------------------------------------------------------------------------------------------------

    #ventana de agregar vehiculo
    def agregarv_ventana(self):
        if self.ventanavehiculos1 is None or not self.ventanavehiculos1.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanavehiculos1 = tk.Toplevel(self.root)
            self.ventanavehiculos1.title('Agregar Vehiculo')
            self.ventanavehiculos1.geometry('400x500')
            self.create_widgets_in_ventanavehiculos()
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanavehiculos1.deiconify()


    #ventana para mostrar
    def mostrarv_ventana(self):
        if self.ventanavehiculos2 is None or not self.ventanavehiculos2.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanavehiculos2 = tk.Toplevel(self.root)
            self.ventanavehiculos2.title('Mostrar Vehiculo')
            self.create_widgets_in_ventanavehiculosmodificar()
            self.ventanavehiculos2.geometry('400x500')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanavehiculos2.deiconify()

    #ventana para modificar
    def modificarv_ventana(self):
        if self.ventanavehiculos3 is None or not self.ventanavehiculos3.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanavehiculos3 = tk.Toplevel(self.root)
            self.ventanavehiculos3.title('Modificar/Eliminar Vehiculo')
            self.create_widgets_in_ventanavehiculosmodificar()
            self.ventanavehiculos3.geometry('400x500')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanavehiculos3.deiconify()
    #ventana para generar y ver el grafico de la estructura
    def graficov_ventana(self):
        if self.ventanavehiculos4 is None or not self.ventanavehiculos4.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanavehiculos4 = tk.Toplevel(self.root)
            self.ventanavehiculos4.title('Grafico Vehiculos')
            self.create_widgets_in_ventanavehiculosgrafico()
            self.ventanavehiculos4.geometry('700x700')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanavehiculos4.deiconify()
    
    #------------------------------------------------------------------------------------------------------------------------------

    def cargarrutas_ventana(self):
        if self.ventanarutas is None or not self.ventanarutas.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanarutas = tk.Toplevel(self.root)
            self.ventanarutas.title('Cargar Rutas')
            self.ventanarutas.geometry('400x500')
            self.create_widgets_in_ventanarutas()
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanarutas.deiconify()
    
    def graficor_ventana(self):
        if self.ventanarutas2 is None or not self.ventanarutas2.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanarutas2 = tk.Toplevel(self.root)
            self.ventanarutas2.title('Grafico Rutas')
            self.ventanarutas2.geometry('700x700')
            self.create_widgets_in_ventanarutas2()
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanarutas2.deiconify()

    
    #------------------------------------------------------------------------------------------------------------------------------

    def agregarviaje_ventana(self):
        if self.ventanaviajes1 is None or not self.ventanaviajes1.winfo_exists():
          
            self.ventanaviajes1 = tk.Toplevel(self.root)
            self.ventanaviajes1.title('Agregar Viaje')
            self.ventanaviajes1.geometry('400x500')
            self.create_widgets_in_ventanaviajes()
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaviajes1.deiconify()
    
    def mostrarviaje_ventana(self):
        if self.ventanaviajes2 is None or not self.ventanaviajes2.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanaviajes2 = tk.Toplevel(self.root)
            self.ventanaviajes2.title('Mostrar Viaje')
            self.create_widgets_in_ventanaviajesmostrar()
            self.ventanaviajes2.geometry('400x500')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaviajes2.deiconify()
    
    def graficarviaje_ventana(self):
        if self.ventanaviajes3 is None or not self.ventanaviajes3.winfo_exists():
            # Crear la ventana secundaria si no existe
            self.ventanaviajes3 = tk.Toplevel(self.root)
            self.ventanaviajes3.title('Grafico Viajes')
            self.create_widgets_in_ventanaviajesgrafico()
            self.ventanaviajes3.geometry('700x700')
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanaviajes3.deiconify()
    #------------------------------------------------------------------------------------------------------------------------------

    def reportes1_ventana(self):
        if self.ventanareportes1 is None or not self.ventanareportes1.winfo_exists():
            self.ventanareportes1 = tk.Toplevel(self.root)
            self.ventanareportes1.title('Top 5 Viajes mas largos')
            self.ventanareportes1.geometry('400x500')
            self.create_widgets_in_ventanareportes1()
        else:
            # Si la ventana ya existe, simplemente la mostramos
            self.ventanareportes1.deiconify()

    #------------------------------------------------------------------------------------------------------------------------------
    
    #obtener los datos del cliente para agregarlo
    def data_cliente(self):
        dpi = self.dpi_entry.get()
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        genero = self.genero_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()
        lcde.agregar_cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        self.dpi_entry.delete(0, tk.END)
        self.nombres_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

    def carga_cliente(self):
        ruta = self.ruta.get()
        lcde.leer_ruta_archivo(ruta)
        self.ruta.delete(0, tk.END)

    #para mostrar los datos del cliente
    def print_data_cliente(self):
        dpi = self.dpi_mostrar.get()
        cliente = lcde.mostrar_cliente(dpi)
        if cliente:
            # Habilitar temporalmente las cajas de texto para escribir
            self.nombres_mostrar.config(state='normal')
            self.nombres_mostrar.delete(0, tk.END)
            self.nombres_mostrar.insert(0, cliente.nombre)
            self.nombres_mostrar.config(state='disabled')  # Volver a inhabilitar

            self.apellidos_mostrar.config(state='normal')
            self.apellidos_mostrar.delete(0, tk.END)
            self.apellidos_mostrar.insert(0, cliente.apellido)
            self.apellidos_mostrar.config(state='disabled')

            self.genero_mostrar.set(cliente.genero)  # Para ComboBox

            self.telefono_mostrar.config(state='normal')
            self.telefono_mostrar.delete(0, tk.END)
            self.telefono_mostrar.insert(0, cliente.telefono)
            self.telefono_mostrar.config(state='disabled')

            self.direccion_mostrar.config(state='normal')
            self.direccion_mostrar.delete(0, tk.END)
            self.direccion_mostrar.insert(0, cliente.direccion)
            self.direccion_mostrar.config(state='disabled')
        else:
            print("Cliente no encontrado")

    def buscar_modificar(self):
        dpi = self.dpi_modb.get()

        cliente = lcde.mostrar_cliente(dpi)
        if cliente:
            # Habilitar temporalmente las cajas de texto para escribir
            self.dpi_mod.config(state='normal')
            self.dpi_mod.delete(0, tk.END)
            self.dpi_mod.insert(0, cliente.dpi)
            self.dpi_mod.config(state='disabled')  # Volver a inhabilitar           
            self.apellidos_mod.delete(0, tk.END)
            self.apellidos_mod.insert(0, cliente.apellido)
            self.genero_mod.set(cliente.genero)  # Para ComboBox
            self.nombres_mod.delete(0, tk.END)
            self.nombres_mod.insert(0, cliente.nombre)
            self.telefono_mod.delete(0, tk.END)
            self.telefono_mod.insert(0, cliente.telefono)          
            self.direccion_mod.delete(0, tk.END)
            self.direccion_mod.insert(0, cliente.direccion)
        else:
            print("Cliente no encontrado")

    def modificar_cliente(self):
        dpi = self.dpi_mod.get()
        nombres = self.nombres_mod.get()
        apellidos = self.apellidos_mod.get()
        genero = self.genero_mod.get()
        telefono = self.telefono_mod.get()
        direccion = self.direccion_mod.get()
        lcde.modificar_cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        self.dpi_modb.delete(0, tk.END)
        self.dpi_mod.delete(0, tk.END)
        self.nombres_mod.delete(0, tk.END)
        self.apellidos_mod.delete(0, tk.END)
        self.genero_mod.delete(0, tk.END)
        self.telefono_mod.delete(0, tk.END)
        self.direccion_mod.delete(0, tk.END)
    
    def eliminar_cliente(self):
        dpi = self.dpi_mod.get()
        lcde.eliminar_cliente(dpi)
        self.dpi_mod.delete(0, tk.END)
        self.nombres_mod.delete(0, tk.END)
        self.apellidos_mod.delete(0, tk.END)
        self.genero_mod.delete(0, tk.END)
        self.telefono_mod.delete(0, tk.END)
        self.direccion_mod.delete(0, tk.END)
    def grafico_cliente(self):
        lcde.generar_grafico()  
        canvas = tk.Canvas(self.ventanaclientes3, width=700, height=700)  
        canvas.grid(row=1, column=0, columnspan=3, sticky="nsew")  

        # Cargar la imagen
        try:
            img = tk.PhotoImage(file="clientes.png")
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.image = img 
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        scrollbar_vertical = tk.Scrollbar(self.ventanaclientes3, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.grid(row=1, column=3, sticky="ns")

        scrollbar_horizontal = tk.Scrollbar(self.ventanaclientes3, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_horizontal.grid(row=2, column=0, columnspan=3, sticky="ew")

        canvas.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
        canvas.config(scrollregion=canvas.bbox("all"))

            


    def create_widgets_in_ventanaclientes(self):
        # Etiquetas (Labels)
        tk.Label(self.ventanaclientes1, text="DPI").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes1, text="Nombres").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes1, text="Apellidos").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes1, text="Genero").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes1, text="Telefono").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes1, text="Direccion").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes1, text="Ruta del archivo").grid(row=8, column=0, padx=10, pady=10, sticky="w")

        # Cajas de texto (Entry)
        self.dpi_entry = tk.Entry(self.ventanaclientes1, width=30)
        self.dpi_entry.grid(row=0, column=1, padx=10, pady=10)
        self.nombres_entry = tk.Entry(self.ventanaclientes1, width=30)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=10)
        self.apellidos_entry = tk.Entry(self.ventanaclientes1, width=30)
        self.apellidos_entry.grid(row=2, column=1, padx=10, pady=10)
        self.genero_entry = ttk.Combobox(self.ventanaclientes1, width=23, values=['Masculino', 'Femenino'], font = "consolas 10")
        self.genero_entry.grid(row=3, column=1, padx=10, pady=10)
        self.telefono_entry = tk.Entry(self.ventanaclientes1, width=30)
        self.telefono_entry.grid(row=4, column=1, padx=10, pady=10)
        self.direccion_entry = tk.Entry(self.ventanaclientes1, width=30)
        self.direccion_entry.grid(row=5, column=1, padx=10, pady=10)
        self.ruta = tk.Entry(self.ventanaclientes1, width=30)
        self.ruta.grid(row=8, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self.ventanaclientes1, text="Guardar", command=self.data_cliente).grid(row=10, column=0, padx=5, pady=20)
        tk.Button(self.ventanaclientes1, text="Cargar datos", command=self.carga_cliente ).grid(row=10, column=1, padx=5, pady=20)
        tk.Button(self.ventanaclientes1, text="Cancelar", command=self.ventanaclientes1.withdraw).grid(row=10, column=2, padx=5, pady=20)
    

    def create_widgets_in_ventanaclientesmostrar(self):
        # Etiquetas (Labels)
        tk.Label(self.ventanaclientes4, text="DPI").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes4, text="Nombres").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes4, text="Apellidos").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes4, text="Genero").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes4, text="Telefono").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes4, text="Direccion").grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Cajas de texto (Entry)
        self.dpi_mostrar = tk.Entry(self.ventanaclientes4, width=30 )
        self.dpi_mostrar.grid(row=0, column=1, padx=10, pady=10)
        self.nombres_mostrar = tk.Entry(self.ventanaclientes4, width=30, state='disabled')
        self.nombres_mostrar.grid(row=1, column=1, padx=10, pady=10)
        self.apellidos_mostrar = tk.Entry(self.ventanaclientes4, width=30, state='disabled')
        self.apellidos_mostrar.grid(row=2, column=1, padx=10, pady=10)
        self.genero_mostrar = ttk.Combobox(self.ventanaclientes4, width=23, values=['Masculino', 'Femenino'], font = "consolas 10", state='disabled')
        self.genero_mostrar.grid(row=3, column=1, padx=10, pady=10)
        self.telefono_mostrar = tk.Entry(self.ventanaclientes4, width=30, state='disabled')
        self.telefono_mostrar.grid(row=4, column=1, padx=10, pady=10)
        self.direccion_mostrar = tk.Entry(self.ventanaclientes4, width=30, state='disabled')
        self.direccion_mostrar.grid(row=5, column=1, padx=10, pady=10)

        # Botones
       
        tk.Button(self.ventanaclientes4, text="Mostrar", command=self.print_data_cliente ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanaclientes4, text="Cancelar", command=self.ventanaclientes4.withdraw).grid(row=7, column=2, padx=5, pady=20)

    def create_widgets_in_ventanaclientesmodificar(self):
        # Etiquetas (Labels)

        tk.Label(self.ventanaclientes2, text="DPI").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes2, text="DPI").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes2, text="Nombres").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes2, text="Apellidos").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes2, text="Genero").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes2, text="Telefono").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaclientes2, text="Direccion").grid(row=6, column=0, padx=10, pady=10, sticky="w")

        # Cajas de texto (Entry)
        self.dpi_modb = tk.Entry(self.ventanaclientes2, width=30 )
        self.dpi_modb.grid(row=0, column=1, padx=10, pady=10)
        self.dpi_mod = tk.Entry(self.ventanaclientes2, width=30, state='disabled')
        self.dpi_mod.grid(row=1, column=1, padx=10, pady=10)
        self.nombres_mod = tk.Entry(self.ventanaclientes2, width=30)
        self.nombres_mod.grid(row=2, column=1, padx=10, pady=10)
        self.apellidos_mod = tk.Entry(self.ventanaclientes2, width=30)
        self.apellidos_mod.grid(row=3, column=1, padx=10, pady=10)
        self.genero_mod = ttk.Combobox(self.ventanaclientes2, width=23, values=['Masculino', 'Femenino'], font = "consolas 10")
        self.genero_mod.grid(row=4, column=1, padx=10, pady=10)
        self.telefono_mod = tk.Entry(self.ventanaclientes2, width=30)
        self.telefono_mod.grid(row=5, column=1, padx=10, pady=10)
        self.direccion_mod = tk.Entry(self.ventanaclientes2, width=30)
        self.direccion_mod.grid(row=6, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self.ventanaclientes2, text="Buscar", command=self.buscar_modificar).grid(row=0, column=2, padx=5, pady=20)
        tk.Button(self.ventanaclientes2, text="Guardar Cambios", command=self.modificar_cliente ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanaclientes2, text="Eliminar Cliente", command=self.eliminar_cliente).grid(row=7, column=2, padx=5, pady=20)
    def create_widgets_in_ventanaclientesgrafico(self):
        # Etiquetas (Labels)
        tk.Label(self.ventanaclientes3, text="").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Button(self.ventanaclientes3, text="Generar", command=self.grafico_cliente ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanaclientes3, text="Cancelar", command=self.ventanaclientes3.withdraw).grid(row=7, column=2, padx=5, pady=20)
    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     
    def crear_vehiculo(self):
        placa = self.placa_ag.get()
        marca = self.marca_ag.get()
        modelo = self.modelo_ag.get()
        precio = self.precio_ag.get()
        arbolb.insertar_valor(Vehiculos(placa, marca, modelo, float(precio)))
        self.placa_ag.delete(0, tk.END)
        self.marca_ag.delete(0, tk.END)
        self.modelo_ag.delete(0, tk.END)
        self.precio_ag.delete(0, tk.END)
    
    def cargar_vehiculo(self):
        ruta = self.ruta_ag.get()
        arbolb.leer_Archivo_vehiculos(ruta)
        

    def buscar_modificar_vehiculo(self):
        placa = self.placa_modb.get()
        vehiculo = arbolb.buscar_modificar(placa)
        if vehiculo:
            self.placa_mod.config(state='normal')
            self.placa_mod.delete(0, tk.END)
            self.placa_mod.insert(0, vehiculo.placa)
            self.placa_mod.config(state='disabled')
            self.marca_mod.delete(0, tk.END)
            self.marca_mod.insert(0, vehiculo.marca)
            self.modelo_mod.delete(0, tk.END)
            self.modelo_mod.insert(0, vehiculo.modelo)
            self.precio_mod.delete(0, tk.END)
            self.precio_mod.insert(0, vehiculo.precio)
        else:
            print("Vehículo no encontrado")

    def modificar_vehiculo(self):
        placa= self.placa_mod.get()
        marca = self.marca_mod.get()
        modelo = self.modelo_mod.get()
        precio = self.precio_mod.get()
        arbolb.modificar_vehiculo(placa, marca, modelo, precio)
        self.placa_modb.delete(0, tk.END)
        self.placa_mod.delete(0, tk.END)
        self.marca_mod.delete(0, tk.END)
        self.modelo_mod.delete(0, tk.END)
        self.precio_mod.delete(0, tk.END)
    
    def eliminar_vehiculo(self):
        placa = self.placa_modb.get()
        arbolb.eliminar_vehiculo(placa)
        self.placa_mod.delete(0, tk.END)
        self.marca_mod.delete(0, tk.END)
        self.modelo_mod.delete(0, tk.END)
        self.precio_mod.delete(0, tk.END)
    

    def grafico_vehiculos(self):
        arbolb.renderizar(arbolb.imprimir_usuario(), "vehiculos")
        canvas = tk.Canvas(self.ventanavehiculos4, width=700, height=700)  
        canvas.grid(row=1, column=0, columnspan=3, sticky="nsew")  

        # Cargar la imagen
        try:
            img = tk.PhotoImage(file="vehiculos.png")
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.image = img 
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        scrollbar_vertical = tk.Scrollbar(self.ventanavehiculos4, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.grid(row=1, column=3, sticky="ns")

        scrollbar_horizontal = tk.Scrollbar(self.ventanavehiculos4, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_horizontal.grid(row=2, column=0, columnspan=3, sticky="ew")

        canvas.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_widgets_in_ventanavehiculos(self):
        # Etiquetas (Labels)
        tk.Label(self.ventanavehiculos1, text="Placa").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos1, text="Marca").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos1, text="Modelo").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos1, text="Precio").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos1, text="Ruta del archivo").grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Cajas de texto (Entry)
        self.placa_ag = tk.Entry(self.ventanavehiculos1, width=30)
        self.placa_ag.grid(row=0, column=1, padx=10, pady=10)
        self.marca_ag = tk.Entry(self.ventanavehiculos1, width=30)
        self.marca_ag.grid(row=1, column=1, padx=10, pady=10)
        self.modelo_ag = tk.Entry(self.ventanavehiculos1, width=30)
        self.modelo_ag.grid(row=2, column=1, padx=10, pady=10)
        self.precio_ag = tk.Entry(self.ventanavehiculos1, width=30)
        self.precio_ag.grid(row=3, column=1, padx=10, pady=10)
        self.ruta_ag = tk.Entry(self.ventanavehiculos1, width=30)
        self.ruta_ag.grid(row=5, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self.ventanavehiculos1, text="Crear", command=self.crear_vehiculo ).grid(row=10, column=0, padx=5, pady=20)
        tk.Button(self.ventanavehiculos1, text="Cargar datos",command=self.cargar_vehiculo).grid(row=10, column=1, padx=5, pady=20)
        tk.Button(self.ventanavehiculos1, text="Cancelar", command=self.ventanavehiculos1.withdraw).grid(row=10, column=2, padx=5, pady=20)
    
    def create_widgets_in_ventanavehiculosmodificar(self):
        # Etiquetas (Labels)

        tk.Label(self.ventanavehiculos3, text="Placa").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos3, text="Placa").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos3, text="Marca").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos3, text="Modelo").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanavehiculos3, text="Precio").grid(row=5, column=0, padx=10, pady=10, sticky="w")


        # Cajas de texto (Entry)
        self.placa_modb = tk.Entry(self.ventanavehiculos3, width=30 )
        self.placa_modb.grid(row=0, column=1, padx=10, pady=10)
        self.placa_mod = tk.Entry(self.ventanavehiculos3, width=30, state='disabled')
        self.placa_mod.grid(row=1, column=1, padx=10, pady=10)
        self.marca_mod = tk.Entry(self.ventanavehiculos3, width=30)
        self.marca_mod.grid(row=2, column=1, padx=10, pady=10)
        self.modelo_mod = tk.Entry(self.ventanavehiculos3, width=30)
        self.modelo_mod.grid(row=3, column=1, padx=10, pady=10)
        self.precio_mod = tk.Entry(self.ventanavehiculos3, width=30)
        self.precio_mod.grid(row=5, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self.ventanavehiculos3, text="Buscar", command=self.buscar_modificar_vehiculo).grid(row=0, column=2, padx=5, pady=20)
        tk.Button(self.ventanavehiculos3, text="Guardar Cambios", command=self.modificar_vehiculo ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanavehiculos3, text="Eliminar Vehiculo", command=self.eliminar_vehiculo).grid(row=7, column=2, padx=5, pady=20)
        
    def create_widgets_in_ventanavehiculosgrafico(self):
        # Etiquetas (Labels)
        tk.Label(self.ventanavehiculos4, text="").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Button(self.ventanavehiculos4, text="Generar", command=self.grafico_vehiculos ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanavehiculos4, text="Cancelar", command=self.ventanavehiculos4.withdraw).grid(row=7, column=2, padx=5, pady=20)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def cargar_rutas(self):
        ruta = self.ruta_rutas.get()
        ady.cargar_rutas_desde_archivo(ruta)
        self.ruta_rutas.delete(0, tk.END)   
        

    def generar_grafo(self):
        dot = ady.imprimir()
        ady.renderizar(dot, "rutas")

        canvas = tk.Canvas(self.ventanarutas2, width=700, height=700)  
        canvas.grid(row=1, column=0, columnspan=3, sticky="nsew")  

        # Cargar la imagen
        try:
            img = tk.PhotoImage(file="rutas.png")
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.image = img 
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        scrollbar_vertical = tk.Scrollbar(self.ventanarutas2, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.grid(row=1, column=3, sticky="ns")

        scrollbar_horizontal = tk.Scrollbar(self.ventanarutas2, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_horizontal.grid(row=2, column=0, columnspan=3, sticky="ew")

        canvas.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_widgets_in_ventanarutas(self):

        tk.Label(self.ventanarutas, text="Ruta del archivo").grid(row=2, column=0, padx=10, pady=10, sticky="w")
       
        self.ruta_rutas = tk.Entry(self.ventanarutas, width=30)
        self.ruta_rutas.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Button(self.ventanarutas, text="Cargar datos", command=self.cargar_rutas ).grid(row=10, column=1, padx=5, pady=20)


    def create_widgets_in_ventanarutas2(self):

        tk.Button(self.ventanarutas2, text="Generar", command=self.generar_grafo ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanarutas2, text="Cancelar", command=self.ventanarutas2.withdraw).grid(row=7, column=2, padx=5, pady=20)

#------------------------------------------------------------------------------------------------------------------------------

    def crear_viaje(self):

        idviaje = self.id_viaje.get()
        origen = self.origen.get()
        destino = self.destino.get()
        fecha = self.fecha.get()
        hora = self.hora.get()
        idcliente = self.id_cliente.get()
        placa = self.placa_vehiculo.get()
        ruta_info = ady.obtener_ruta_corta(origen, destino)

        ruta, distancia = ruta_info
        cantidad_destinos = len(ruta) - 1 

        ve_encontrado=arbolb.buscar_modificar(placa)
        cliente_encontrado=lcde.buscar_cliente(idcliente)
        if ve_encontrado and cliente_encontrado:
            linked.insertar_linked(idviaje, origen, destino, fecha, hora, idcliente, placa, ruta,cantidad_destinos, distancia)
            #aqui incremento los contadores de viaje
            cliente_encontrado.contador+=1
            ve_encontrado.contador+=1
            print(f"Viaje creado correctamente con {cantidad_destinos} destinos en la ruta. con tiempo de {distancia}")

            print(f"Cliente {cliente_encontrado.nombre} ahora tiene {cliente_encontrado.contador} viajes.")
            print(f"Vehículo con placa {ve_encontrado.placa} ahora tiene {ve_encontrado.contador} viajes.")

        else:
            print("No se pudo crear el viaje")
        
        
    
    def mostrar_viaje(self):
        idviaje = self.idb_viaje.get()
        viaje = linked.mostrar_viaje(idviaje)
        if viaje:
            self.idviaje.config(state='normal')
            self.idviaje.delete(0, tk.END)
            self.idviaje.insert(0, viaje.ID)
            self.idviaje.config(state='disabled')
            self.origen_mos.config(state='normal')
            self.origen_mos.delete(0, tk.END)
            self.origen_mos.insert(0, viaje.origen)
            self.origen_mos.config(state='disabled')
            self.destino_mos.config(state='normal')
            self.destino_mos.delete(0, tk.END)
            self.destino_mos.insert(0, viaje.destino)
            self.destino_mos.config(state='disabled')
            self.fecha_mos.config(state='normal')
            self.fecha_mos.delete(0, tk.END)
            self.fecha_mos.insert(0, viaje.fecha)
            self.fecha_mos.config(state='disabled')
            self.hora_mos.config(state='normal')
            self.hora_mos.delete(0, tk.END)
            self.hora_mos.insert(0, viaje.hora)
            self.hora_mos.config(state='disabled')
            self.idcliente_mos.config(state='normal')
            self.idcliente_mos.delete(0, tk.END)
            self.idcliente_mos.insert(0, viaje.cliente)
            self.idcliente_mos.config(state='disabled')
            self.placa_mos.config(state='normal')
            self.placa_mos.delete(0, tk.END)
            self.placa_mos.insert(0, viaje.vehiculo)
            self.placa_mos.config(state='disabled')
            self.ruta_mos.config(state='normal')
            self.ruta_mos.delete(0, tk.END)
            self.ruta_mos.insert(0, viaje.ruta)
            self.ruta_mos.config(state='disabled')
            self.tiempo_mos.config(state='normal')
            self.tiempo_mos.delete(0, tk.END)
            self.tiempo_mos.insert(0, viaje.tiempo)
            self.tiempo_mos.config(state='disabled')

    def graficoviajes(self):
        dot = linked.generar_dot_viajes()
        linked.renderizar(dot, "viajes")

        canvas = tk.Canvas(self.ventanaviajes3, width=700, height=700)  
        canvas.grid(row=1, column=0, columnspan=3, sticky="nsew")  

        # Cargar la imagen
        try:
            img = tk.PhotoImage(file="viajes.png")
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.image = img 
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        scrollbar_vertical = tk.Scrollbar(self.ventanaviajes3, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_vertical.grid(row=1, column=3, sticky="ns")

        scrollbar_horizontal = tk.Scrollbar(self.ventanaviajes3, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_horizontal.grid(row=2, column=0, columnspan=3, sticky="ew")

        canvas.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
        canvas.config(scrollregion=canvas.bbox("all"))
        


    def create_widgets_in_ventanaviajes(self):
        # Etiquetas (Labels)
        tk.Label(self.ventanaviajes1, text="ID").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes1, text="Origen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes1, text="Destino").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes1, text="Fecha").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes1, text="Hora").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes1, text="ID Cliente").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes1, text="Placa Vehiculo").grid(row=6, column=0, padx=10, pady=10, sticky="w")

        # Cajas de texto (Entry)
        self.id_viaje = tk.Entry(self.ventanaviajes1, width=30)
        self.id_viaje.grid(row=0, column=1, padx=10, pady=10)
        self.origen = tk.Entry(self.ventanaviajes1, width=30)
        self.origen.grid(row=1, column=1, padx=10, pady=10)
        self.destino = tk.Entry(self.ventanaviajes1, width=30)
        self.destino.grid(row=2, column=1, padx=10, pady=10)
        self.fecha = tk.Entry(self.ventanaviajes1, width=30)
        self.fecha.grid(row=3, column=1, padx=10, pady=10)
        self.hora = tk.Entry(self.ventanaviajes1, width=30)
        self.hora.grid(row=4, column=1, padx=10, pady=10)
        self.id_cliente = tk.Entry(self.ventanaviajes1, width=30)
        self.id_cliente.grid(row=5, column=1, padx=10, pady=10)
        self.placa_vehiculo = tk.Entry(self.ventanaviajes1, width=30)
        self.placa_vehiculo.grid(row=6, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self.ventanaviajes1, text="Crear", command=self.crear_viaje).grid(row=10, column=0, padx=5, pady=20)
        tk.Button(self.ventanaviajes1, text="Cancelar", command=self.ventanaviajes1.withdraw).grid(row=10, column=2, padx=5, pady=20)
    
    def create_widgets_in_ventanaviajesmostrar(self):
        tk.Label(self.ventanaviajes2, text="ID Viaje Buscar").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="ID viaje").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Origen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Destino").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Fecha").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Hora").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="ID Cliente").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Placa Vehiculo").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Ruta Corta").grid(row=8, column=0, padx=10, pady=10, sticky="w")
        tk.Label(self.ventanaviajes2, text="Tiempo").grid(row=9, column=0, padx=10, pady=10, sticky="w")


        # Cajas de texto (Entry)
        self.idb_viaje = tk.Entry(self.ventanaviajes2, width=30 )
        self.idb_viaje.grid(row=0, column=1, padx=10, pady=10)
        self.idviaje = tk.Entry(self.ventanaviajes2, width=30, state='disabled')
        self.idviaje.grid(row=1, column=1, padx=10, pady=10)
        self.origen_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.origen_mos.grid(row=2, column=1, padx=10, pady=10)
        self.destino_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.destino_mos.grid(row=3, column=1, padx=10, pady=10)
        self.fecha_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.fecha_mos.grid(row=4, column=1, padx=10, pady=10)
        self.hora_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.hora_mos.grid(row=5, column=1, padx=10, pady=10)
        self.idcliente_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.idcliente_mos.grid(row=6, column=1, padx=10, pady=10)
        self.placa_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.placa_mos.grid(row=7, column=1, padx=10, pady=10)
        self.ruta_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.ruta_mos.grid(row=8, column=1, padx=10, pady=10)
        self.tiempo_mos = tk.Entry(self.ventanaviajes2, width=30)
        self.tiempo_mos.grid(row=9, column=1, padx=10, pady=10)

        # Botones
        tk.Button(self.ventanaviajes2, text="Mostrar", command=self.mostrar_viaje ).grid(row=10, column=1, padx=5, pady=20)
        tk.Button(self.ventanaviajes2, text="Cancelar", command=self.ventanaviajes2.withdraw).grid(row=10, column=2, padx=5, pady=20)
    
    def create_widgets_in_ventanaviajesgrafico(self):
        
        tk.Button(self.ventanaviajes3, text="Generar", command=self.graficoviajes ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanaviajes3, text="Cancelar", command=self.ventanaviajes3.withdraw).grid(row=7, column=2, padx=5, pady=20)
        
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def create_widgets_in_ventanareportes1(self):
        
        tk.Button(self.ventanareportes1, text="Generar",command=linked.mostrar_top_5_viajes ).grid(row=7, column=1, padx=5, pady=20)
        tk.Button(self.ventanareportes1, text="Cancelar", command=self.ventanareportes1.withdraw).grid(row=7, column=2, padx=5, pady=20)

# Configuración de la ventana principal
root = tk.Tk()
root.title('Proyecto 2 Emily de León')
root.geometry('700x500')
visual_studio_code = Myapp(root)
root.mainloop()
