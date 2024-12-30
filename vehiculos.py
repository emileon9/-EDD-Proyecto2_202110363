class Vehiculos:
    def __init__(self, placa:str,marca: str, modelo: str, precio: float,contador=0):
        self.placa: str = placa;
        self.marca: str = marca;
        self.modelo: str = modelo;
        self.precio: float = precio;
        self.contador = contador
        
    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Precio: {self.precio} - Placa: {self.placa}";

class NodoArbolB:
    #constructor
    def __init__(self, hoja: bool = False):
        self.hoja: bool = hoja;
        self.claves: list[Vehiculos] = [] # orden del árbol - 1 (m - 1);
        self.hijos: list[NodoArbolB] = [] # orden del árbol (m)        
        
    def __str__(self):
        return f"Hoja: {self.hoja} - Claves: {self.claves} - Hijos: {self.hijos}";

class ArbolB:
    #constructor
    def __init__(self, orden: int):
        self.root: NodoArbolB = NodoArbolB(True);
        self.orden: int = orden;
        
    
    
    def insertar_valor(self, valor: Vehiculos):
        root: NodoArbolB = self.root
        
        self.insertar_valor_no_completo(root, valor)
        if len(root.claves) > self.orden - 1:
            nodo: NodoArbolB = NodoArbolB()
            self.root = nodo
            nodo.hijos.insert(0, root)
            self.dividir_pagina(nodo, 0)
            
    def insertar_valor_no_completo(self, root: NodoArbolB, valor: Vehiculos):
        posicion: int = len(root.claves) - 1;
        
        if (root.hoja):
            root.claves.append(None);
            
            while posicion >= 0 and valor.placa < root.claves[posicion].placa:
                root.claves[posicion + 1] = root.claves[posicion];
                posicion -= 1;
            root.claves[posicion + 1] = valor;
                
        else:
            while posicion >= 0 and valor.placa < root.claves[posicion].placa:
                posicion -= 1;
                
            posicion += 1;
            
            self.insertar_valor_no_completo(root.hijos[posicion], valor);
            if len(root.hijos[posicion].claves) > self.orden - 1:
                self.dividir_pagina(root, posicion);
    
    def dividir_pagina(self, root: NodoArbolB, posicion: int):
        posicion_media: int = int((self.orden - 1) / 2);
        
        hijo: NodoArbolB = root.hijos[posicion];
        nodo: NodoArbolB = NodoArbolB(hijo.hoja);
        
        root.hijos.insert(posicion + 1, nodo);
        
        root.claves.insert(posicion, hijo.claves[posicion_media]);
        
        nodo.claves = hijo.claves[posicion_media + 1:];
        hijo.claves = hijo.claves[:posicion_media];
        
        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media + 1:];
            hijo.hijos = hijo.hijos[:posicion_media + 1];
            
    def imprimir_usuario(self) -> str:
        dot: str = 'digraph G {\n\tbgcolor="white";\n\t'
        dot += "fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false\n\t"
        dot += 'node [shape=record width=1.2 style=filled fillcolor="#ff71c7" '
        dot += "fontcolor=\"#af006a\" color=transparent];\n\t"
        dot += 'edge [fontcolor=white color="black"];\n\t'
        
        dot += self.imprimir(self.root)
        
        dot += "\n}"
        
        return dot
            
    def imprimir(self, nodo: NodoArbolB, id: list[int] = [0]) -> str:
        root: NodoArbolB = nodo
        
        arbol = f'n{id[0]}[label="'
        contador: int = 0
        for item in root.claves:
            if contador == len(root.claves) - 1:
                arbol += f"<f{contador}>|{item.placa}|<f{contador + 1}>"
                break
            arbol += f"<f{contador}>|{item.placa}|"
            
            contador += 1
        
        arbol += "\"];\n\t"
        
        contador = 0
        id_padre = id[0]
        for item in root.hijos:
            arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
            
            id[0] += 1
            arbol += self.imprimir(item, id)
            
            contador += 1
            
        return arbol

    #renderizar el archivo dot y generar la imagen
    def renderizar(self, dot: str, nombre: str):
        from graphviz import Source
        Source(dot).render(nombre, format="png", cleanup=True)

        
    def __str__(self):
        return f"{self.root}"
    
    def leer_Archivo_vehiculos(self, ruta):
        try:
            with open(ruta, "r") as file:
                contenido = file.read()
                vehiculos = contenido.split(";")
                placas = set()
                duplicados = 0
                procesados = 0

                for vehiculo in vehiculos:
                    if vehiculo.strip():
                        try:
                            placa, marca, modelo, precio = vehiculo.strip().split(":")
                            if placa in placas:
                                duplicados += 1
                                continue
                            self.insertar_valor(Vehiculos(placa, marca, modelo, float(precio)))
                            placas.add(placa)
                            procesados += 1
                        except ValueError:
                            print(f"Formato inválido: {vehiculo.strip()}")
                            continue

                print(f"Vehículos cargados: {procesados}, Duplicados: {duplicados}")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    def buscar(self, nodo, placa):
        i = 0
        while i < len(nodo.claves) and placa > nodo.claves[i].placa:
            i += 1

        if i < len(nodo.claves) and placa == nodo.claves[i].placa:
            return nodo.claves[i]
        elif nodo.hoja:
            return None
        else:
            return self.buscar(nodo.hijos[i], placa)
    
    def buscar_modificar(self, placa):
        vehiculo = self.buscar(self.root, placa)
        if vehiculo is not None:
            return vehiculo
        else:
            print("Vehículo no encontrado")
    

    def modificar_vehiculo(self, placa, marca, modelo, precio):
        vehiculo = self.buscar(self.root, placa)
        if vehiculo is not None:
            vehiculo.marca = marca
            vehiculo.modelo = modelo
            vehiculo.precio = precio
            print("Vehículo modificado correctamente")
        else:
            print("Vehículo no encontrado")

    def eliminar_vehiculo(self, placa):
        self.eliminar(self.root, placa)
        # Si la raíz se queda vacía y no es hoja, reemplazarla con el primer hijo
        if len(self.root.claves) == 0 and not self.root.hoja:
            self.root = self.root.hijos[0]
        elif len(self.root.claves) == 0:  # Si la raíz está vacía y es hoja
            self.root = NodoArbolB(True)
        print("Vehículo eliminado correctamente")

    def eliminar(self, nodo, placa):
        i = 0
        # Encuentra la posición de la clave
        while i < len(nodo.claves) and placa > nodo.claves[i].placa:
            i += 1

        # Caso 1: La clave está en el nodo actual (hoja o interno)
        if i < len(nodo.claves) and placa == nodo.claves[i].placa:
            if nodo.hoja:  # Caso 1a: Nodo hoja
                nodo.claves.pop(i)
            else:  # Caso 1b: Nodo interno
                self.eliminar_interno(nodo, i)
        elif nodo.hoja:  # Caso 2: La clave no está y estamos en una hoja
            print("Vehículo no encontrado")
            return
        else:  # Caso 3: Buscar en un hijo
            # Asegurarse de que el hijo tenga suficientes claves
            if len(nodo.hijos[i].claves) < self.orden - 1:
                self.rellenar(nodo, i)
            # Recursivamente eliminar en el hijo adecuado
            if i > len(nodo.claves):  # Si se fusionó el nodo, moverse al último hijo
                self.eliminar(nodo.hijos[i - 1], placa)
            else:
                self.eliminar(nodo.hijos[i], placa)

    def eliminar_interno(self, nodo, i):
        # Caso 1: Predecesor tiene suficientes claves
        if len(nodo.hijos[i].claves) >= self.orden:
            predecesor = self.obtener_predecesor(nodo, i)
            nodo.claves[i] = predecesor
            self.eliminar(nodo.hijos[i], predecesor.placa)
        # Caso 2: Sucesor tiene suficientes claves
        elif len(nodo.hijos[i + 1].claves) >= self.orden:
            sucesor = self.obtener_sucesor(nodo, i)
            nodo.claves[i] = sucesor
            self.eliminar(nodo.hijos[i + 1], sucesor.placa)
        # Caso 3: Fusionar hijos
        else:
            self.unir(nodo, i)
            self.eliminar(nodo.hijos[i], nodo.claves[i].placa)

    def obtener_predecesor(self, nodo, i):
        actual = nodo.hijos[i]
        while not actual.hoja:
            actual = actual.hijos[-1]
        return actual.claves[-1]

    def obtener_sucesor(self, nodo, i):
        actual = nodo.hijos[i + 1]
        while not actual.hoja:
            actual = actual.hijos[0]
        return actual.claves[0]

    def rellenar(self, nodo, i):
        if i != 0 and len(nodo.hijos[i - 1].claves) >= self.orden:
            self.prestar_anterior(nodo, i)
        elif i != len(nodo.hijos) - 1 and len(nodo.hijos[i + 1].claves) >= self.orden:
            self.prestar_siguiente(nodo, i)
        else:
            if i != len(nodo.hijos) - 1:
                self.unir(nodo, i)
            else:
                self.unir(nodo, i - 1)

    def prestar_anterior(self, nodo, i):
        hijo = nodo.hijos[i]
        hermano = nodo.hijos[i - 1]

        hijo.claves.insert(0, nodo.claves[i - 1])
        nodo.claves[i - 1] = hermano.claves.pop(-1)

        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop(-1))

    def prestar_siguiente(self, nodo, i):
        hijo = nodo.hijos[i]
        hermano = nodo.hijos[i + 1]

        hijo.claves.append(nodo.claves[i])
        nodo.claves[i] = hermano.claves.pop(0)

        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))

    def unir(self, nodo, i):
        hijo = nodo.hijos[i]
        hermano = nodo.hijos[i + 1]

        hijo.claves.append(nodo.claves.pop(i))
        hijo.claves.extend(hermano.claves)

        if not hijo.hoja:
            hijo.hijos.extend(hermano.hijos)

        nodo.hijos.pop(i + 1)

    def __str__(self):
        return f"{self.root}"