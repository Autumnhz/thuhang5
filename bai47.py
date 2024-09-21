# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:37:21 2024

@author: LAPTOP
"""

max_sum = 0
s = []

xmax = 979 // 2
ymax = 979 // 7
zmax = 979 // 9
for x in range(1, xmax + 1):
    for y in range(1, ymax + 1):
        for z in range(1, zmax + 1):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong > max_sum:
                    max_sum = tong
                    s = [x, y, z]
print("Bộ nghiệm có tổng lớn nhất:", s)