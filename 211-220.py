#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:54:32 2021

@author: ijin
"""

##211 -220
#%%
def 함수(문자열):
    print(문자열)
    
함수("안녕")
함수("Hi")

#%%
def 함수(a, b):
    print(a + b)
    
함수(3, 4)
함수(7, 8)

#%%
##에러 뜨는 이유? 파라미터를 입력하지 않았다
# def 함수(문자열):
#     print(문자열)
    
# 함수()

#%%
##에러뜨는 이유? 파라미터 타입이 안맞음 
# def 함수(a, b):
#     print( a+ b)
    
# 함수("안녕", 3)


#%%
def print_with_smile(문자열):
    print(문자열 + ":D")
    
print_with_smile("지니")


#%%
def print_upper_price(price):
    print(price * 1.3)
    
print_upper_price(1000)

#%%
def print_sum(a, b):
    print( a + b)
    
print_sum(3, 4)

#%%
def print_arithmetic_operation(a, b):
    print(a, "+", b ,"=", a + b)
    print(a, "-", b ,"=", a - b)
    print(a, "*", b ,"=", a * b)
    print(a, "/", b ,"=", a / b)
    
print_arithmetic_operation(3, 4)


#%%
def print_max(a, b, c):
    print(max(a, b, c))
    
print_max(4, 3, 1)







    