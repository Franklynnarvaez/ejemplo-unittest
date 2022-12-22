import unittest
from request import checkResponseApi, getPokemonEncoding


class TestRequest(unittest.TestCase):

    def test_checkResponseApi(self):
        res = checkResponseApi()
        self.assertEqual(res, 200)

    def test_getPokemonHeaders(self):
        res = getPokemonEncoding()
        self.assertEqual(res, 'utf-8')


if __name__ == "__main__":
    unittest.main()
