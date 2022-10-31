from tkinter import *
from PIL import Image, ImageTk
class interfaz:
    def __init__(self, ventana):
        #ventana
        ventana=ventana
        ventana.title('Teoría de Grafos')
        ventana.geometry('550x500')
        ventana.resizable(0,0)
        ventana.configure(bg="orange")
        #imagenes
        ime1=Image.open('nube3.png')
        self.img1=ImageTk.PhotoImage(ime1)
        lbl_img1=Label(ventana, image=self.img1)
        lbl_img1.place(x=10,y=0)
        #lbl_img1.pack()
        ime2=Image.open('nube2.gif')
        self.img2=ImageTk.PhotoImage(ime2)
        lbl_img2=Label(ventana, image=self.img2)
        lbl_img2.place(x=150,y=0)
        '''img2=PhotoImage(file="nube3.png")
        lbl_img2=Label(ventana, image=img2)
        lbl_img2.pack()'''
        #labels
        lbl_vertice=Label(ventana,text="Vertice")
        lbl_vertice.place(x=10,y=300)
        lbl_arista=Label(ventana,text="Arista")
        lbl_arista.place(x=10,y=370)
        lbl_peso=Label(ventana, text="Peso")
        lbl_peso.place(x=130,y=370)
        vertices=Label(ventana,text="Vertices")
        vertices.place(x=250,y=300)
        aristas=Label(ventana,text="Aristas")
        aristas.place(x=370,y=300)
        #Entrys
        cuadro_vertice=Entry(ventana,width=17)
        cuadro_vertice.place(x=10,y=330)
        cuadro_arista=Entry(ventana,width=17)
        cuadro_arista.place(x=10,y=400)
        cuadro_peso=Entry(ventana,width=17)
        cuadro_peso.place(x=130,y=400)
        #textarea
        self.text_vertices= Text(ventana)
        self.text_vertices.config(height=5, width=10)
        self.text_vertices.place(x=250,y=330)
        self.text_aristas= Text(ventana)
        self.text_aristas.config(height=5, width=10)
        self.text_aristas.place(x=370,y=330)
        #botones
        agregar_vertice=Button(ventana, text="Agregar Vertice", bg="lightblue", fg="black")
        agregar_vertice.place(x=130,y=330)
        #agregar_peso=Button(ventana, text="Agregar Peso", bg="lightblue", fg="black")
        #gregar_peso.place(x=130,y=430)
        agregar_arista=Button(ventana,text="Agregar Arista", bg="lightblue", fg="black")
        agregar_arista.place(x=10,y=430)
        generar=Button(ventana, text="Generar", bg="lightblue", fg="black")
        generar.place(x=480,y=360)



if __name__ == "__main__":
    ventana = Tk()
    aplicacion = interfaz(ventana)
    ventana.mainloop()