from typing import Optional, Union

import singly_linked

NodeValue = Union[int, float]


class Node(singly_linked.Node):
    """A linked list element class."""

    def __init__(
        self,
        value: Optional[NodeValue] = None,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None
    ):
        super().__init__(value=value, next=next)
        self.prev = prev


class List(singly_linked.List):
    """A linked list class, whose elements are instances of the Node class."""

    _conn_sign = " >< "

    def _gist_add_at_head(self, val: NodeValue) -> Node:
        node = Node(val, None, self.root)
        try:
            self.root.prev = node
        except AttributeError:
            pass
        return node

    def _gist_add_at_tail(self, val: NodeValue) -> Node:
        return Node(val, self.end)

    def _gist_add_at_index(self, temp: Node, val: NodeValue):
        temp.next = Node(val, temp, temp.next)
        temp.next.next.prev = temp.next

    def _gist_delete(self, index: int):
        if index == 0:
            self.root = self.root.next
            self.root.prev = None
        elif index == len(self) - 1:
            self.end = self.end.prev
            self.end.next = None
        else:
            temp = self._get(index - 1)
            temp.next = temp.next.next
            temp.next.prev = temp

    def _gist_get(self, index: int) -> Node:
        if index <= len(self) // 2:
            return self._gist_go_to_node(index)

        temp = self.end
        for i in range(len(self) - index - 1):
            temp = temp.prev

        return temp
