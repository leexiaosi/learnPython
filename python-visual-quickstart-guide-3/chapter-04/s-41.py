# -*- coding: utf-8 -*-
import unittest


class S41Test(unittest.TestCase):
    # 全是false
    def test_false_false(self):
        p = False
        q = False
        self.assertEqual(p == q, True)
        self.assertEqual(p != q, False)
        self.assertEqual(p and q, False)
        self.assertEqual(p or q, False)
        self.assertEqual(not p, True)

    # false,true
    def test_flase_true(self):
        p = False
        q = True
        self.assertEqual(p == q, False)
        self.assertEqual(p != q, True)
        self.assertEqual(p and q, False)
        self.assertEqual(p or q, True)
        self.assertEqual(not p, True)

    # true,true
    def test_true_true(self):
        p = True
        q = True
        self.assertEqual(p == q, True)
        self.assertEqual(p != q, False)
        self.assertEqual(p and q, True)
        self.assertEqual(p or q, True)
        self.assertEqual(not p, False)

    # true,false
    def test_true_false(self):
        p = True
        q = False
        self.assertEqual(p == q, False)
        self.assertEqual(p != q, True)
        self.assertEqual(p and q, False)
        self.assertEqual(p or q, True)
        self.assertEqual(not p, False)


if __name__ == '__main__':
    unittest.main()
