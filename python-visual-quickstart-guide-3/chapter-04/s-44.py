# -*- coding: utf-8 -*-
import unittest

class S44Test(unittest.TestCase):
    def for_in_loop(self):
        for i in range(10):
            print(i)
        self.assertEqual(i, 9)

    def while_loop(self):
        i = 0
        while i < 10:
            print(i)
        self.assertEqual(i, 10)

if __name__ == '__main__':
    unittest.main()


