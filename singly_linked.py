import typing
from typing import Optional, Union

ListType = typing.List[Union[int, float]]
NodeValue = Union[int, float]


class Node:
    """A linked list element class."""

    def __init__(
        self,
        value: Optional[NodeValue] = None,
        next: Optional["Node"] = None
    ):
        self.val = value
        self.next = next


class List:
    """A linked list class, whose elements are instances of the Node class.

    Args:
        *values: 1 or more values of a list

    Attributes:
        root: the 1st element
        end: the last element
    """

    _conn_sign = " -> "

    def __init__(self, *values: NodeValue):
        self.root = None
        self.end = None

        self._length = 0

        self.add_at_head(*values)

    def add_at_head(self, *values: NodeValue):
        """Add a node(s) before the first element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        for val in values[::-1]:
            self.root = self._gist_add_at_head(val)
            if not self.root.next:
                self.end = self.root

        self._length += len(values)

    def add_at_tail(self, *values: NodeValue):
        """Add a node(s) after the last element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        if not self.end:
            self.add_at_head(*values)
        else:
            for val in values:
                self.end.next = self._gist_add_at_tail(val)
                self.end = self.end.next

            self._length += len(values)

    def add_at_index(self, index: int, *values: NodeValue):
        """Add a node(s) before the index-th node in a linked list.

        If the index equals to the length of the linked list, the node will be
        appended to the end of the linked list.

        :param index: the node index
        :param *values: 1 or more values of the node(s)
        """
        if index == 0:
            self.add_at_head(*values)
        elif index == len(self):
            self.add_at_tail(*values)
        elif 0 < index < len(self):
            for val in values[::-1]:
                temp = self._get(index - 1)
                self._gist_add_at_index(temp, val)

            self._length += len(values)
        else:
            raise IndexError

    def delete(self, index: int):
        """Delete the index-th node in a linked list, if the index is valid.

        :param index: the node index
        """
        if 0 <= index < len(self):
            if len(self) == 1:
                self.root = None
                self.end = None
            else:
                self._gist_delete(index)

            self._length -= 1
        else:
            raise IndexError

    def pop_root(self) -> Optional[NodeValue]:
        """Remove the first node from a linked list and return its value.

        :return: the 1st node value
        """
        if not self:
            return None

        res = self.root.val
        self.delete(0)

        return res

    def pop_end(self) -> Optional[NodeValue]:
        """Remove the last node  from a linked list and return its value.

        :return: the last node value
        """
        if len(self) < 2:
            return self.pop_root()

        res = self.end.val
        self.delete(len(self) - 1)

        return res

    def _get(self, index) -> Optional[Node]:
        """Get the index-th node in a linked list.

        :return: the index-th node
        """
        if not isinstance(index, int):
            raise TypeError
        if not (-len(self) <= index < len(self)):
            raise IndexError

        if index == 0:
            return self.root
        if index == len(self) - 1:
            return self.end

        if index < 0:
            index += len(self)

        return self._gist_get(index)

    def _gist_add_at_head(self, val: NodeValue) -> Node:
        return Node(val, self.root)

    def _gist_add_at_tail(self, val: NodeValue) -> Node:
        return Node(val)

    def _gist_add_at_index(self, temp: Node, val: NodeValue):
        temp.next = Node(val, temp.next)

    def _gist_delete(self, index: int):
        if index == 0:
            self.root = self.root.next
        elif index == len(self) - 1:
            self.end = self._get(len(self) - 2)
            self.end.next = None
        else:
            temp = self._get(index - 1)
            temp.next = temp.next.next

    def _gist_get(self, index: int) -> Node:
        return self._gist_go_to_node(index)

    def _gist_go_to_node(self, index: int) -> Node:
        temp = self.root
        for i in range(index):
            temp = temp.next
        return temp

    def __len__(self):
        return self._length

    def __iter__(self) -> NodeValue:
        for i in range(len(self)):
            yield (self._get(i)).val

    def __getitem__(self, item) -> Union[int, float, ListType]:
        if isinstance(item, slice):
            step = item.step or 1
            if step < 0 and (item.start is None or item.stop is None):
                start = item.start or len(self) - 1
                stop = item.stop or -1
            else:
                start = item.start or 0
                stop = len(self) if item.stop is None else item.stop

                if start < 0:
                    start += len(self)
                if stop < 0:
                    stop += len(self)

            return [
                (self._get(i)).val
                for i in range(start, stop, step)
                if 0 <= i < len(self)
            ]

        return (self._get(item)).val

    def __setitem__(self, key: int, value: Optional[NodeValue]):
        (self._get(key)).val = value

    def __contains__(self, item: Optional[NodeValue]) -> bool:
        temp = self.root
        while temp and temp.val != item:
            temp = temp.next

        return temp is not None

    def __add__(self, other: "List") -> "List":
        first = [i for i in self]
        second = [i for i in other]
        result = self.__class__(*first)
        result.add_at_tail(*second)

        return result

    def __str__(self):
        return self._conn_sign.join(str(i) for i in self)
