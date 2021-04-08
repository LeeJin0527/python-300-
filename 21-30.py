#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:42:03 2021

@author: ijin
"""

#21-30
#문자열 인덱싱
#%%
letters = 'python'
print(letters[0],letters[2])

#%%
#뒤에서 부터 가져오기 
license_plate = "24가 2210"
print(license_plate[-4:])

#%%
string = "홀짝홀짝홀짝"
print(string[0:5:2])

#%%
string ="PYTHON"
print(string[::-1])

#%%
phone_number = "010-1111-2222"

phone_number1 = phone_number.replace("-"," ")
print(phone_number1)

#%%
phone_number = "010-1111-2222"

phone_number1 = phone_number.replace("-","")
print(phone_number1)

#%%
url = "http://shareebook.kr"
url_split = url.split(".")
print(url_split[-1])

#%%
#문자열은 immutable
lang = 'python'
lang[0] ='P'
print(lang)

#%%
string = 'abcert45345asdasd'
change_str = string.replace("a","A")
print(change_str)

#%%
#그대로 출력됨 
string ='abcd'
string.replace('b','B')
print(string)


