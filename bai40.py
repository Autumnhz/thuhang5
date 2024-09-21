# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:40:42 2024

@author: LAPTOP
"""

n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += 1 / (2 * i)
print("Tổng S =", S)