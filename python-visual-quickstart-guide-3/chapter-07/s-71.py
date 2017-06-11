import unittest


class S71Test(unittest.TestCase):
    def test_type_5(self):
        self.assertEqual(str(type(5)), "<type 'int'>")

    def test_type_5_0(self):
        self.assertEqual(str(type(5.0)), "<type 'float'>")


if __name__ == '__main__':
    unittest.main()
