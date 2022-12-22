import unittest
from arrays import sumaLista, exitsElement, findElement, reverseList, multList


class TestArrays(unittest.TestCase):

    def test_sumaLista(self):
        res = sumaLista([1, 2, 3, 4, 5])
        self.assertEqual(res, 15)

    def test_exitsElement(self):
        res = exitsElement(2, [1, 2, 3, 4, 5])
        self.assertTrue(res)

    def test_findElement(self):
        res = findElement(2, [1, 2, 3, 4, 5])
        self.assertIs(res, 2)

    def test_reverseList(self):
        res = reverseList([1, 2, 3, 4, 5])
        self.assertEqual(res, [5, 4, 3, 2, 1])

    def test_multLista(self):
        res = multList([5, 4, 3, 2, 1])
        self.assertEqual(res, 120)


if __name__ == "__main__":
    unittest.main()
