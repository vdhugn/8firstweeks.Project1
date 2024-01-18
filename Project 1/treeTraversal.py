class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

class FamilyTree:
    def __init__(self):
        self.root = None

    def add_child_parent(self, child_name, parent_name):
        child_node = Node(child_name)
        parent_node = Node(parent_name)

        if self.root is None:
            self.root = parent_node
        else:
            parent_node.children.append(child_node)
            child_node.parent = parent_node

    def descendants(self, name):
        node = self.find_node(name)
        if node is None:
            return 0

        count = 1
        if node.children:
            for child in node.children:
                count += self.descendants(child.name)

        return count

    def generation(self, name):
        node = self.find_node(name)
        if node is None:
            return 0

        count = 0
        while node.parent is not None:
            node = node.parent
            count += 1

        return count

    def find_node(self, name):
        node = self.root
        while node is not None:
            if node.name == name:
                return node

            # Check if the given name is present in the children list of any node in the family tree
            for child in node.children:
                if child.name == name:
                    return child

            node = node.children[0]

        return None


def main():
    family_tree = FamilyTree()

    # Read the child-parent relations from the first block of input
    while True:
        line = input()
        if line == "***":
            break

        child, parent = line.split()
        family_tree.add_child_parent(child, parent)

    # Read the queries from the second block of input and store them in a list
    queries = []
    while True:
        line = input()
        if line == "***":
            break

        cmd, param = line.split()

        queries.append((cmd, param))

    # Iterate over the list of queries and perform the descendants and generation queries
    for cmd, param in queries:
        if cmd == "descendants":
            print(family_tree.descendants(param))
        elif cmd == "generation":
            print(family_tree.generation(param))


if __name__ == "__main__":
    main()