# Clase Process
class Process:
    def __init__(self, pid, vruntime):
        self.pid = pid
        self.vruntime = vruntime


# Clase Node
class Node:
    def __init__(self, process):
        self.process = process
        self.left = None
        self.right = None


# Clase BinarySearchTree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, process):
        new_node = Node(process)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if process.vruntime < current.process.vruntime:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def _insert_recursive(self, current_node, process):
        if process.vruntime < current_node.process.vruntime:
            if current_node.left is None:
                current_node.left = Node(process)
            else:
                self._insert_recursive(current_node.left, process)
        else:
            if current_node.right is None:
                current_node.right = Node(process)
            else:
                self._insert_recursive(current_node.right, process)

    def search(self, vruntime):
        current = self.root
        steps = 0

        while current is not None:
            if vruntime == current.process.vruntime:
                return current, steps

            elif vruntime < current.process.vruntime:
                current = current.left
                steps += 1  # solo cuenta cuando bajas

            else:
                current = current.right
                steps += 1  # solo cuenta cuando bajas

        return None, steps

# Clase SplayTree
class SplayTree:
    def __init__(self):
        self.root = None

    
    # Rotaciones
    
    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    
    # SPLAY (versión simplificada)
   
    def _splay(self, root, vruntime):
        if root is None or root.process.vruntime == vruntime:
            return root

        # Caso izquierda
        if vruntime < root.process.vruntime:
            if root.left is None:
                return root

            # Zig-Zig
            if vruntime < root.left.process.vruntime:
                root.left.left = self._splay(root.left.left, vruntime)
                root = self._rotate_right(root)

            # Zig-Zag
            elif vruntime > root.left.process.vruntime:
                root.left.right = self._splay(root.left.right, vruntime)
                if root.left.right:
                    root.left = self._rotate_left(root.left)

            return root if root.left is None else self._rotate_right(root)

        # Caso derecha
        else:
            if root.right is None:
                return root

            # Zag-Zag
            if vruntime > root.right.process.vruntime:
                root.right.right = self._splay(root.right.right, vruntime)
                root = self._rotate_left(root)

            # Zag-Zig
            elif vruntime < root.right.process.vruntime:
                root.right.left = self._splay(root.right.left, vruntime)
                if root.right.left:
                    root.right = self._rotate_right(root.right)

            return root if root.right is None else self._rotate_left(root)


    # Insert (básico)

    def insert(self, process):
        if self.root is None:
            self.root = Node(process)
            return

        self.root = self._splay(self.root, process.vruntime)

        if process.vruntime < self.root.process.vruntime:
            new_node = Node(process)
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
            self.root = new_node

        elif process.vruntime > self.root.process.vruntime:
            new_node = Node(process)
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
            self.root = new_node

        # si es igual, no insertamos duplicado

    # Search con SPLAY

    def search(self, vruntime):
        steps = 0
        current = self.root

        # contar pasos como BST normal
        while current is not None:
            if vruntime == current.process.vruntime:
                break
            elif vruntime < current.process.vruntime:
                current = current.left
                steps += 1
            else:
                current = current.right
                steps += 1

        # hacer splay (mueve el nodo al root)
        self.root = self._splay(self.root, vruntime)

        if self.root and self.root.process.vruntime == vruntime:
            return self.root, steps

        return None, steps

# Referencias bibliográficas:
# Yadav, B. (2025). Binary Tree in Python. GeeksforGeeks. https://www.geeksforgeeks.org/binary-tree-in-python/

