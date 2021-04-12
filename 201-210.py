#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:45:11 2021

@author: ijin
"""

## 201-210
#%%
def print_coin():
    print("비트코인")
    
print_coin()

#%%
def print_coins():
    for i in range(100):
        print("비트코인")
        
print_coins()

#%%
##에러 뜨는 이유? 함수 정의보다 호출이 먼저 됨 
# hello()
# def hello():
#     print("Hi")
    
#%%
def message():
    print("A")
    print("B")
    
message()
print("C")
message()

#%%
print("A")

def message():
    print("B")

print("C")
message()

#%%
print("A")
def message1():
    print("B")
print("C")
def message2():
    print("D")
message1()
print("E")
message2()

#%%
def message1():
    print("A")
    
def message2():
    print("B")
    message1()
    
message2()

#%%
def message1():
    print("A")
    
def message2():
    print("B")
    
def message3():
    for i in range(3):
        message2()
        print("C")
    message1()
    
message3()
