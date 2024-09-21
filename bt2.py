# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:57:49 2024

@author: LAPTOP
"""

print("Danh sách các số chia hết cho 9:")
ds = []
for i in range(2020,3839,2):
    if i % 9 == 0:
        print(f"{i} ", end ='')
        
        