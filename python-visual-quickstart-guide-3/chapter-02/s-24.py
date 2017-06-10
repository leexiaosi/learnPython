# -*- coding: utf-8 -*-
import unittest
import math


class S24Test(unittest.TestCase):
    # 大于或等于的整数
    def test_ceil(self):
        value = math.ceil(3.333)
        self.assertEqual(value, 4)

    # 平方根
    def test_sqrt(self):
        value = math.sqrt(4)
        self.assertEqual(value, 2)


if __name__ == '__main__':
    unittest.main()
