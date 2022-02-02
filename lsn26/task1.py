from typing import Any, Union, Optional

class Stack:
    def __init__(self, items_limit: int) -> None:
        self._items = []
        self._limit = items_limit

    def push(self, item: Any) -> Union[bool, Exception]:
        if len(self._items) < self._limit:
            self._items.append(item)
            return True
        raise Exception('Stack overflow')
    
    def pop(self, index: int = -1) -> Any:
        if not self._items:
            raise IndexError
        return self._items.pop(index)

    def __repr__(self) -> str:
        if self._items:
            show_stack = ''
            for item in reversed(self._items):
                show_stack += item
            return show_stack
        return 'Stack is empty'
