# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:50:08 2024

@author: LAPTOP
"""

s = int(input("Nhập số xe của bạn (4 chữ số): "))
tong = 0
while s > 0:
    chu_so = s % 10  
    tong += chu_so
    s //= 10
print("Số nút của biển số xe của bạn là:", tong)