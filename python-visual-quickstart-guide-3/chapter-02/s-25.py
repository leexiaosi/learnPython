# -*- coding: utf-8 -*-
import unittest


class S25Test(unittest.TestCase):
    # 单引号
    def test_single_quote(self):
        value = 'hello'
        self.assertEqual(value, 'hello')

    # 双引号
    def test_double_quote(self):
        value = "hello"
        self.assertEqual(value, 'hello')

    # 三引号
    def test_three_quote(self):
        value = '''hello'''
        self.assertEqual(value, 'hello')

    # 字符串拼接
    def test_join(self):
        value = 'hello' + 'world'
        self.assertEqual(value, 'helloworld')

    # 乘法
    def test_multi(self):
        value = 'hello' * 3
        self.assertEqual(value, 'hellohellohello')

    # 字符串长度
    def test_length(self):
        value = len('abcd')
        self.assertEqual(value, 4)


if __name__ == '__main__':
    unittest.main()
