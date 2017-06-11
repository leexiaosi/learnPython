import unittest

class S51Test(unittest.TestCase):
    def pow_call(self):
        n = pow(2, 5)
        self.assertEqual(n, 32)


if __name__ == '__main__':
    unittest.main()
