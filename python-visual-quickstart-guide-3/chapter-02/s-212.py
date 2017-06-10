# -*- coding: utf-8 -*-
import unittest


class S212Test(unittest.TestCase):
    # 多重赋值
    def test_multiassign(self):
        x, y, z = 1, 'a', 3.14
        self.assertEqual(x, 1)
        self.assertEqual(y, 'a')
        self.assertEqual(z, 3.14)


if __name__ == '__main__':
    unittest.main()
