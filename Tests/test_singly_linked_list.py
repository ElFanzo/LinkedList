from unittest import TestCase, main
from singly_linked_list import SinglyLinkedList


class TestList(TestCase):
    def setUp(self):
        self._list = SinglyLinkedList()

    def test_add_at_head(self):
        self._list.add_at_head(0)
        self.assertListEqual(self._list[:], [0])

        self._list.add_at_head(1, 2)
        self.assertListEqual(self._list[:], [1, 2, 0])

    def test_add_at_tail(self):
        self._list.add_at_tail(1, 3, 5)
        self.assertListEqual(self._list[:], [1, 3, 5])

        self._list.add_at_tail(4)
        self.assertListEqual(self._list[:], [1, 3, 5, 4])

    def test_add_at_index(self):
        self._list.add_at_index(0, 1, 2)
        self.assertListEqual(self._list[:], [1, 2])

        self._list.add_at_index(0, 3, 4)
        self.assertListEqual(self._list[:], [3, 4, 1, 2])

        self._list.add_at_index(3, 5)
        self.assertListEqual(self._list[:], [3, 4, 1, 5, 2])

        self._list.add_at_index(5, 6)
        self.assertListEqual(self._list[:], [3, 4, 1, 5, 2, 6])

        with self.assertRaises(IndexError):
            self._list.add_at_index(99, 1)

    def test_delete_at_index(self):
        with self.assertRaises(IndexError):
            self._list.delete_at_index(0)

        self._list.add_at_head(1, 2, 3)

        self._list.delete_at_index(0)
        self.assertListEqual(self._list[:], [2, 3])

        self._list.delete_at_index(1)
        self.assertListEqual(self._list[:], [2])

        with self.assertRaises(IndexError):
            self._list.delete_at_index(4)

    def test_pop_root(self):
        self.assertIsNone(self._list.pop_root())

        self._list.add_at_head(1, 2)

        self.assertEqual(self._list.pop_root(), 1)
        self.assertListEqual(self._list[:], [2])

        self.assertEqual(self._list.pop_root(), 2)
        self.assertListEqual(self._list[:], [])

        self.assertIsNone(self._list.pop_root())

    def test_pop_end(self):
        self.assertIsNone(self._list.pop_end())

        self._list.add_at_head(2, 3)

        self.assertEqual(self._list.pop_end(), 3)
        self.assertListEqual(self._list[:], [2])

        self.assertEqual(self._list.pop_end(), 2)
        self.assertListEqual(self._list[:], [])

        self.assertIsNone(self._list.pop_end())

    def test_contain(self):
        self.assertNotIn(3, self._list)

        self._list.add_at_head(3, 5)

        self.assertIn(5, self._list)

        self.assertNotIn(None, self._list)

    def test_reversed(self):
        self._list.add_at_head(1, 2, 5, 14)

        self.assertListEqual(self._list[::-1], [14, 5, 2, 1])

    def test_set(self):
        self._list.add_at_head(3)

        self._list[0] = 1
        self.assertListEqual(self._list[:], [1])

        self._list[0] = 2
        self.assertListEqual(self._list[:], [2])

        with self.assertRaises(IndexError):
            self._list[1] = 3

        with self.assertRaises(IndexError):
            self._list[-4] = 5

    def test_get(self):
        with self.assertRaises(IndexError):
            x = self._list[0]

        self._list.add_at_head(4, 3)

        self.assertEqual(self._list[0], 4)

        self.assertEqual(self._list[1], 3)

        with self.assertRaises(IndexError):
            x = self._list[4]

    def test_len(self):
        self.assertFalse(len(self._list))

        self._list.add_at_head(4, 5, 1, 2, 3)
        self.assertEqual(len(self._list), 5)

        self._list.delete_at_index(0)
        self.assertEqual(len(self._list), 4)

    def test_add(self):
        self._list.add_at_head(2, 4, 6)
        temp = SinglyLinkedList(1, 3, 5)
        temp = self._list + temp
        self.assertListEqual(temp[:], [2, 4, 6, 1, 3, 5])

        temp = SinglyLinkedList()
        temp = self._list + temp
        self.assertListEqual(temp[:], [2, 4, 6])

        temp = SinglyLinkedList(1)
        temp = self._list + temp
        self.assertListEqual(temp[:], [2, 4, 6, 1])

        temp = SinglyLinkedList(0) + SinglyLinkedList(1)
        self.assertListEqual(temp[:], [0, 1])

        temp = SinglyLinkedList() + SinglyLinkedList()
        self.assertListEqual(temp[:], [])

    def test_str(self):
        self.assertEqual(str(self._list), "")

        self._list.add_at_head(10)
        self.assertEqual(str(self._list), "10")

        self._list.add_at_tail(4, 5, 13)
        self.assertEqual(str(self._list), "10 -> 4 -> 5 -> 13")

        self._list.delete_at_index(0)
        self.assertEqual(str(self._list), "4 -> 5 -> 13")


if __name__ == "__main__":
    main()
