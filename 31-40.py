#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:12:15 2021

@author: ijin
"""

#문자열 합치기 
#%%
a = "3"
b = "4"
print( a + b)

#%%
print("Hi" * 3)

#%%
print("-" * 80)

#%%
t1 = 'python'
t2 = 'java'

sum = t1 + ' '+ t2 + ' '
print(sum * 5)

#%%
name1 = "김민수"
age1 = 10 
name2 = "이철희"
age2 = 13

print("이름 : %s 나이 : %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

#%%

name1 = "김민수"
age1 = 10 
name2 = "이철희"
age2 = 13



print("이름: {} 나이: {}".format(name1 , age1))
print("이름: {} 나이:{}".format(name2, age2))

#%%

name1 = "김민수"
age1 = 10 
name2 = "이철희"
age2 = 13


print(f"이름: {name1} 나이: {age1}")
print(f"이름:{name2} 나이: {age2}")

#%%
상장주식주 = "5,969,782,550"
상장주식주_in = 상장주식주.replace("," , "")
타입변환 = int(상장주식주_in)
print(타입변환)
#상장주식주_in.replace(","," ")
#print(상장주식주_in)
#%%

분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

#%%
data ="   삼성전자     "
data1 = data.strip()
print(data1)


