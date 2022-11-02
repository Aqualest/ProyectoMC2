from django.shortcuts import render
import Render

# Para la verificacion de ciclos
destino = None
primer = True

class Vertice:
    def __init__(self):
        self.nombre = 'Default'
        self.resaltar = False
        self.aristasResaltadas = []

class Arista:
    def __init__(self):
        self.peso = 0
        self.resaltar = False
        self.conexion1 = Vertice()
        self.conexion2 = Vertice()
        pass

class Grafo:
    def __init__(self):
        self.listaVertices = []
        self.listaAristas = []
        pass
    
    def verificarSiExisteVertice(self, nombreProbar:str):
        if len(self.listaVertices) > 0:
            for vert in self.listaVertices:
                if vert.nombre == nombreProbar:
                    return True
        return False

    def verificarSiExisteArista(self, nomVert1:str, nomVert2:str):
        if len(self.listaAristas) > 0:
            for aris in self.listaAristas:
                if aris.conexion1.nombre == nomVert1:
                    if aris.conexion2.nombre == nomVert2:
                        return True
                elif aris.conexion1.nombre == nomVert2:
                    if aris.conexion2.nombre == nomVert1:
                        return True
        return False
    
    def agregarVertice(self, nombre:str):
        if self.verificarSiExisteVertice(nombre):
            print('Ya existe un vertice con ese nombre, intenta otro.')
        else:
            temp = Vertice()
            temp.nombre = nombre
            self.listaVertices.append(temp)

    def agregarArista(self, peso:int, nomVert1:str, nomVert2:str):
        
        if self.verificarSiExisteArista(nomVert1, nomVert2):
            print('Ya existe una arista con esas conexiones.')
        else:
            temp = Arista()
            temp.peso = peso
            encontrado1 = False
            encontrado2 = False
            for vert in self.listaVertices:
                if vert.nombre == nomVert1:
                    temp.conexion1 = vert
                    encontrado1 = True
                elif vert.nombre == nomVert2:
                    temp.conexion2 = vert
                    encontrado2 = True
            # Para evitar que se cree una arista con Defaults
            if encontrado1 and encontrado2:
                self.listaAristas.append(temp)
            else:
                print('No se encontraron uno o ambos vertices para crear la arista.')

    def ordenarAristas(self):
        n = len(self.listaAristas)
        cambio = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.listaAristas[j].peso > self.listaAristas[j + 1].peso:
                    cambio = True
                    # Gracias Python por ser capaz de hacer este cambio tan genial xD
                    self.listaAristas[j], self.listaAristas[j + 1] = self.listaAristas[j + 1], self.listaAristas[j]
            if not cambio:
                return

    def resaltarVertice(self, nombre:str):
        for vert in self.listaVertices:
            if vert.nombre == nombre:
                vert.resaltar = True
                break

    def esCiclo(self, arista:Arista, inicio:Vertice):
        global destino
        for resal in inicio.aristasResaltadas:
            if resal != arista:
                # Si la arista padre y la arista resaltada del hijo no son la misma...

                if resal.conexion1.nombre == inicio.nombre:
                    if resal.conexion2.nombre == destino:
                        destino = 'Supah'
                        print('-------------------------------')
                        return
                    else:
                        if len(resal.conexion2.aristasResaltadas) > 1:
                            self.esCiclo(resal, resal.conexion2)
                        else:
                            continue

                elif resal.conexion2.nombre == inicio.nombre:
                    if resal.conexion1.nombre == destino:
                        destino = 'Supah'
                        print('-------------------------------')
                        return
                    else:
                        if len(resal.conexion1.aristasResaltadas) > 1:
                            self.esCiclo(resal, resal.conexion2)
                        else:
                            continue

    def encontrarMinimal(self):
        vertices = []
        visitados = []
        for vert in self.listaVertices:
            vertices.append(vert.nombre)
        # Bubblesort para los vertices, para usar Kruskal
        self.ordenarAristas()
        # Kruskal
        for arista in self.listaAristas:
            if arista.conexion1.nombre not in visitados or arista.conexion2.nombre not in visitados:
                arista.resaltar = True
                self.resaltarVertice(arista.conexion1.nombre)
                self.resaltarVertice(arista.conexion2.nombre)

                arista.conexion1.aristasResaltadas.append(arista)
                arista.conexion2.aristasResaltadas.append(arista)

                if arista.conexion1.nombre not in visitados:
                    visitados.append(arista.conexion1.nombre)
                if arista.conexion2.nombre not in visitados:
                    visitados.append(arista.conexion2.nombre)
            else:
                global destino
                destino = arista.conexion2.nombre
                if len(arista.conexion1.aristasResaltadas) > 0:
                    self.esCiclo(arista, arista.conexion1)
                    if destino != 'Supah':
                        arista.resaltar = True
                        self.resaltarVertice(arista.conexion1.nombre)
                        self.resaltarVertice(arista.conexion2.nombre)

                        arista.conexion1.aristasResaltadas.append(arista)
                        arista.conexion2.aristasResaltadas.append(arista)

                        if arista.conexion1.nombre not in visitados:
                            visitados.append(arista.conexion1.nombre)
                        if arista.conexion2.nombre not in visitados:
                            visitados.append(arista.conexion2.nombre)

            # Si la cantidad de vertices resaltados es igual a la de vertices - 1:
            contador = 0
            for arist in self.listaAristas:
                if arist.resaltar:
                    contador += 1
            if contador == len(vertices)-1:
                break

    def contarPesoMinimo(self):
        contador = 0
        for arista in self.listaAristas:
            if arista.resaltar == True:
                contador += arista.peso
        return contador

"""
# Pruebas
G = Grafo()

# Pruebas con vertices
G.agregarVertice('A')
G.agregarVertice('B')
G.agregarVertice('C')
G.agregarVertice('D')
G.agregarVertice('E')
G.agregarVertice('F')
G.agregarVertice('G')
G.agregarVertice('H')
G.agregarVertice('I')
G.agregarVertice('J')

# Pruebas con Aristas

G.agregarArista(3, 'A', 'C')
G.agregarArista(6, 'A', 'B')
G.agregarArista(9, 'A', 'E')
G.agregarArista(4, 'C', 'B')
G.agregarArista(9, 'C', 'E')
G.agregarArista(2, 'C', 'D')
G.agregarArista(9, 'C', 'F')
G.agregarArista(9, 'B', 'G')
G.agregarArista(2, 'B', 'D')
G.agregarArista(9, 'D', 'G')
G.agregarArista(8, 'F', 'E')
G.agregarArista(8, 'D', 'F')
G.agregarArista(18, 'E', 'J')
G.agregarArista(7, 'F', 'G')
G.agregarArista(9, 'F', 'I')
G.agregarArista(10, 'F', 'J')
G.agregarArista(5, 'G', 'I')
G.agregarArista(1, 'H', 'I')
G.agregarArista(4, 'G', 'H')
G.agregarArista(4, 'H', 'J')
G.agregarArista(3, 'I', 'J')


print('Nombres de vertices')
for vert in G.listaVertices:
    print(vert.nombre)

print('Nombres de Aristas')
for aris in G.listaAristas:
    print(f'Peso: {aris.peso}, Con1: {aris.conexion1.nombre}, Con2: {aris.conexion2.nombre}')


# Render
Render.graficarGrafo(G, minimal=False)
Render.renderizar(mini=False)
# Minimal
G.encontrarMinimal()
# Render otra vez con minimal
Render.graficarGrafo(G, minimal=True)
Render.renderizar(mini=True)

print(G.contarPesoMinimo())

"""