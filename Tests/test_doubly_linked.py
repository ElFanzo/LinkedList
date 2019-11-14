from doubly_linked import List
from Tests.test_singly_linked import TestList


class TestDList(TestList):
    conn_sign = "><"

    def test_double(self):
        self._list.add_at_head(1, 2, 3)
        temp = self._list.end
        temp = temp.prev
        self.assertEqual(temp.val, 2)

        temp = temp.prev
        self.assertEqual(temp.val, 1)

        temp = temp.prev
        self.assertIsNone(temp)

    def get_list(self, *args):
        return List(*args)
