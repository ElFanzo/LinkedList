class Node:
    """A linked list element class."""

    def __init__(self, value=None, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next


class DLinkedList:
    """A linked list class, whose elements are instances of the Node class.

    Args:
        *values: 1 or more values of a list

    Attributes:
        root: the 1st element
        end: the last element
    """

    def __init__(self, *values):
        self.root = None
        self.end = None

        self.__length = 0

        self.add_at_head(*values)

    def add_at_head(self, *values):
        """Add a node(s) before the first element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        for val in values[::-1]:
            node = Node(val, None, self.root)
            try:
                self.root.prev = node
            except AttributeError:
                pass
            self.root = node
            if not self.root.next:
                self.end = self.root

        self.__length += len(values)

    def add_at_tail(self, *values):
        """Add a node(s) after the last element of a linked list.

        :param *values: 1 or more values of the node(s)
        """
        if not self.end:
            self.add_at_head(*values)
        else:
            for val in values:
                self.end.next = Node(val, self.end)
                self.end = self.end.next

            self.__length += len(values)

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
            for val in values:
                temp = self._get(index - 1)
                node = Node(val, temp, temp.next)
                temp.next = node
                node.next.prev = node

            self.__length += len(values)
        else:
            raise IndexError

    def delete_at_index(self, index):
        """Delete the index-th node in a linked list, if the index is valid.

        :param index: node index
        """
        if 0 <= index < len(self):
            if len(self) == 1:
                self.root = None
                self.end = None
            elif index == 0:
                self.root = self.root.next
                self.root.prev = None
            elif index == len(self) - 1:
                self.end = self.end.prev
                self.end.next = None
            else:
                temp = self._get(index - 1)
                temp.next = temp.next.next
                temp.next.prev = temp

            self.__length -= 1
        else:
            raise IndexError

    def pop_root(self):
        """Remove the first node from a linked list and return its value.

        :return: the 1st node value
        """
        if not self:
            return None

        res = self.root.val
        self.delete_at_index(0)

        return res

    def pop_end(self):
        """Remove the last node from a linked list and return its value.

        :return: the last node value
        """
        if len(self) < 2:
            return self.pop_root()

        res = self.end.val
        self.delete_at_index(len(self) - 1)

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

        temp = None
        if index <= len(self) // 2:
            temp = self.root
            for i in range(index):
                temp = temp.next
        else:
            temp = self.end
            for i in range(len(self) - index - 1):
                temp = temp.prev

        return temp

    def __len__(self):
        return self.__length

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
        result = DLinkedList(*first)
        result.add_at_tail(*second)

        return result

    def __str__(self):
        return " >< ".join(str(i) for i in self)