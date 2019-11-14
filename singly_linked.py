class Node:
    """A linked list element class."""

    def __init__(self, value=None, next=None):
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

    def __init__(self, *values):
        self.root = None
        self.end = None

        self._length = 0

        self.add_at_head(*values)

    def add_at_head(self, *values):
        """Add a node(s) before the first element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        for val in values[::-1]:
            self.root = self._gist_add_at_head(val)
            if not self.root.next:
                self.end = self.root

        self._length += len(values)

    def add_at_tail(self, *values):
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

    def add_at_index(self, index, *values):
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

    def delete(self, index):
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

    def pop_root(self):
        """Remove the first node from a linked list and return its value.

        :return: the 1st node value
        """
        if not self:
            return None

        res = self.root.val
        self.delete(0)

        return res

    def pop_end(self):
        """Remove the last node  from a linked list and return its value.

        :return: the last node value
        """
        if len(self) < 2:
            return self.pop_root()

        res = self.end.val
        self.delete(len(self) - 1)

        return res

    def _get(self, index):
        """Get the index-th node in a linked list.

        :return: the index-th node
        """
        if not isinstance(index, int):
            raise TypeError
        if index >= len(self):
            raise IndexError

        if index == 0:
            return self.root
        if index == len(self) - 1:
            return self.end

        if index < 0:
            if abs(index) > len(self):
                raise IndexError
            index += len(self)

        return self._gist_get(index)

    def _gist_add_at_head(self, val):
        return Node(val, self.root)

    def _gist_add_at_tail(self, val):
        return Node(val)

    def _gist_add_at_index(self, temp, val):
        temp.next = Node(val, temp.next)

    def _gist_delete(self, index):
        if index == 0:
            self.root = self.root.next
        elif index == len(self) - 1:
            self.end = self._get(len(self) - 2)
            self.end.next = None
        else:
            temp = self._get(index - 1)
            temp.next = temp.next.next

    def _gist_get(self, index):
        return self._gist_go_to_node(index)

    def _gist_go_to_node(self, index):
        temp = self.root
        for i in range(index):
            temp = temp.next
        return temp

    def __len__(self):
        return self._length

    def __iter__(self):
        for i in range(len(self)):
            yield (self._get(i)).val

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = 0 if not item.start else item.start
            stop = len(self) if not item.stop else item.stop
            step = 1 if not item.step else item.step
            if step < 0:
                start, stop = stop, start
                start -= 1
                stop -= 1

            return [(self._get(i)).val for i in range(start, stop, step)]

        return (self._get(item)).val

    def __setitem__(self, key, value):
        (self._get(key)).val = value

    def __contains__(self, item):
        temp = self.root
        while temp and temp.val != item:
            temp = temp.next

        return temp is not None

    def __add__(self, other):
        first = [i for i in self]
        second = [i for i in other]
        result = self.__class__(*first)
        result.add_at_tail(*second)

        return result

    def __str__(self):
        return self._conn_sign.join(str(i) for i in self)
