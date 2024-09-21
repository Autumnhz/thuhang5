# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:45:31 2024

@author: LAPTOP
"""

import math
n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
   cb2 = math.sqrt(n)
   if cb2 - int(cb2) == 0:
      print(n, "là số chính phương.")
   else:
      print(n, "không phải là số chính phương.")
else:
    print("Vui lòng nhập số nguyên dương!")