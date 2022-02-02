from task1 import Stack
from typing import Any

class ExtendedStack(Stack):
    def get_from_stack(self, item: Any) -> Any:
        if item in self._items:
            item_index = self._items.index(item)
            return self.pop(item_index)
        raise ValueError

stack = ExtendedStack(10)


