# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:11:07 2024

@author: LAPTOP
"""

n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += (2*i - 1) / (2*i)
print("Tổng S =", S)