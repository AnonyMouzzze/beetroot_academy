from typing import Any
from node import Node


class Stack:
    def __init__(self, head: Node=None) -> None:
        self._head = head
        self._length = 0

    def add(self, data: Any) -> Node:
        new_node = Node(data, self._head)
        self._head = new_node
        self._length += 1
        return new_node

    def pop(self) -> Node:
        head_node = self._head
        self._head = self._head.next_node
        return head_node

    def __repr__(self) -> str:
        res = ''
        current_node = self._head
        while current_node:
            res += str(current_node.data) + ' -> '
            current_node = current_node.next_node
        return res


stack = Stack()

stack.add(1)
stack.add(2)
stack.add(3)
print(stack)
stack.pop()
print(stack)
