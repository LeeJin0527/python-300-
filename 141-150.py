# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:27:37 2021

@author: jin
"""

## 141-150
#%%
리스트 = [100, 200, 300]
for i in 리스트:
    print(int( i +10))
    
#%%
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:" , i)
    
#%%
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for  i in 리스트:
    print(len(i))
    
#%%
리스트 = ['dog', 'cat', 'parrot']
for  i in 리스트:
    print(i , len(i))
    
#%%
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])
    
#%%
리스트 = [1, 2, 3]
for i in 리스트:
    print( str(3) +"x"+ str(i))
    
#%%
리스트 = [1, 2, 3]
for i in 리스트:
    print( str(3) +"x"+ str(i) +"=" , i * 3)
    
#%%
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)
    
#%%
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2]:
    print(i)
    
#%%
리스트 = ["가", "나", "다", "라"]
for i in reversed(리스트):
    print(i)
    
#%%
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
    print(i)
