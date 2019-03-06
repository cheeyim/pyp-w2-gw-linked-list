from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=[]):
        self.elements = []
        self.start = None
        self.end = None

        if elements is not None:
            self.traverse(elements)

    def traverse(self, elements):
        for element in elements:
            self.append(element)

    def __eq__(self, other):
        return not self.__ne__(other)

    def __ne__(self, other):
        return self.elements != other.elements

    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        new_list = self.elements.copy()
        new_list.extend(other.elements)
        return LinkedList(new_list)

    def __iadd__(self, other):
        return self + other

    def __str__(self):
        return "[{}]".format(", ".join([str(element) for element in self.elements]))

    def append(self, element):

        node = Node(element)
        self.elements.append(element)

        if self.start is None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def count(self):
        return len(self.elements)

    def pop(self, index=None):
        if self.count() == 0:
            raise IndexError

        if index is not None:
            return self.elements.pop(index)
        return self.elements.pop()