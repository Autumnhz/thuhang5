# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:16:27 2024

@author: LAPTOP
"""

def tong(n):
    return n * (n + 1) // 2
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
S = 0
for i in range(1, n+1):
    ms = tong(i)
    S += (x**i) / ms
print("Tổng S =", S)