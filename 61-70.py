#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:18:49 2021

@author: ijin
"""

#%% 
#61-70 
price = ['20180728', 100, 130, 140, 150, 160, 170]
price_cut = price[1:]
print(price_cut)

#%%

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_cut = nums[::2]
print(nums_cut)

#%%
nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_cut = nums[1::2]
print(nums_cut)

#%%
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#%%
interest = ['삼성전자 ', 'LG전자 ', 'Naver']

print(interest[0] , interest[2])

#%%
interest = ['삼성전자', 'LG전자', 'Naver','SK하이닉스','미래에셋대우']
print("/".join(interest))

#%%
interest1 = ['삼성전자', 'LG전자', 'Naver','SK하이닉스','미래에셋대우']
print("\n".join(interest1))

#%%
string = "삼성전자/ LG전자/ Naver"
interest = string.split("/")
print(interest)

#%%
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
#data1 = sorted(data)
#print(data1)






