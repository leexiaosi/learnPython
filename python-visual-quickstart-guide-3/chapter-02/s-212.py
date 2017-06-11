# -*- coding: utf-8 -*-
import unittest


class S212Test(unittest.TestCase):
    # 多重赋值
    def test_multi_assign(self):
        x, y, z = 1, 'a', 3.14
        self.assertEqual(x, 1)
        self.assertEqual(y, 'a')
        self.assertEqual(z, 3.14)

    # 交换变量
    def test_swipe_variable(self):
        a, b = 5, 9
        self.assertEqual(a, 5)
        self.assertEqual(b, 9)



if __name__ == '__main__':
    unittest.main()
