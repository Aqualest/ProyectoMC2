from tkinter import *
from PIL import Image, ImageTk
from Grafo import Grafo
from Render import graficarGrafo, renderizar

class interfaz:
    def __init__(self, ventana):
        #ventana
        self.G=Grafo()
        ventana=ventana
        ventana.title('Teoría de Grafos - Árbol Generador Minimal')
        ventana.geometry('800x500')
        ventana.configure(bg="#27a3f5")
        # frame de imagenes
        self.frame1 = Frame(ventana, width=400, height=300, padx=5, pady=5)
        self.frame1.grid(row=0, column=0, columnspan=3)
        self.frame2 = Frame(ventana, width=400, height=300, padx=5, pady=5)
        self.frame2.grid(row=0, column=3, columnspan=3)
        #labels
        lbl_vertice=Label(ventana,text="Vertice")
        lbl_vertice.grid(row=1, column=0, padx=10, pady=10)
        lbl_arista=Label(ventana,text="Arista")
        lbl_arista.grid(row=3, column=0, padx=10, pady=10)
        lbl_peso=Label(ventana, text="Peso")
        lbl_peso.grid(row=3, column=1, padx=10, pady=10)
        vertices=Label(ventana,text="Vertices")
        vertices.grid(row=1, column=2, padx=10, pady=10)
        aristas=Label(ventana,text="Aristas")
        aristas.grid(row=1, column=3, padx=10, pady=10)
        lbl_ejemplo=Label(ventana,text="Ejemplo: A->B")
        lbl_ejemplo.grid(row=5, column=0, padx=10, pady=10)
        lbl_pesominimo=Label(ventana,text=f"Peso minimo: {str(self.G.contarPesoMinimo())}")
        lbl_pesominimo.grid(row=6, column=0, padx=10, pady=10)
        #Entrys
        self.cuadro_vertice=Entry(ventana,width=17)
        self.cuadro_vertice.grid(row=2, column=0)
        self.cuadro_arista=Entry(ventana,width=17)
        self.cuadro_arista.grid(row=4, column=0)
        self.cuadro_peso=Entry(ventana,width=17)
        self.cuadro_peso.grid(row=4, column=1)
        #textarea
        self.text_vertices= Text(ventana)
        self.text_vertices.config(height=5, width=10)
        self.text_vertices.grid(row=2, column=2, rowspan=3)
        self.text_aristas= Text(ventana)
        self.text_aristas.config(height=5, width=20)
        self.text_aristas.grid(row=2, column=3, rowspan=3)
        #self.text_aristas.configure(state='disabled')
        
        #botones
        agregar_vertice=Button(ventana, text="Agregar Vertice", bg="lightgreen", fg="black", command=lambda:self.agregar_vertice())
        agregar_vertice.grid(row=2, column=1)
  
        agregar_arista=Button(ventana,text="Agregar Arista", bg="lightgreen", fg="black", command=lambda:self.agregar_arista())
        agregar_arista.grid(row=5, column=1)

        generar=Button(ventana, text="Generar", bg="lightgreen", fg="black", command=lambda:self.generar())
        generar.grid(row=1, column=4)

    def agregar_vertice(self):

        self.G.agregarVertice(str(self.cuadro_vertice.get()))
        self.cuadro_vertice.delete(0, 'end')
        contenidoVertices = ''
        self.text_vertices.delete('1.0', END)
        for vert in self.G.listaVertices:
            contenidoVertices += f'{vert.nombre}\n'
        self.text_vertices.insert(1.0, contenidoVertices)
    
    def agregar_arista(self):

        self.arista=self.cuadro_arista.get().replace("->","")
        print(self.arista[0],self.arista[1])

        self.G.agregarArista(self.cuadro_peso.get(),str(self.arista[0]),str(self.arista[1]))
        self.cuadro_arista.delete(0, 'end')
        self.cuadro_peso.delete(0, 'end')

        contenidoAristas = ''
        self.text_aristas.delete('1.0', END)
        for arist in self.G.listaAristas:
            contenidoAristas += f'{arist.conexion1.nombre} -> {arist.conexion2.nombre} Peso: {arist.peso}\n'
        self.text_aristas.insert(1.0, contenidoAristas)

    def generar(self):
        graficarGrafo(self.G, minimal=False)
        renderizar(mini=False)
        self.G.encontrarMinimal()
        graficarGrafo(self.G,minimal=True)
        renderizar(mini=True)

        # Create an object of tkinter ImageTk
        img1 = ImageTk.PhotoImage(Image.open("Grafo.png"))
        img2 = ImageTk.PhotoImage(Image.open("Minimal.png"))

        label1 = Label(self.frame1, image = img1)
        label1.pack()
        label2 = Label(self.frame2, image = img2)
        label2.pack()



if __name__ == "__main__":
    ventana = Tk()
    aplicacion = interfaz(ventana)
    ventana.mainloop()