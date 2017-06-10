# -*- coding: utf-8 -*-
import unittest


class S33Test(unittest.TestCase):
    # 输入文件
    def test_input(self):
        name = input('What is your name?')
        print('hello ' + name.capitalize() + '!')
        self.assertEqual(name, 'ldh')

    # 过滤空白
    def test_strip(self):
        name = input('What is your name?').strip()
        print('hello ' + name.capitalize() + '!')
        self.assertEqual(name, 'ldh')

    # 数字
    def test_number(self):
        value = input('Enter number:').strip()
        number = int(value) + 10
        print('the value is ' + str(number))
        self.assertEqual(number, 20)


if __name__ == '__main__':
    unittest.main()
