from circular import listacirculardoble
from vehiculos import ArbolB

arbol = ArbolB(5)
circular = listacirculardoble()

class Viajes:
    def __init__(self,ID,origen,destino,fecha,hora,cliente,vehiculo,ruta):
        self.ID = ID
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.ruta = ruta
        self.siguiente = None
        self.anterior = None

class LinkedList:
    def __init__(self):
        self.primero = None

    def insertar_linked(self, ID, origen, destino, fecha, hora, cliente, placa, ruta):

        nuevo = Viajes(ID, origen, destino, fecha, hora, cliente, placa, ruta)

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
                f'"{actual.ID}" [label="ID: {actual.ID}\\nOrigen: {actual.origen}\\nDestino: {actual.destino}\\nFecha: {actual.fecha}\\nHora: {actual.hora}\\nCliente: {actual.cliente}\\nVehículo: {actual.vehiculo}"]'
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
