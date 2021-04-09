#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:26:27 2021

@author: ijin
"""

##파이썬 딕셔너리 
#81-90
#%%
#별표현식 
a, b, *c =(0, 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

#%%start expression
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,_,_ =scores
print(valid_score) 

#%%
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*valid_score =scores
print(valid_score)

#%%
temp = {}
print(temp)

#%%
temp = {"메로나":1000, "폴라포": 1200, "빵빠레":1800}
print(temp)

#%%
temp["죠스바"] =1200
temp["월드콘"]=1200
print(temp)

#%%
print(temp["메로나"])

#%%
temp["메로나"] =1300
print(temp)

#%%
del temp["메로나"]
print(temp)

#%%
#딕셔너리에 없는 키 값을 사용하면 에러 발생 