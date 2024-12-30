from circular import listacirculardoble
from vehiculos import ArbolB
import tkinter as tk
from tkinter import ttk

arbol = ArbolB(5)
circular = listacirculardoble()

class Viajes:
    def __init__(self,ID,origen,destino,fecha,hora,cliente,vehiculo,ruta,destinos=0,tiempo=0):
        self.ID = ID
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.ruta = ruta
        self.destinos = destinos
        self.tiempo = tiempo
        self.siguiente = None
        self.anterior = None

class LinkedList:
    def __init__(self):
        self.primero = None

    def insertar_linked(self, ID, origen, destino, fecha, hora, cliente, placa, ruta, destinos, tiempo):

        nuevo = Viajes(ID, origen, destino, fecha, hora, cliente, placa, ruta, destinos, tiempo)

        if self.primero is None:
            self.primero = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
        else:
            actual = self.primero
            while True:
                if actual.siguiente == self.primero:
                    break
                actual = actual.siguiente
            nuevo.siguiente = self.primero
            nuevo.anterior = actual
            actual.siguiente = nuevo
            self.primero.anterior = nuevo
        print("Viaje agregado correctamente")
    
    def buscar_viaje(self, ID):
        if self.primero is None:
            return None
        actual = self.primero
        while True:
            if actual.ID == ID:
                return actual
            actual = actual.siguiente
            if actual == self.primero:
                return None
    
    def mostrar_viaje(self, ID):
        actual = self.buscar_viaje(ID)
        if actual is not None:
            return actual
        else:
            print("Viaje no encontrado")
        
          

    def generar_dot_viajes(self):
        if self.primero is None:
            print("No hay viajes para mostrar.")
            return None

        actual = self.primero
        dot = "digraph Viajes {\n\trankdir=LR;\n\tnode [shape=record style=filled fillcolor=\"#6cf0e0\" fontcolor=black];\n\t"

        # Generar los nodos
        nodos = []
        while True:
            nodos.append(
                f'"{actual.ID}" [label="ID: {actual.ID}\\nOrigen: {actual.origen}\\nDestino: {actual.destino}\\nFecha: {actual.fecha}\\nHora: {actual.hora}\\nCliente: {actual.cliente}\\nVehículo: {actual.vehiculo}\\nRuta: {actual.ruta}\\nTiempo: {actual.tiempo}"];'
            )
            actual = actual.siguiente
            if actual == self.primero:
                break
        dot += ";\n\t".join(nodos) + ";\n\t"

        # Generar las conexiones
        actual = self.primero
        while True:
            if actual.siguiente != self.primero:  # Asegurar que no conecte de vuelta al primero
                dot += f'"{actual.ID}" -> "{actual.siguiente.ID}";\n\t'
            
            actual = actual.siguiente
            if actual == self.primero:
                break

        dot += "}"
        return dot

# Método para renderizar el archivo DOT
    def renderizar(self, dot: str, nombre: str):
        from graphviz import Source
        Source(dot).render(nombre, format="png", cleanup=True)
    
    # Top 5 viajes con más destinos
    def top_5_viajes(self):
        if self.primero is None:
            print("No hay viajes para mostrar.")
            return None
        else:
            actual = self.primero
            lista = []
            while True:
                lista.append(actual)
                actual = actual.siguiente
                if actual == self.primero:
                    break
            lista.sort(key=lambda x: x.destinos, reverse=True)
            return lista[:5]
    
    def obtener_top_5_viajes(self):
        top_viajes = self.top_5_viajes()
        if not top_viajes:
            return []
        return [(viaje.ID, viaje.origen, viaje.destino, viaje.fecha, viaje.hora, viaje.cliente, viaje.vehiculo, viaje.ruta, viaje.destinos, viaje.tiempo) for viaje in top_viajes]
    


    def mostrar_top_5_viajes(self):
        # Crear ventana de Tkinter
        ventana = tk.Tk()
        ventana.title("Top 5 Viajes con Más Destinos")
        ventana.geometry("800x400")

        
        tree = ttk.Treeview(
            ventana,
            columns=("ID", "Origen", "Destino", "Fecha", "Hora", "Cliente", "Vehículo", "Ruta", "Destinos", "Tiempo"),
            show="headings"
        )
        tree.heading("ID", text="ID")
        tree.heading("Origen", text="Origen")
        tree.heading("Destino", text="Destino")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Hora", text="Hora")
        tree.heading("Cliente", text="Cliente")
        tree.heading("Vehículo", text="Vehículo")
        tree.heading("Ruta", text="Ruta")
        tree.heading("Destinos", text="Destinos")
        tree.heading("Tiempo", text="Tiempo")

        tree.column("ID", anchor="center", width=60)
        tree.column("Origen", anchor="center", width=100)
        tree.column("Destino", anchor="center", width=100)
        tree.column("Fecha", anchor="center", width=100)
        tree.column("Hora", anchor="center", width=80)
        tree.column("Cliente", anchor="center", width=120)
        tree.column("Vehículo", anchor="center", width=100)
        tree.column("Ruta", anchor="center", width=150)
        tree.column("Destinos", anchor="center", width=80)
        tree.column("Tiempo", anchor="center", width=80)

        # Obtener el top 5 de viajes
        top_viajes= self.obtener_top_5_viajes()
        
        for viaje in top_viajes:
            tree.insert("", "end", values=viaje)

    
        tree.pack(fill="both", expand=True)

        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
        btn_cerrar.pack(pady=10)

        # Mostrar la ventana
        ventana.mainloop()
