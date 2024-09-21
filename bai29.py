# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:19:14 2024

@author: LAPTOP
"""

n = int(input("Nhập số nguyên dương N: "))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print("Tổng các chữ số của N là:", sum)