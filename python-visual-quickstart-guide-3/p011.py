import unittest


class P11Test(unittest.TestCase):
    def test_add(self):
        value = 5 + 9
        self.assertEquals(value, 14)

    def test_sub(self):
        value = 22 - 6
        self.assertEquals(value, 16)

    def test_division(self):
        value = 22 / 7
        self.assertGreater(value, 2)

    def test_exponential(self):
        value = 2 ** 4
        self.assertEquals(value, 16)

    def test_remainder(self):
        value = 25 % 7
        self.assertEquals(value, 4)

    def test_operation_1(self):
        value = 1 + 2 * 3
        self.assertEquals(value, 7)

    def test_operation_2(self):
        value = (1 + 2) * 3
        self.assertEquals(value, 9)

    def test_rounding(self):
        value = 7 // 3
        self.assertEquals(value, 2)


if __name__ == '__main__':
    unittest.main()
