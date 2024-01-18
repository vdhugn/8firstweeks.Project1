class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = Node(value)
        current = self.root
        while True:
            if current is None:
                self.root = new_node
                return
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right
            else:
                return
    def pre_order_traversal(self, node):
        if node is None:
            return
        L = []
        L.append(node.value)
        if node.left is not None:
            L.append(self.pre_order_traversal(node.left))
        if node.right is not None:
            L.append(self.pre_order_traversal(node.right))
        return L

def flatten(L):
    flat_list = []
    for element in L:
        if isinstance(element, list):
            flat_list += flatten(element)
        else:
            flat_list.append(element)
    return flat_list

if __name__ == '__main__':
    bst = BST()
    while True:
        operation = input()
        if operation.startswith("insert"):
            value = int(operation.split(" ")[1])
            bst.insert(value)
        else:
            break
    pre_order_list = bst.pre_order_traversal(bst.root)
    flat_list = flatten(pre_order_list)
    print(" ".join(map(str, flat_list)))