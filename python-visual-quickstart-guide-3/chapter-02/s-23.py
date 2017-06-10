# -*- coding: utf-8 -*-
import unittest


class S23Test(unittest.TestCase):
    # 加法
    def test_add(self):
        value = 3.5 + 42.7
        self.assertEqual(value, 46.2)

    # 减法
    def test_sub(self):
        value = 3.5 - 42.7
        self.assertEqual(value, -39.2)

    # 乘法
    def test_multi(self):
        value = 3.5 * 42
        self.assertEqual(value, 147.0)

    # 除法
    def test_division(self):
        value = 42.7 / 34.8
        self.assertGreater(value, 1)

    # 科学记数
    def test_scientific_notation(self):
        value = 2.30e2
        self.assertEqual(value, 230.0)

    # 整除
    def test_divide_exactly(self):
        value = 42.3 // 4
        self.assertEqual(value, 10.0)

    def test_test_remainder(self):
        value = 42.0 % 4
        self.assertEqual(value, 2.0)

    def test_complex_number(self):
        value = 1j * 1j
        self.assertEqual(value, -1)


if __name__ == "__main__":
    unittest.main()
