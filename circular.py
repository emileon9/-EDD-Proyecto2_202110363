from graphviz import Digraph
from tkinter import PhotoImage


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

