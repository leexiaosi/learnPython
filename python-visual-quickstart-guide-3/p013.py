import unittest


class P13Test(unittest.TestCase):
    def test_remainder(self):
        value = 32.33 % 3
        self.assertGreater(value, 2)

    def test_divide(self):
        value = 33.33 // 3
        self.assertEquals(value, 11)

    def test_science(self):
        value = 2.3e02
        self.assertEquals(value, 230.0)

    def test_declare_01(self):
        value = 3.
        self.assertEquals(value, 3.0)

    def test_declare_02(self):
        value = 3.0
        self.assertEquals(value, 3.0)

    def test_declare_03(self):
        value = .5
        self.assertEquals(value, 0.5)

    def test_declare_04(self):
        value = 0.5
        self.assertEquals(value, 0.5)


if __name__ == '__main__':
    unittest.main()
