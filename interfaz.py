from tkinter import *
from PIL import Image, ImageTk
from Grafo import Grafo
from Render import graficarGrafo,renderizar
class interfaz:
    def __init__(self, ventana):
        #ventana
        self.G=Grafo()
        ventana=ventana
        ventana.title('Teoría de Grafos')
        ventana.geometry('1000x600')
        ventana.configure(bg="orange")
        #imagenes
        '''ime1=Image.open('Grafo.png')
        self.img1=ImageTk.PhotoImage(ime1)
        lbl_img1=Label(ventana, image=self.img1)
        lbl_img1.place(x=0,y=10)'''
        #lbl_img1.pack()
        '''ime2=Image.open('Minimal.png')
        self.img2=ImageTk.PhotoImage(ime2)
        lbl_img2=Label(ventana, image=self.img2)
        lbl_img2.place(x=650,y=10)'''
        #lbl_img2.pack()
        '''img2=PhotoImage(file="nube3.png")
        lbl_img2=Label(ventana, image=img2)
        lbl_img2.pack()'''
        #labels
        lbl_vertice=Label(ventana,text="Vertice")
        lbl_vertice.place(x=10,y=400)
        lbl_arista=Label(ventana,text="Arista")
        lbl_arista.place(x=10,y=470)
        lbl_peso=Label(ventana, text="Peso")
        lbl_peso.place(x=130,y=470)
        vertices=Label(ventana,text="Vertices")
        vertices.place(x=250,y=400)
        aristas=Label(ventana,text="Aristas")
        aristas.place(x=370,y=400)
        lbl_ejemplo=Label(ventana,text="Ejemplo: A->B")
        lbl_ejemplo.place(x=10,y=530)
        lbl_pesominimo=Label(ventana,text=f"Peso minimo: {str(self.G.contarPesoMinimo())}")
        lbl_pesominimo.place(x=10,y=570)
        #Entrys
        self.cuadro_vertice=Entry(ventana,width=17)
        self.cuadro_vertice.place(x=10,y=430)
        self.cuadro_arista=Entry(ventana,width=17)
        self.cuadro_arista.place(x=10,y=500)
        self.cuadro_peso=Entry(ventana,width=17)
        self.cuadro_peso.place(x=130,y=500)
        #textarea
        self.text_vertices= Text(ventana)
        self.text_vertices.config(height=5, width=10)
        self.text_vertices.place(x=250,y=430)
        #self.text_vertices.configure(state='disabled')
        self.text_aristas= Text(ventana)
        self.text_aristas.config(height=5, width=10)
        self.text_aristas.place(x=370,y=430)
        #self.text_aristas.configure(state='disabled')
        #botones
        agregar_vertice=Button(ventana, text="Agregar Vertice", bg="lightblue", fg="black", command=lambda:self.agregar_vertice())
        agregar_vertice.place(x=130,y=430)
        #agregar_peso=Button(ventana, text="Agregar Peso", bg="lightblue", fg="black")
        #gregar_peso.place(x=130,y=430)
        agregar_arista=Button(ventana,text="Agregar Arista", bg="lightblue", fg="black", command=lambda:self.agregar_arista())
        agregar_arista.place(x=130,y=530)
        generar=Button(ventana, text="Generar", bg="lightblue", fg="black", command=lambda:self.generar())
        generar.place(x=480,y=400)

    def agregar_vertice(self):
        #print(self.cuadro_vertice.get())
        self.text_vertices.insert("1.0",self.cuadro_vertice.get())
        self.G.agregarVertice(str(self.cuadro_vertice.get()))
        self.cuadro_vertice.delete(0, 'end')

    def agregar_arista(self):
        self.text_aristas.insert("1.0",self.cuadro_arista.get())
        self.arista=self.cuadro_arista.get().replace("->","")
        print(self.arista[0],self.arista[1])
        self.G.agregarArista(self.cuadro_peso.get(),str(self.arista[0]),str(self.arista[1]))
        self.cuadro_arista.delete(0, 'end')
        self.cuadro_peso.delete(0, 'end')

    def generar(self):
        graficarGrafo(self.G, minimal=False)
        renderizar(mini=False)
        self.G.encontrarMinimal()
        graficarGrafo(self.G,minimal=True)
        renderizar(mini=True)


if __name__ == "__main__":
    ventana = Tk()
    aplicacion = interfaz(ventana)
    ventana.mainloop()