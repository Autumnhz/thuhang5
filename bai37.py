# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:14:45 2024

@author: LAPTOP
"""

n = int(input("Nhập n: "))
if n % 2 == 0 and n > 0:
    S = n // 2 * (n // 2 + 1)
    print("Tổng S =", S)
else:
    print("Không hợp lệ!")