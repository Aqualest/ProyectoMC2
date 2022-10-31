import networkx as nx


class renderizacion:

    def __init__(self, grafo: nx.Graph,nombre:str):
        self.grafo = grafo


    #Funcion para crear nodos
    def crearnodos(self, nodo):
        self.grafo.add_node(nodo)


    # Funcion para crear aristas
    def creararista(self,nodo1: str,nodo2: str,peso: int):
        self.grafo.add_edge(nodo1,nodo2,label =str(peso))
        

    def modificararista(self,nodo1: str, nodo2: str):
        #Obteniendo los atributos 
        valor = list(self.grafo.get_edge_data(nodo1,nodo2).values())
        peso = int(valor[0])

        #Agregando el cambio de color de los nodos y las aristas
            #Nodos
        self.grafo.add_node(nodo1, color = "green")
        self.grafo.add_node(nodo2, color = "green")

            #Arista
        self.grafo.add_edge(nodo1,nodo2,label =str(peso),color = "green")


    def guardarimagen(self,nombre:str):
        nx.draw(self.grafo)
        A = nx.nx_agraph.to_agraph(self.grafo)
        A.layout('dot')
        A.draw(nombre+'.png') # guardar como png

#Pruebas ---------------------------------------------------------------------------------------------------------------

#Creando el grafo   
grafo = nx.Graph(rankdir="LR")

#Inicializando la clase
g = renderizacion(grafo,"grafo")

#Generando Nodos
g.crearnodos("A")
g.crearnodos("B")
g.crearnodos("C")
g.crearnodos("D")
g.crearnodos("E")
g.crearnodos("F")
g.crearnodos("G")
g.crearnodos("G")


#Generando Aristasd
g.creararista("A","B",10)
g.creararista("A","C",15)
g.creararista("A","F",20)
g.creararista("E","F",5)
g.creararista("E","G",6)
g.creararista("E","D",3)
g.creararista("B","C",2)
g.creararista("C","E",1)
g.creararista("C","D",4)
g.creararista("D","G",6)
g.creararista("H","F",7)
g.creararista("H","G",8)

#Guardar Imagen Inicial
g.guardarimagen("inicial")

#Modificar Aristas para el algoritmo de Prim
g.modificararista("A","B")
g.modificararista("B","C")
g.modificararista("C","E")
g.modificararista("E","F")
g.modificararista("F","H")

#Guardar Final
g.guardarimagen("final")
