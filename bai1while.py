# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:11:58 2024

@author: LAPTOP
"""

while True:
    try:
       n = int(input("Nhập vào một số nguyên: "))
       if -99 <= n <= 99:
         break 
       else:
           print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
         print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại!")
  
