#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:01:46 2021

@author: ijin
"""

##71-80 
#파이썬 튜플 
#%%
m_v = ()
print(type(m_v))

#%%
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

#%%
tu = (1)
print(tu)

#%% error 
t = (1, 2, 3)
t[0] ='a'
print(t[0])

#%%
t = 1, 2, 3, 4
print(type(t))
#%%
t = ('a' , 'b', 'c')
t = ('A', 'b', 'c')
print(t)

#%%
interest = ('삼성전자 ', 'LG전자', 'SK Hynix')
inter = list(interest)
print(inter)

#%%
inter1 = tuple(inter)
print(inter1)

#%%
temp = ('apple', 'banana' ,'cake')
a, b, c = temp
print(a, b, c)

print(type(a))

#%%
data = tuple(range(2,100, 2))
print(data)



