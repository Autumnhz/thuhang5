# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:17:12 2024

@author: LAPTOP
"""

n = int(input("Nhập n: "))
if n % 2 != 0 and n > 0:
    S = 1
    for i in range(1, n+1, 2):
        S *= i
    print("Tích S =", S)
else:
    print("Không hợp lệ!")