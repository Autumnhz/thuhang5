# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:58:49 2024

@author: LAPTOP
"""

for x in range(1, 980 // 2 + 1):
    for y in range(1, 980 // 7 + 1):
        for z in range(1, 980 // 9 + 1):
            if 2 * x + 7 * y + 9 * z == 979:
                print(f"Bộ nghiệm: x = {x}, y = {y}, z = {z}")