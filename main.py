from structures import Process, BinarySearchTree, SplayTree, RedBlackTree
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


if __name__ == "__main__":

    # -------------------------
    # ESCENARIO A
    # -------------------------
    print("\n--- ESCENARIO A ---")

    bst = BinarySearchTree()
    splay = SplayTree()
    rb = RedBlackTree()

    processes = []

    for i in range(1000):
        vruntime = random.randint(1, 10000)
        p = Process(i, vruntime)
        processes.append(p)

        bst.insert(p)
        splay.insert(p)
        rb.insert(p)  

    print("1000 procesos insertados en BST, Splay y Red-Black")

    # Visualización (pequeña)
    small_bst = BinarySearchTree()
    for i in range(30):
        vruntime = random.randint(1, 100)
        small_bst.insert(Process(i, vruntime))

    graph = visualize_tree(small_bst.root)
    graph.render("bst_small", format="png", cleanup=True)

    print("Imagen generada: bst_small.png")

    # Búsqueda
    sample = random.sample(processes, 100)

    bst_steps = []
    splay_steps = []
    rb_steps = []

    for p in sample:
        _, steps_bst = bst.search(p.vruntime)
        _, steps_splay = splay.search(p.vruntime)
        _, steps_rb = rb.search(p.vruntime)  

        bst_steps.append(steps_bst)
        splay_steps.append(steps_splay)
        rb_steps.append(steps_rb)

    avg_bst = sum(bst_steps) / len(bst_steps)
    avg_splay = sum(splay_steps) / len(splay_steps)
    avg_rb = sum(rb_steps) / len(rb_steps)

    print(f"Promedio BST: {avg_bst}")
    print(f"Promedio Splay: {avg_splay}")
    print(f"Promedio Red-Black: {avg_rb}")

    # Gráfica
    x = list(range(100))

    plt.figure()
    plt.plot(x, bst_steps, label="BST")
    plt.plot(x, splay_steps, label="Splay")
    plt.plot(x, rb_steps, label="Red-Black")  

    plt.xlabel("Procesos")
    plt.ylabel("Iteraciones")
    plt.title("Escenario A")
    plt.legend()

    plt.savefig("escenario_A.png")
    plt.show()

    print("Gráfica generada: escenario_A.png")


    # -------------------------
    # ESCENARIO B
    # -------------------------
    print("\n--- ESCENARIO B: Llegada Secuencial ---")

    bst_seq = BinarySearchTree()
    splay_seq = SplayTree()
    rb_seq = RedBlackTree()  

    for i in range(1, 1001):
        p = Process(i, i)
        bst_seq.insert(p)
        splay_seq.insert(p)
        rb_seq.insert(p)  

    print("Procesos insertados en orden")

    node_bst, steps_bst = bst_seq.search(1000)
    node_splay, steps_splay = splay_seq.search(1000)
    node_rb, steps_rb = rb_seq.search(1000)  

    print(f"BST -> Iteraciones: {steps_bst}")
    print(f"Splay -> Iteraciones: {steps_splay}")
    print(f"Red-Black -> Iteraciones: {steps_rb}")  

    # Visualización pequeña
    small_seq = BinarySearchTree()

    for i in range(1, 20):
        small_seq.insert(Process(i, i))

    graph = visualize_tree(small_seq.root)
    graph.render("bst_secuencial", format="png", cleanup=True)

    print("Imagen generada: bst_secuencial.png")
    

    # -------------------------
    # ESCENARIO C
    # -------------------------
    print("\n--- ESCENARIO C: Proceso Frecuente ---")

    bst = BinarySearchTree()
    splay = SplayTree()
    rb = RedBlackTree()  

    processes = []

    for i in range(1000):
        vruntime = random.randint(1, 10000)
        p = Process(i, vruntime)
        processes.append(p)

        bst.insert(p)
        splay.insert(p)
        rb.insert(p)  

    print("Árboles generados")

    target = random.choice(processes)
    print(f"Proceso elegido (vruntime): {target.vruntime}")

    bst_steps = []
    splay_steps = []
    rb_steps = []  

    for i in range(50):
        _, steps_bst = bst.search(target.vruntime)
        _, steps_splay = splay.search(target.vruntime)
        _, steps_rb = rb.search(target.vruntime)  

        bst_steps.append(steps_bst)
        splay_steps.append(steps_splay)
        rb_steps.append(steps_rb)

        print(f"Búsqueda {i+1}: BST={steps_bst}, Splay={steps_splay}, RB={steps_rb}")

    avg_bst = sum(bst_steps) / 50
    avg_splay = sum(splay_steps) / 50
    avg_rb = sum(rb_steps) / 50

    print(f"\nPromedio BST: {avg_bst}")
    print(f"Promedio Splay: {avg_splay}")
    print(f"Promedio Red-Black: {avg_rb}")

    # Gráfica
    plt.figure()
    plt.plot(range(50), bst_steps, label="BST")
    plt.plot(range(50), splay_steps, label="Splay")
    plt.plot(range(50), rb_steps, label="Red-Black")  

    plt.xlabel("Número de búsqueda")
    plt.ylabel("Iteraciones")
    plt.title("Escenario C - Proceso Frecuente")
    plt.legend()

    plt.savefig("escenario_C.png")
    plt.show()

    print("Gráfica generada: escenario_C.png")