#!/usr/bin/python3
"""Module that defines the Node and SinglyLinkedList"""

class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new node with data and the next node."""
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """Sets the data of the node. The data must be an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Gets the next node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node. The next node must be a Node object or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes an empty linked list."""
        self._head = None

    def __str__(self):
        """Returns a string representation of the linked list. Each node's data is printed on a new line."""
        nodes_data = []
        current_node = self._head
        while current_node is not None:
            nodes_data.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(nodes_data)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order)."""
        new_node = Node(value)

        # If the list is empty or the new node's data is less than the head's data,
        # insert the new node at the beginning of the list.
        if self._head is None or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
            return

        # Otherwise, insert the new node at the correct position in the sorted list.
        previous_node = None
        current_node = self._head
        while current_node is not None and value >= current_node.data:
            previous_node = current_node
            current_node = current_node.next_node

        new_node.next_node = current_node
        previous_node.next_node = new_node

