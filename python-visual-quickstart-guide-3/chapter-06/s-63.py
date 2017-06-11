import unittest


def get_ext(fname):
    """
    Returns the extension of file frame
    :param fname:
    :return:
    """
    dot = fname.rfind('.')
    if dot == -1:
        return ''
    else:
        return fname[dot + 1:]


class S63Test(unittest.TestCase):
    def test_hello_text(self):
        ext = get_ext('hello.text')
        self.assertEqual(ext, 'text')

    def test_pizza_py(self):
        ext = get_ext('prizza.py')
        self.assertEqual(ext, 'py')


if __name__ == '__main__':
    unittest.main()
