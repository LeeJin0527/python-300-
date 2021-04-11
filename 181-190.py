# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:11:14 2021

@author: jin
"""

##181-190
#%%
apart = [[101, 102],
         [201, 202],
         [301, 302]]

print(apart)

#%%
stock =[["시가",100, 200, 300],
        ["종가",80,210,330]]
print(stock)
#%%
stock = {"10/10": [80, 110, 70, 90], 
         "10/11": [210, 230, 190, 200]}
print(stock)

#%%
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    print(i[0] , "호")
    print(i[1] ,"호")
    
#%%
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    print(i[0] , "호")
    print(i[1] ,"호")
    
#%%
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j,"호")
#%%
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::]:
    for j in i[::]:
        print(j,"호")
        print("------")
        
#%%
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::]:
    for j in i[::]:
        
        print(j,"호")
    print("----")
    
#%%
apart = [ [101, 102], [201, 202], [301, 302] ]

for i in apart[::]:
    for j in i[::]:
        
        print(j,"호")
print("----")