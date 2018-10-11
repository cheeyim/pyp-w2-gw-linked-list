from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None): 
        self.elements = []
        self.start = None
        self.end = None

        if elements is not None:
            self.traverse(elements)

    def traverse(self, elements):
        for elem in elements:
            self.append(elem)

    def prev_node(self):
        if self.count() <= 1:
            return

        return self.elements[self.count() - 2] 

    def __str__(self):
        return "[{}]".format(", ".join([str(element.elem) for element in self.elements]) )
            
    def __len__(self):
        pass

    def __iter__(self):
        return self

    # TODO: Why only on child works ?
    def __getitem__(self, index):
        if len(self.elements) < index:
            raise IndexError
        return self.elements[index].elem

    def __add__(self, other):

        new_linked_list = LinkedList()
        new_element_list = self.elements + other.elements
        
        for element in new_element_list:
            new_linked_list.append(element.elem)

        return new_linked_list

    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):
        return all([a == b for a, b in zip(self.elements, other.elements) ])

    def append(self, elem):
        node = Node(elem)
        self.elements.append(node)

        if self.start is None: 
            self.start = node
        else :
            prev = self.prev_node()
            prev.next = node
        self.end = node
        
    def count(self):
        return len(self.elements)

    def pop(self, index=None):
        if self.count() == 0 or (index is not None and self.count() <= index):
            raise IndexError 

        # if self.count() > 1:
        #     prev = self.prev_node()
        #     self.end = prev
        
        return self.elements.pop().elem if index is None else self.elements.pop(index).elem