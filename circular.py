from graphviz import Digraph
from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk


class Nodocircular:
    def __init__(self, dpi, nombre, apellido, genero, telefono, direccion, contador=0):
        self.dpi = dpi
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion
        self.contador = contador
        self.siguiente = None
        self.anterior = None


class listacirculardoble:
    def __init__(self):
        self.primero = None

    def agregar_cliente(self, dpi, nombre, apellido, genero, telefono, direccion):
        if self.buscar_cliente(dpi) is not None:
            print("Cliente con este DPI ya existe")
            return

        nuevo = Nodocircular(dpi, nombre, apellido, genero, telefono, direccion)
        if self.primero is None:
            self.primero = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
        else:
            actual = self.primero
            while True:
                if actual.dpi > nuevo.dpi:
                    break
                actual = actual.siguiente
                if actual == self.primero:
                    break

            anterior = actual.anterior
            nuevo.siguiente = actual
            nuevo.anterior = anterior
            anterior.siguiente = nuevo
            actual.anterior = nuevo

            if actual == self.primero and nuevo.dpi < self.primero.dpi:
                self.primero = nuevo
        print("Cliente agregado correctamente")

    def buscar_cliente(self, dpi):
        if self.primero is None:
            return None
        actual = self.primero
        while True:
            if actual.dpi == dpi:
                return actual
            actual = actual.siguiente
            if actual == self.primero:
                return None

    def modificar_cliente(self, dpi, nombre, apellido, genero, telefono, direccion):
        actual = self.buscar_cliente(dpi)
        if actual is not None:
            actual.nombre = nombre
            actual.apellido = apellido
            actual.genero = genero
            actual.telefono = telefono
            actual.direccion = direccion
            print("Cliente modificado correctamente")
        else:
            print("Cliente no encontrado")

    def eliminar_cliente(self, dpi):
        actual = self.buscar_cliente(dpi)
        if actual is not None:
            if actual.siguiente == actual:
                self.primero = None
            else:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                if actual == self.primero:
                    self.primero = actual.siguiente
            print("Cliente eliminado correctamente")
        else:
            print("Cliente no encontrado")

    def mostrar_cliente(self, dpi):
        actual = self.buscar_cliente(dpi)
        if actual is not None:
            return actual
        else:
            print("Cliente no encontrado")

    def leer_ruta_archivo(self, ruta):
        try:
            with open(ruta, "r") as file:
                contenido = file.read()
                clientes = contenido.split(";")
                for cliente in clientes:
                    if cliente.strip():
                        dpi, nombre, apellido, genero, telefono, direccion = (
                            cliente.strip().split(",")
                        )
                        self.agregar_cliente(
                            dpi, nombre, apellido, genero, telefono, direccion
                        )

            print("Clientes cargados correctamente desde el archivo")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    
    def generar_grafico(self):
        if self.primero is None:
            print("No hay clientes para graficar")
            return

        from graphviz import Digraph

        dot = Digraph(comment="Clientes")
        dot.attr(layout="circo")
        dot.node_attr.update(shape="box")

        actual = self.primero
        visitados = set()
        nodos = []
        conexiones = []

        # Crear nodos y conexiones
        while actual.dpi not in visitados:
            visitados.add(actual.dpi)
            nodos.append(
                (str(actual.dpi), f"DPI: {actual.dpi}\nNombre: {actual.nombre}\nApellido: {actual.apellido}\nGénero: {actual.genero}\nTeléfono: {actual.telefono}\nDirección: {actual.direccion}")
            )
            if actual.siguiente:
                conexiones.append((str(actual.dpi), str(actual.siguiente.dpi)))
            actual = actual.siguiente
            if actual == self.primero:
                break

        # Agregar nodos al gráfico
        for nodo_id, label in nodos:
            dot.node(nodo_id, label)

        # Agregar conexiones al gráfico
        for origen, destino in conexiones:
            dot.edge(origen, destino, dir="both")

        # Cerrar conexión circular
        dot.edge(str(actual.anterior.dpi), str(self.primero.dpi), dir="both")

        try:
            dot.render("clientes", format="png", cleanup=True)
            print("Gráfico generado correctamente")
        except Exception as e:
            print(f"Error al generar el gráfico: {e}")
    
    def top_5_clientes(self):
        if self.primero is None:
            print("No hay clientes para mostrar.")
            return None
        else:
            actual = self.primero
            lista = []
            while True:
                lista.append(actual)
                actual = actual.siguiente
                if actual == self.primero:
                    break
            # Ordenar por el contador de viajes en orden descendente
            lista.sort(key=lambda x: x.contador, reverse=True)
            return lista[:5]  # Retornar los 5 clientes con más viajes

    def obtener_top_5_clientes(self):
        top_clientes = self.top_5_clientes()
        if not top_clientes:
            return []
        return [
            (
                cliente.dpi,
                cliente.nombre,
                cliente.apellido,
                cliente.genero,
                cliente.telefono,
                cliente.direccion,
                cliente.contador,
            )
            for cliente in top_clientes
        ]

    def mostrar_top_5_clientes(self):
        # Crear ventana de Tkinter
        ventana = tk.Tk()
        ventana.title("Top 5 Clientes con Más Viajes")
        ventana.geometry("800x400")

        # Crear tabla usando Treeview
        tree = ttk.Treeview(
            ventana,
            columns=("DPI", "Nombre", "Apellido", "Género", "Teléfono", "Dirección", "Viajes"),
            show="headings"
        )
        tree.heading("DPI", text="DPI")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Apellido", text="Apellido")
        tree.heading("Género", text="Género")
        tree.heading("Teléfono", text="Teléfono")
        tree.heading("Dirección", text="Dirección")
        tree.heading("Viajes", text="Viajes")

        tree.column("DPI", anchor="center", width=120)
        tree.column("Nombre", anchor="center", width=100)
        tree.column("Apellido", anchor="center", width=100)
        tree.column("Género", anchor="center", width=80)
        tree.column("Teléfono", anchor="center", width=120)
        tree.column("Dirección", anchor="center", width=150)
        tree.column("Viajes", anchor="center", width=80)

        # Obtener el top 5 de clientes con más viajes
        top_clientes = self.obtener_top_5_clientes()
        for cliente in top_clientes:
            tree.insert("", "end", values=cliente)

        tree.pack(fill="both", expand=True)

        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)

        # Mostrar la ventana
        ventana.mainloop()



