#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = self.head

        # first case, no other nodes
        if not self.head:
            new_node.next = new_node
        else:
            # second case, there is a node in the list
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node
    def append(self, data):
        # first case, there is no head
        # set head to data passed in
        # set pointer to next node as head (itself)
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            # second case, there is a node already
            # set new node equal to the data passed in
            # traverse the list until we hit the node that points to the head
            # have that node point to new_node
            # set new_node to point to head
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()

