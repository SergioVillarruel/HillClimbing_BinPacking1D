import numpy as np

def text_to_list(string):
    string = string.split(",")
    data_set = []
    for data in string:
        data_set.append(int(data))
    return data_set

def read(path):
    """
    Función para leer un archivo y obtener los valores correspondientes
    retorna la capacidad de los contenedor y el número de cajas 
    ordenadas de mayor a menor
    """
    #OBTENCIÓN DE ARCHIVOS
    file = open(path,"r")
    f1=file.readlines()
    #FILTADO DEL ARCHIVO
    data = []
    boxes = []
    for line in f1:
        data.append([str(n) for n in line.split(' ')])
    #SE OBTIENEN LOS DATOS
    container_size = int(data[0][0])
    for i in range(1,len(data)):
        n_box = int(data[i][0])
        for time in range(n_box):
            valor = int(data[i][1])
            if valor > container_size: return 0,0
            boxes.append(valor)
    return container_size, boxes
