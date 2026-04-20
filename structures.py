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
        if self.root is None:
            self.root = Node(process)
        else:
            self._insert_recursive(self.root, process)

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
            steps += 1

            if vruntime == current.process.vruntime:
                return current, steps
            elif vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right

        return None, steps


# Clase SplayTree
class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, process):
        # Igual que BST por ahora (sin splay)
        if self.root is None:
            self.root = Node(process)
        else:
            self._insert_recursive(self.root, process)

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
            steps += 1

            if vruntime == current.process.vruntime:
                return current, steps
            elif vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right

        return None, steps
    
# Referencias bibliográficas:
# Yadav, B. (2025). Binary Tree in Python. GeeksforGeeks. https://www.geeksforgeeks.org/binary-tree-in-python/

