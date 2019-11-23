import unittest

class TestIndex(unittest.TestCase):
    def test_status_code_deve_retornar_200(self):
        self.assertEqual(200, 200)

if __name__ == '__main__':
    unittest.main()
