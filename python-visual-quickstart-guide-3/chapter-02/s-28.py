# -*- coding: utf-8 -*-
import unittest


class S28Test(unittest.TestCase):
    # 将整数转化为浮点
    def test_int2float(self):
        value = float(3)
        self.assertEqual(value, 3.0)

    # 将字符串转换成浮点
    def test_string2float(self):
        value = float('2.34')
        self.assertEqual(value, 2.34)

    # 将整数转化成字符串
    def test_int2str(self):
        value = str(2)
        self.assertEqual(value, '2')

    # 将浮点转化成字符串
    def test_float2str(self):
        value = str(2.34)
        self.assertEqual(value, '2.34')

    # 自动转换
    def test_auto(self):
        value = 2.5 * 4
        self.assertEqual(value, 10.0)

    # 浮点转化成整数
    def test_float2int(self):
        value = int(2.34)
        self.assertEqual(value, 2)

    # 圆整
    def test_float2round(self):
        value = round(8.75)
        self.assertEqual(value, 9)

    # 银行家圆整
    def test_float2round2(self):
        value = round(8.5)
        self.assertEqual(value, 8)


if __name__ == '__main__':
    unittest.main()
