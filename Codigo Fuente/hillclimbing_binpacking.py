import numpy as np
from data_in import read
from graphics import show_results

def heuristic(container,new_box,container_size):
    """
    Funcion heuristica
    """
    h = 0
    for box in container:#Suma las cajas dentro del contenedor
        h += box#..............Para conocer el espacio ocupado
    h += new_box#...Suma el valor de la caja candidata a entrar
    if h > container_size: #Si excede el tamanho del contenedor
        return 0  #retornará el valor cero
    else: 
        return h #Se retorna el calculo de la heuristica

def find_best_box(container,boxes,container_size):
    """
    Función para encontrar la mejor opción
    """
    heuristics = [] #....................Esta lista de heuristica mantiene los indices de las cajas 
    for box in boxes:#.......Asi que heuristics[0] corresponde a la heuristica de la caja candidata [0]
        heuristics.append(heuristic(container,box,container_size))#Se hace el calculo heuristico para los candidatos
    if heuristics: #..................Si se logró correctamente entonces obtendremos el valor mayor
        max_h = max(heuristics)
        if max_h != 0: #Si la heuristica maxima tiene un valor diferente a cero
            selection = heuristics.index(max_h) #Seleccionaremos la mejor caja candidata
            container.append(boxes.pop(selection)) #Quitamos la caja seleccionada y la agregamos al contenedor
            return True #Si se tuvo exito
    return False #Si no se tuvo exito

def hill_climbing(container_size,boxes):
    containers = [[boxes.pop(0)]]#....................................Ingresa la primera caja de la lista 
    print("Packing Boxes",containers)#....................a un contenedor
    index = 0
    while boxes:
        if not find_best_box(containers[index],boxes,container_size):#Función para encontrar la caja que mejor se adapta
            containers.append([boxes.pop(0)])#...Crea un nuevo contenedor con la primera caja de la lista de ese momento
            index += 1#........Cambia al siguiente contenedor, ya que en el anterior no puede entrar ninguna de las cajas
        print("Packing Boxes",containers)
    print("Solved")
    return containers

