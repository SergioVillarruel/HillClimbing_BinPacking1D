import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox
from data_in import read
from data_in import text_to_list
import numpy as np
from hillclimbing_binpacking import hill_climbing
from graphics import show_results

class MyWindow:
    def __init__(self, win):
        container_size = 3
        #LABELS
        self.lbl1=Label(win, text='Altura de contenedores:')
        self.lbl2=Label(win, text='Lista de alturas de cajas:')
        self.lbl3=Label(win, text='Optimización de Bin Packing de una dimensión',font=("Arial Bold",18))
        self.lbl1.place(x=50, y=70)
        self.lbl2.place(x=45, y=120)
        self.lbl3.place(x=25, y=20)
        #textScroll
        self.txt=scrolledtext.ScrolledText(window,width=40,height=10)
        self.txt.grid(column=0,row=0)
        self.txt.place(x=465,y=50)
        #RADIO BUTTON
        self.v0 = IntVar()
        self.v0.set(0)
        self.r1 = Radiobutton(win,text="Descendente", variable=self.v0, value= 0)
        self.r2 = Radiobutton(win,text="Ascendente", variable=self.v0, value= 1)
        self.r3 = Radiobutton(win,text="Desordenado", variable=self.v0, value= 2)
        self.r1.place(x=50,y=160)
        self.r2.place(x=170,y=160)
        self.r3.place(x=290,y=160)
        #INPUTS
        self.t1=Entry()
        self.t1.insert(END,str(container_size))
        self.t2=Entry()
        self.t2.insert(END,"3,2,2,1,1")
        self.t1.place(x=200, y=70)
        self.t2.place(x=200, y=120)
        #BUTTONS
        self.b1=Button(win, text='Ingresar .txt', command=self.read_txt)
        self.b2=Button(win, text='Optimizar',command=self.start)
        self.b1.place(x=150, y=200)
        self.b2.place(x=250, y=200)
   
    def read_txt(self):
        path = fd.askopenfilename()
        container_size, boxes = read(path)
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        var_boxes = str(boxes)
        var_boxes = var_boxes[1:-1]
        #Ambos valores son 0 cuando una caja excede la altura del contenedor
        if (container_size == 0) and (boxes == 0):
            messagebox.showerror("ERROR DE LECTURA", "La altura de las caja deben ser menores a la altura del contenedor")
        else:
            self.t1.insert(END,str(container_size))
            self.t2.insert(END,var_boxes)
    def start(self):
        #obtención de datos
        container_size = int(self.t1.get())
        boxes = text_to_list(self.t2.get())
        check = True
        #Verificar que las cajas no excedan a la altura del contenedor
        for box in boxes:
            if box > container_size: check = False
        #Verifica que el contenedor tenga un espacio y no sea nulo
        if container_size < 1: check = False
        if not check:
            messagebox.showerror("ERROR DE LECTURA", "La altura de las caja deben ser menores a la altura del contenedor")
        else:
            #SE CONFIGURA EL ESTADO INICIAL
            if self.v0.get() == 0:
                boxes.sort(reverse=True)
            elif self.v0.get() == 1:
                boxes.sort()
            var_boxes = str(boxes)
            var_boxes = var_boxes[1:-1]
            self.txt.insert(END,"RESULTADOS\n----------------------------------------\nLas alturas de las cajas a colocar son  las siguientes: " + str(var_boxes) + "\n")
            #SE EJECUTA EL ALGORITMO DE OPTIMIZACIÓN
            start = time.time()
            containers = hill_climbing(container_size,boxes)
            end = time.time()
            print("Algorithm Time Execution:",(end-start)*1000)
            self.txt.insert(END,"La solución óptima local encontrada es  distribuir las cajas en " + str(len(containers))+" contenedores\n")
            np_containers = np.array(containers)
            self.txt.insert(END,"Agrupados de la siguiente manera:\n")
            for container,i in zip(np_containers,range(len(np_containers))):
                self.txt.insert(END,"Contenedor "+str(i+1)+": "+str(container)+"\n")
            self.txt.insert(END,"\n")
            #MUESTRA LOS RESULTADOS GRAFICAMENTE
            show_results(container_size,containers)

window=Tk()
mywin=MyWindow(window)
window.title('BIN PACKING DE UNA DIMENSION')
window.geometry("800x250+10+10")
window.mainloop()
