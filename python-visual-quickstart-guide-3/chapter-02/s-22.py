# -*- coding: utf-8 -*-
import unittest


class S22Test(unittest.TestCase):
    # 加法
    def test_add(self):
        value = 5 + 9
        self.assertEqual(value, 14)

    # 减法
    def test_sub(self):
        value = 22 - 6
        self.assertEqual(value, 16)

    # 乘法
    def test_multi(self):
        value = 12 * 14
        self.assertEqual(value, 168)

    # 指数
    def test_exponent(self):
        value = 2 ** 4
        self.assertEqual(value, 16)

    # 余数
    def test_remainder(self):
        value = 25 % 7
        self.assertEqual(value, 4)

    # 复合运算
    def test_compound_operation(self):
        value = 1 + 2 * 3
        self.assertEqual(value, 7)

    # 整除
    def test_divide_exactly(self):
        value = 7 // 4
        self.assertEqual(value, 1)

    # 大数
    def test_great_number(self):
        value = 27 ** 100
        self.assertGreater(value, 10000)


if __name__ == "__main__":
    unittest.main()
