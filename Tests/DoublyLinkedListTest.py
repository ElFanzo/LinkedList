from unittest import TestCase, main
from List.DoublyLinkedList import DLinkedList


class TestList(TestCase):

    def setUp(self):
        self._list = DLinkedList()

    def test_addAtHead(self):
        self._list.addAtHead(0)
        self.assertEqual(str(self._list), '0')

        self._list.addAtHead(1, 2)
        self.assertEqual(str(self._list), '1 -- 2 -- 0')

    def test_addAtTail(self):
        self._list.addAtTail(1, 3, 5)
        self.assertEqual(str(self._list), '1 -- 3 -- 5')

        self._list.addAtTail(4)
        self.assertEqual(str(self._list), '1 -- 3 -- 5 -- 4')

    def test_addAtIndex(self):
        self._list.addAtIndex(0, 1, 2)
        self.assertEqual(str(self._list), '1 -- 2')

        self._list.addAtIndex(0, 3, 4)
        self.assertEqual(str(self._list), '3 -- 4 -- 1 -- 2')

        self._list.addAtIndex(3, 5)
        self.assertEqual(str(self._list), '3 -- 4 -- 1 -- 5 -- 2')

        self._list.addAtIndex(5, 6)
        self.assertEqual(str(self._list), '3 -- 4 -- 1 -- 5 -- 2 -- 6')

        with self.assertRaises(IndexError):
            self._list.addAtIndex(99, 1)

    def test_deleteAtIndex(self):
        with self.assertRaises(IndexError):
            self._list.deleteAtIndex(0)

        self._list.addAtHead(1, 2, 3)

        self._list.deleteAtIndex(0)
        self.assertEqual(str(self._list), '2 -- 3')

        self._list.deleteAtIndex(1)
        self.assertEqual(str(self._list), '2')

        with self.assertRaises(IndexError):
            self._list.deleteAtIndex(4)

    def test_popRoot(self):
        self.assertIsNone(self._list.popRoot())

        self._list.addAtHead(1, 2)

        self.assertEqual(self._list.popRoot(), 1)

        self.assertEqual(self._list.popRoot(), 2)

        self.assertIsNone(self._list.popRoot())

    def test_popEnd(self):
        self.assertIsNone(self._list.popEnd())

        self._list.addAtHead(2, 3)

        self.assertEqual(self._list.popEnd(), 3)

        self.assertEqual(self._list.popEnd(), 2)

        self.assertIsNone(self._list.popEnd())

    def test_contain(self):
        self.assertNotIn(3, self._list)

        self._list.addAtHead(3, 5)

        self.assertIn(5, self._list)

        self.assertNotIn(None, self._list)

    def test_reversed(self):
        self._list.addAtHead(1, 2, 5, 14)

        self.assertListEqual(self._list[::-1], [14, 5, 2, 1])

    def test_set(self):
        self._list.addAtHead(3)

        self._list[0] = 1
        self.assertEqual(str(self._list), '1')

        self._list[0] = 2
        self.assertEqual(str(self._list), '2')

        with self.assertRaises(IndexError):
            self._list[1] = 3

        with self.assertRaises(IndexError):
            self._list[-4] = 5

    def test_get(self):
        with self.assertRaises(IndexError):
            x = self._list[0]

        self._list.addAtHead(4, 3)

        self.assertEqual(self._list[0], 4)

        self.assertEqual(self._list[1], 3)

        with self.assertRaises(IndexError):
            x = self._list[4]

    def test_len(self):
        self.assertFalse(len(self._list))

        self._list.addAtHead(4, 5, 1, 2, 3)
        self.assertEqual(len(self._list), 5)

        self._list.deleteAtIndex(0)
        self.assertEqual(len(self._list), 4)


if __name__ == '__main__':
    main()