# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:54:58 2024

@author: LAPTOP
"""

import random

s = random.randint(20, 30)
print("Số lượng phần tử:",s)

ds = []
for i in range(s):
    t = random.uniform(18, 99)  
    bp = t ** 2
    ds += [bp]
print("Danh sách các giá trị bình phương:")
for gt in ds:
    print(gt)