import numpy as np
import matplotlib.pyplot as plt

#EN CASO EXISTA MÁS DE UN CONTENEDOR
def multi_draw(container_size,containers,ax):
    for container, graph, n in zip(containers,ax,range(len(containers))):
        btm = 0
        container_label = "Contenedor " + str(n+1)
        for i in range(len(container)):
            if i == len(container) - 1:
                graph.bar(container_label, container[i],  yerr=[[0],[container_size-btm-container[i]]], edgecolor="black",linewidth=1, bottom=btm)
            elif i == 0:
                graph.bar(container_label, container[i],  edgecolor="black",linewidth=1)
            else:
                graph.bar(container_label, container[i],  edgecolor="black",linewidth=1, bottom=btm)
            btm += container[i]
#EN CASO EXISTA SOLO UN CONTENEDOR
def single_draw(container_size,containers,ax):
    for container, n in zip(containers,range(len(containers))):
        btm = 0
        container_label = "Contenedor " + str(n+1)
        for i in range(len(container)):
            if i == len(container) - 1:
                ax.bar(container_label, container[i],  yerr=[[0],[container_size-btm-container[i]]], edgecolor="black",linewidth=1, bottom=btm)
            elif i == 0:
                ax.bar(container_label, container[i],  edgecolor="black",linewidth=1)
            else:
                ax.bar(container_label, container[i],  edgecolor="black",linewidth=1, bottom=btm)
            btm += container[i]

def show_results(container_size,containers):
    fig, ax = plt.subplots(1,len(containers),figsize=(10+len(containers),7),sharey=True)
    if len(containers) == 1:
        single_draw(container_size,containers,ax)
        ax.set_ylabel('Espacio ocupado', fontsize = 20)
    else:
        multi_draw(container_size,containers,ax)
        ax[0].set_ylabel('Espacio ocupado', fontsize = 20)
    fig.suptitle('Conjunto de Contenedores', fontsize = 20)
    plt.show()