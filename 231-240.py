#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:33:58 2021

@author: ijin
"""

###231-240
#%%
##에러발생 return 값이 없음 
# def n_plus_1(n):
#     result = n + 1
    
# n_plus_1(3)
# print(result)

#%%
def make_url(문자열):
    return "www."+문자열+".com"

answer = make_url("naver")
print(answer)

#%%
def make_list(문자열):
    return list(문자열)

answer = make_list("abcd")
print(answer)

#%%
def pickup_even(리스트):
    for i in 리스트:
        if i % 2 ==0:
            answer.append(i)
    return answer

answer =[]
qu = pickup_even([3, 4, 5, 6, 7, 8])
print(qu)

#%%
def convert_int(문자열):
    answer = 문자열.replace(',','')
    return(answer)
    
    
qu = convert_int("1,234,567")

print(qu)

#%%
def 함수(num):
    return num +4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#%%
def 함수(num):
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#%%
def 함수1(num):
    return num +4

def 함수2(num):
    return num +10

a = 함수1(10)
c = 함수2(a)
print(c)

#%%
def 함수1(num):
    return num + 4
def 함수2(num):
    num = num +2
    return 함수1(num)

c  = 함수2(10)
print(c)

#%%
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)