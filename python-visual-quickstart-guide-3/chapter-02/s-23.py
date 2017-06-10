# -*- coding: utf-8 -*-
import unittest


class S23Test(unittest.TestCase):
    # 加法
    def test_add(self):
        value = 3.5 + 42.7
        self.assertLess(value, 100)

    # 减法
    def test_sub(self):
        value = 3.5 - 42.7
        self.assertLess(value, 1)

    # 乘法
    def test_multi(self):
        value = 3.5 * 42
        self.assertLess(value, 200)

    # 除法
    def test_divi(self):
        value = 42.7 / 34.8
        self.assertGreater(value, 1)

    # 科学记数
    def test_kexue(self):
        value = 2.30e2
        self.assertEqual(value, 230.0)


if __name__ == "__main__":
    unittest.main()
