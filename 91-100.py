#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:40:52 2021

@author: ijin
"""

#%% 딕셔너리 2
#91-100
#%%
inventory ={"메로나" :[300,20] , "비비빅": [400, 3] , "죠스바": [250,100]}
print(inventory)

#%%
print(inventory["메로나"][0])
print(inventory["메로나"][1])

#%%
inventory["월드콘"] =[500,7]
print(inventory)

#%%
icecream ={"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
print(list(icecream.keys()))

#%%
icecream ={"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
print(list(icecream.values()))

#%%
icecream ={"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
new_product = {"팥빙수":2700, "아맛나":1000}
icecream.update(new_product)
print(icecream)

#%%
keys =("apple","pear","peach")
vals = (300,250,400)
result = dict(zip(keys, vals))
print(result)

#%%
date =['09/05' ,'09/06','09/07','09/08','09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)


