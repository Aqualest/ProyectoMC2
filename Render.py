import pydot


def graficarGrafo(grafo, minimal:bool):
    print("")
    # Principio
    contenido = '''Graph {
graph[rankdir=LR, center=true, margin=0.2, nodesep=0.1, ranksep=0.3]
node[shape=circle, style=filled, fontname="Verdana", fontsize=10, width=0.4, height=0.4, fixedsize=true]

'''
    
    # Nodos
    for vertice in grafo.listaVertices:
        if vertice.resaltar:
            contenido += f'{vertice.nombre} [fillcolor=cyan]\n'
        else:
            contenido += f'{vertice.nombre} [fillcolor=grey]\n'

    for arista in grafo.listaAristas:
        vert1 = arista.conexion1.nombre
        vert2 = arista.conexion2.nombre
        peso = arista.peso
        if arista.resaltar:
            contenido += f'{vert1} -- {vert2} [label=\"{peso}\" color=blue]\n'
        else:
            contenido += f'{vert1} -- {vert2} [label=\"{peso}\" color=grey]\n'
    
    contenido += '\n}'
        

    if not minimal:
        archivoDot = open('Grafo.dot', 'w')
        archivoDot.write(contenido)
        archivoDot.close
    else:
        archivoDot = open('Minimal.dot', 'w')
        archivoDot.write(contenido)
        archivoDot.close
        


def renderizar(mini:bool):
    if mini:
        (graph,) = pydot.graph_from_dot_file('Minimal.dot')
        graph.write_png('Minimal.png')
    else:
        (graph,) = pydot.graph_from_dot_file('Grafo.dot')
        graph.write_png('Grafo.png')