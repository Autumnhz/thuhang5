# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:06:15 2024

@author: LAPTOP
"""

n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += i / (i+1)
print("Tổng S =", S)