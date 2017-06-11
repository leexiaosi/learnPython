import unittest

def codesum1(s):
    """Returns the sums of the character codes of s
    """
    total = 0
    for c in s:
        total = total + ord(c)
    return total


class S61Test(unittest.TestCase):
    def test_code_sum(self):
        count = codesum1('Hi there')
        self.assertEqual(count, 778)


if __name__ == '__main__':
    unittest.main()
