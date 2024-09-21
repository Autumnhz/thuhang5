# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:52:58 2024

@author: LAPTOP
"""

n = int(input("Nhập n: "))
S = 0
for i in range(1, 2*n+2, 2):
    S += 1/i
print("Tổng S =", S)