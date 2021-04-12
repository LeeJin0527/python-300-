#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:05:23 2021

@author: ijin
"""

## 221-230
#%%
def print_reverse(문자열):
    print(문자열[::-1])
    
print_reverse("python")

#%%

def print_score(리스트):
    sum =0
    for i in 리스트:
        
        sum = sum +i
    print(sum / len(리스트))


print_score([1, 3, 2])
        
#%%
def print_even(리스트):
    for i in 리스트:
        if i % 2 ==0:
            print(i)
            
print_even([1, 3, 2, 10, 12, 11, 15])

#%%
def print_keys(딕셔너리):
    for i in 딕셔너리.keys():
        print(i)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})      

#%%
##밸류는 배열 값 구할 때 처럼 하면 됨 
def print_value_by_key(딕셔너리, key):
    print(딕셔너리[key])
    
    
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}        
print_value_by_key(my_dict, "10/26")    

#%%
def print_5xn(문자열):
    num = int(len(문자열) /5)
    for i in range(num +1):
        print(문자열[i*5:i*5+5])
print_5xn("아이엠어보이유얼어걸")

#%%
def printmxn(문자열, num):
     num1 = int(len(문자열) /3)
     for i in range(num1 +1):
         print(문자열[i*num :i*num+num])
printmxn("아이엠어보이유알어걸", 3)

#%%
def calc_monthly_salary(annual_salary):
    print(int(annual_salary /12))
    
calc_monthly_salary(12000000)

#%%
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)
    
my_print(a = 100, b = 200)

#%%
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)
    
my_print(b = 100, a = 200)

                  
                  


