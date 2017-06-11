import unittest
import math


def shop(where='store', what='pasta', howmuch='10 pounds'):
    print('I want you to go the', where)
    print('and buy', howmuch, 'of', what, '.')

shop()
shop(what='towels')
shop(howmuch='a ton', what='towels')
shop(howmuch='a ton', what='towels', where='bakery')