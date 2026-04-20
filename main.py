from structures import Process, BinarySearchTree, SplayTree
import random
import matplotlib.pyplot as plt
from graphviz import Digraph


# VISUALIZACIÓN (Graphviz)

def visualize_tree(root):
    dot = Digraph()

    def add_nodes_edges(node):
        if node is None:
            return

        dot.node(str(id(node)), f"{node.process.vruntime}")

        if node.left:
            dot.edge(str(id(node)), str(id(node.left)))
            add_nodes_edges(node.left)

        if node.right:
            dot.edge(str(id(node)), str(id(node.right)))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    return dot


# ESCENARIO A

if __name__ == "__main__":

    # Crear árboles
    bst = BinarySearchTree()
    splay = SplayTree()

    # Generar 1000 procesos aleatorios
    processes = []
    for i in range(1000):
        vruntime = random.randint(1, 10000)
        p = Process(i, vruntime)
        processes.append(p)

        bst.insert(p)
        splay.insert(p)

    print("1000 procesos insertados en BST y Splay")


    # VISUALIZACIÓN (solo una muestra)
  
    small_bst = BinarySearchTree()
    for i in range(30):
        vruntime = random.randint(1, 100)
        small_bst.insert(Process(i, vruntime))

    graph = visualize_tree(small_bst.root)
    graph.render("bst_small", format="png", cleanup=True)

    print("Imagen generada: bst_small.png")

    
    # SELECCIONAR 100 PROCESOS ALEATORIOS
    
    sample = random.sample(processes, 100)

    bst_steps = []
    splay_steps = []


    # BÚSQUEDA Y MEDICIÓN
  
    for p in sample:
        _, steps_bst = bst.search(p.vruntime)
        _, steps_splay = splay.search(p.vruntime)

        bst_steps.append(steps_bst)
        splay_steps.append(steps_splay)


    # PROMEDIOS

    avg_bst = sum(bst_steps) / len(bst_steps)
    avg_splay = sum(splay_steps) / len(splay_steps)

    print(f"Promedio de iteraciones BST: {avg_bst}")
    print(f"Promedio de iteraciones Splay: {avg_splay}")


    # GRÁFICA

    x = list(range(100))  # procesos 0–99

    plt.figure()
    plt.plot(x, bst_steps, label="BST")
    plt.plot(x, splay_steps, label="Splay")

    plt.xlabel("Procesos")
    plt.ylabel("Cantidad de iteraciones")
    plt.title("Escenario A - Comparación de búsquedas")
    plt.legend()

    plt.savefig("escenario_A.png")
    plt.show()

    print("Gráfica generada: escenario_A.png")