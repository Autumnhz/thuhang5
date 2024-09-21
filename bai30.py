# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:38:36 2024

@author: LAPTOP
"""

while True:
    try:
        m = int(input("Nhập tháng: "))
        y = int(input("Nhập năm: "))
        if 1 <= m <= 12:
            break
        else:
            print("Tháng không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")

nhuan = False
if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
    nhuan = True
if m in (4, 6, 9, 11):
   d = 30
elif m == 2:
    d = 29 if nhuan else 28
else:
    d = 31
print("Tháng", m, "năm", y, "có", d, "ngày.")