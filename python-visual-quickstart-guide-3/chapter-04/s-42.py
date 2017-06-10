# -*- coding: utf-8 -*-
import unittest


class S42Test(unittest.TestCase):
    # if语句
    def test_password(self):
        pwd = input('what is the passwd?')
        if pwd == 'apple':
            # note use of ==
            # instend of =
            print('Logging on ...')
        else:
            print('Incorrent password')
            print('All done!')
        self.assertEqual(pwd, 'hello')


if __name__ == '__main__':
    unittest.main()
