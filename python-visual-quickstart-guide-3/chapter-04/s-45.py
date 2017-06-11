# -*- coding: utf-8 -*-
import unittest

n = input('How many number to sum?')
n = int(n)
total = 0
for i in range(n):
    s = input('Enter number' + str(i + 1) + ':')
    total = total + int(s)
print('The sum is ' + str(total))

