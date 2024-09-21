# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:12:51 2024

@author: LAPTOP
"""

while True:
    try:
        n = int(input("Nhập vào một số nguyên dương N: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")

print("Các ước số của", n, "là:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = '')