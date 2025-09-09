from model.nodo import Nodo as Node
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo_nodo = Node(data)
        if not self.head:
            self.head = nuevo_nodo
            return
        last = self.head
        while last.siguiente:
            last = last.siguiente
        last.siguiente = nuevo_nodo

    def display(self):
        current = self.head
        while current:
            print(current.dato, end=" -> ")
            current = current.siguiente
        print("None")