class Vertice:
    def __init__(self):
        self.nombre = 'Default'

    def agregarArista():
        pass
class Arista:
    def __init__(self):
        self.peso = 0
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



# Pruebas
G = Grafo()

# Pruebas con vertices
if not G.verificarSiExisteVertice('C'):
    print('No existe C')

G.agregarVertice('A')
G.agregarVertice('B')

if G.verificarSiExisteVertice('B'):
    print('Existe B')

G.agregarVertice('C')
G.agregarVertice('D')

if not G.verificarSiExisteVertice('F'):
    print("No existe F")

G.agregarVertice('C')

# Pruebas con Aristas
# Arista con vertices inexistentes
G.agregarArista(333, 'G', 'Z')

G.agregarArista(3, 'A', 'B')

G.agregarArista(7, 'B', 'C')

G.agregarArista(14, 'C', 'D')

# Arista con conexiones ya existentes
G.agregarArista(4654, 'C', 'B')


print('Nombres de vertices')
for vert in G.listaVertices:
    print(vert.nombre)

print('Nombres de Aristas')
for aris in G.listaAristas:
    print(f'Peso: {aris.peso}, Con1: {aris.conexion1.nombre}, Con2: {aris.conexion2.nombre}')