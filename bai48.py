# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:28:31 2024

@author: LAPTOP
"""

m = float('inf')
s = None
for x in range(1, 979):
    for y in range(1, 979 - x):
        z = (979 - 2*x - 7*y) / 9
        if z > 0 and z.is_integer():
            tong = x + y + z
            if tong < m:
               m = tong
               s = (x, y, int(z))
if s:
    print("Bộ nghiệm nguyên (x, y, z) có tổng nhỏ nhất là:", s)
else:
    print("Error!")