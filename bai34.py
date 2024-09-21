# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:49:18 2024

@author: LAPTOP
"""

n = int(input("Nhập vào số nguyên dương n: "))
if n <= 1:
    print(n, "không phải là số nguyên tố.")
else:
    so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            so_nguyen_to = False
            break

    if so_nguyen_to:
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải là số nguyên tố.")