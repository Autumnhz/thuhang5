# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:35:51 2024

@author: LAPTOP
"""

print("Danh sách các số chẵn nguyên chia hết cho 5:")
for i in range(2018, 2829, 2):
    if i % 5 == 0:
        print(f"{i},  ", end ='')
        