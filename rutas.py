class Rutas:
    def __init__(self, origen, destino, tiempo):
        self.origen = origen
        self.destino = destino
        self.tiempo = tiempo
        self.siguiente = None
        self.anterior = None    

class Nodo:
    def __init__(self, valor: Rutas):
        self.valor: Rutas = valor
        self.sig: Nodo = None

class Vertice:
    def __init__(self, valor: str):
        self.valor: str = valor
        self.vecinos: Lista = Lista()
        
    def __str__(self) -> str:
        aux = self.vecinos.cabeza
        dot: str = ""
        while aux is not None:
            dot += f'{self.valor} -> {aux.valor.destino} [label="{aux.valor.tiempo}"];\n\t'
            aux = aux.sig
        return dot

class Lista:
    def __init__(self):
        self.cabeza: Nodo = None
        
    def insertar_final(self, valor: Rutas) -> Nodo:
        aux: Nodo = self.cabeza
        if aux is None:
            aux = Nodo(valor)
            self.cabeza = aux
            return self.cabeza
        while aux.sig is not None:
            aux = aux.sig
        aux.sig = Nodo(valor)
        return aux.sig
        
    def buscar(self, valor: str) -> Nodo:
        aux: Nodo = self.cabeza
        while aux is not None:
            if aux.valor.valor == valor:
                return aux
            aux = aux.sig
        return None

class ListaAdyacencia:
    def __init__(self):
        self.vertices: Lista = Lista()
        
    def insertar(self, origen: str, destino: str, tiempo: int):
        ruta = Rutas(origen, destino, tiempo)
        vertice_origen = self.vertices.buscar(origen)
        if vertice_origen is None:
            vertice_origen = Nodo(Vertice(origen))
            self.vertices.insertar_final(vertice_origen.valor)
        vertice_origen.valor.vecinos.insertar_final(ruta)
        
    def imprimir(self) -> str:
        dot = 'digraph G {\n\tbgcolor="white";\n\trankdir=LR;\n\tedge [arrowhead=none fontcolor=black color="#8e44ad"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#85c1e9" fontcolor=white '
        dot += 'color=transparent];\n\t'
        conexiones = set()
        aux: Nodo = self.vertices.cabeza
        while aux is not None:
            vertice = aux.valor
            vecinos = vertice.vecinos.cabeza
            while vecinos is not None:
                ruta = vecinos.valor
                conexion = (min(ruta.origen, ruta.destino), max(ruta.origen, ruta.destino))
                if conexion not in conexiones:
                    dot += f'{ruta.origen} -> {ruta.destino} [fontsize=7, headlabel="{ruta.tiempo}",taillabel="{ruta.tiempo}", labeldistance=1.5];\n\t'
                    conexiones.add(conexion)
                vecinos = vecinos.sig
            aux = aux.sig
        dot += "}"
        return dot

    #renderizar el archivo dot y generar la imagen
    def renderizar(self, dot: str, nombre: str):
        from graphviz import Source
        Source(dot).render(nombre, format="png", cleanup=True)

    def cargar_rutas_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as file:
                for linea in file:
                    partes = linea.strip().split('%')
                    for parte in partes:
                        if parte.strip():
                            subpartes = parte.strip().split('/')
                            if len(subpartes) == 3:
                                origen = subpartes[0].strip()
                                destino = subpartes[1].strip()
                                tiempo = int(subpartes[2].strip())

                                # Insertar las rutas en ambas direcciones
                                self.insertar(origen, destino, tiempo)
                                self.insertar(destino, origen, tiempo)

            print("Archivo de rutas cargado correctamente.")
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
    
    
    def obtener_ruta_corta(self, origen: str, destino: str):
        if self.vertices.cabeza is None:
            print("No hay rutas para buscar.")
            return None

        # Inicializar estructuras para el algoritmo de Dijkstra
        distancias = {}
        predecesores = {}
        visitados = set()

        # Inicializar las distancias a infinito y predecesores a None
        aux = self.vertices.cabeza
        while aux is not None:
            vertice = aux.valor
            distancias[vertice.valor] = float('inf')
            predecesores[vertice.valor] = None
            aux = aux.sig

        distancias[origen] = 0  # La distancia al nodo origen es 0

        # Aplicar Dijkstra
        while len(visitados) < len(distancias):
            # Seleccionar el nodo no visitado con la menor distancia
            actual = None
            menor = float('inf')
            for vertice, distancia in distancias.items():
                if vertice not in visitados and distancia < menor:
                    menor = distancia
                    actual = vertice

            if actual is None:
                break  # No hay más nodos alcanzables

            visitados.add(actual)

            # Relajar las aristas del nodo actual
            vertice_actual = self.vertices.buscar(actual)
            if vertice_actual is not None:
                arista_aux = vertice_actual.valor.vecinos.cabeza
                while arista_aux is not None:
                    arista = arista_aux.valor
                    nueva_distancia = distancias[actual] + arista.tiempo
                    if nueva_distancia < distancias[arista.destino]:
                        distancias[arista.destino] = nueva_distancia
                        predecesores[arista.destino] = actual
                    arista_aux = arista_aux.sig

        # Reconstruir el camino más corto desde el origen al destino
        camino = []
        actual = destino
        while actual is not None:
            camino.insert(0, actual)
            actual = predecesores[actual]

        if distancias[destino] == float('inf'):
            print(f"No hay un camino desde {origen} a {destino}.")
            return None

        return camino, distancias[destino]



