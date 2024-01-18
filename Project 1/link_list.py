class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_last(self, key):
        new_node = Node(key)
        current = self.head
        if current is None:
            self.head = new_node
            return
        while current.next is not None:
            if current.key == key:
                return
            current = current.next
        current.next = new_node

    def add_after(self, key_u, key_v):
        current = self.head
        while current is not None:
            if current.key == key_u:
                return
            else:
                if current.key == key_v:
                    new_node = Node(key_u)
                    new_node.next = current.next
                    current.next = new_node
                    return
            current = current.next
        return

    def add_before(self, key_u, key_v):
        current = self.head
        previous = None
        while current is not None:
            if current.key == key_v:
                new_node = Node(key_u)
                if previous is None:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    new_node.next = previous.next
                    previous.next = new_node
                return
            previous = current
            current = current.next
        return

    def remove(self, key):
        current = self.head
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return

            previous = current
            current = current.next
        return

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def __str__(self):
        current = self.head
        string = ""

        while current is not None:
            string += str(current.key) + " "
            current = current.next

        return string

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    linked_list = LinkedList()
    for i in range(n):
        linked_list.add_last(arr[i])
    while True:
        command = input()
        if command == "#":
            break
        command_args = command.split()

        if command_args[0] == "addlast":
            linked_list.add_last(int(command_args[1]))
        elif command_args[0] == "addfirst":
            linked_list.add_first(int(command_args[1]))
        elif command_args[0] == "addafter":
            linked_list.add_after(int(command_args[1]), int(command_args[2]))
        elif command_args[0] == "addbefore":
            linked_list.add_before(int(command_args[1]), int(command_args[2]))
        elif command_args[0] == "remove":
            linked_list.remove(int(command_args[1]))
        elif command_args[0] == "reverse":
            linked_list.reverse()

    print(linked_list)

if __name__ == "__main__":
    main()