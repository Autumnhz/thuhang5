# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:18:50 2024

@author: LAPTOP
"""

k = float(input("Nhập quãng đường đi được: "))
tong_tien = 0
km_da_di = 0
if k > 0:
    tong_tien += 15000
    km_da_di += 1
while km_da_di < k:
    if km_da_di < 5:
        tong_tien += 13500
    else:
        tong_tien += 11000
    km_da_di += 1
if k > 120:
    tong_tien *= 0.9
print("Tổng số tiền phải trả là:", tong_tien, "VND")