# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:15:08 2024

@author: LAPTOP
"""

n = int(input("Nhập số nguyên dương n: "))
t = 1
for i in range(1, n + 1):
    t *= i
print(f"Giai thừa của {n} là: {t}")
