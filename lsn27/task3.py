from node import Node

class Queue:
    def __init__(self, head: Node=None, tail: Node=None):
        self._head = head
        self._tail = tail

    def add(self, data):
        new_node = Node(data)
        if not self._head:
            self._head, self._tail = new_node, new_node
        else:
            self._tail.next_node = new_node
            self._tail = new_node
            
    def pop(self):
        current_node = self._head
        self._head = self._head.next_node
        return current_node

    def __repr__(self):
        res = ''
        current_node = self._head
        while current_node:
            res += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        return res