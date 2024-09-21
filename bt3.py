# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:52:22 2024

@author: LAPTOP
"""

n = int(input("Nhập giá trị nguyên n: "))
dict = {i:i**i for i in range(1, n+1)}
print(dict)