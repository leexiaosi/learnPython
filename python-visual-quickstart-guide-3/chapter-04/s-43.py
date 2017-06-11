# -*- coding: utf-8 -*-
import unittest

# 计算折扣

age = input('Input your age!').strip()
age = int(age)
if age <= 2:
    print('free')
elif 2 < age < 13:
    print('child fare')
else:
    print('adult fare')
