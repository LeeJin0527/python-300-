#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:50:32 2021

@author: ijin
"""

#%% 51-60
#파이썬 리스트 

movie_rank = ["닥터 스트레인지", "스플릿" , "럭키"]
print(movie_rank)

#%%
movie_rank.append("배트맨")
print(movie_rank)

#%%
movie_rank .insert(1,"슈퍼맨")
print(movie_rank)

#%%
del movie_rank[0]
del movie_rank[0]

print(movie_rank)

#%%
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1+ lang2
print(langs)

#%%
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

#%%
nums = [ 1, 2, 3, 4, 5]
print(sum(nums))

#%%
cook = ["피자 ", "김밥" , "만두", "양념치킨 ", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#%%

nums = [1, 2, 3, 4, 5]
avg = sum(nums) / len(nums)
print(avg)







