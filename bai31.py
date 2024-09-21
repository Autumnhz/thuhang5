# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:51:45 2024

@author: LAPTOP
"""

while True:
    try:
       a = int(input("Nhập cạnh a: "))
       b = int(input("Nhập cạnh b: "))
       c = int(input("Nhập cạnh c: "))
       if a > 0 and b > 0 and c > 0:
        break
       print("Ba cạnh phải là các số nguyên dương. Vui lòng nhập lại!")
    except ValueError:
          print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Ba cạnh này không tạo thành một tam giác!")